import collections
import sys
import numpy as np
import pyaudio

ATHEON = False

#0 off, 1 prints all sounds, 2 prints those making it through your filters
DEBUG = 0

#ignore notes below this volume
DECIBEL_CUTOFF = 20
#must be this close to the note
DIFF_CUTOFF = 0.04
#had issues detecting b flat (7), so has a special condition for that
B_FLAT_MIN = 59.05
B_FLAT_MAX = 59.17
#use below two variables for how long the queue of notes should be, and how many are needed to trigger a print
QUEUE_LENGTH = 8
NOTES_IN_QUEUE_REQUIRED = 5

NOTE_MIN = 60
NOTE_MAX = 69
FSAMP = 22050
FRAME_SIZE = 2096
FRAMES_PER_FFT = 16
SAMPLES_PER_FFT = FRAME_SIZE * FRAMES_PER_FFT
FREQ_STEP = float(FSAMP) / SAMPLES_PER_FFT

if(ATHEON):
    NOTE_NAMES = 'C N D N E N F# G N A N N'.split()
else:
    NOTE_NAMES = 'C N D N E N F# G N A Bb N'.split()

def freq_to_number(f): return 69 + 12 * np.log2(f / 440.0)
def number_to_freq(n): return 440 * 2.0 ** ((n - 69) / 12.0)
def note_name(n): return NOTE_NAMES[n % 12]

def note_to_location(n):
    if (n == "A"): return "far left, " if ATHEON else "1"
    if (n == "F#"): return "close middle, " if ATHEON else "2"
    if (n == "D"): return "far right, " if ATHEON else "3"
    if (n == "C"): return "far middle, " if ATHEON else "4"
    if (n == "E"): return "close right, " if ATHEON else "5"
    if (n == "G"): return "close left, " if ATHEON else "6"
    if (n == "Bb"): return "ERROR " if ATHEON else "7"

def note_to_fftbin(n): return number_to_freq(n) / FREQ_STEP
imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN - 1))))
imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX + 1))))
buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)
num_frames = 0

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
input_index = int(input("Please choose a device ID: "))
stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                input_device_index=input_index,
                                frames_per_buffer=FRAME_SIZE)
stream.start_stream()
window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, SAMPLES_PER_FFT, False)))

last_printed_note = None
samples_without_char = 0
sequence = collections.deque(QUEUE_LENGTH * [""], QUEUE_LENGTH)

while stream.is_active():
    samples_without_char += 1
    if samples_without_char == 35 or samples_without_char == 100:
        last_printed_note = None
        print("")
    buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
    buf[-FRAME_SIZE:] = np.fromstring(stream.read(FRAME_SIZE), np.int16)
    fft = np.fft.rfft(buf * window)
    s_mag = np.abs(fft) * 2 / np.sum(window)
    s_dbfs = (20 * np.log10((s_mag / 32768))) + 120
    decibel = (sum(s_dbfs) / len(s_dbfs))
    if ((sum(s_dbfs) / len(s_dbfs)) < DECIBEL_CUTOFF):
        continue
    freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP
    n = freq_to_number(freq)
    n0 = int(round(n))
    note = note_name(n0)
    diff = n - n0
    num_frames += 1
    if num_frames >= FRAMES_PER_FFT:
        if (DEBUG == 1):
            print("note: {:>3f} {:>3s} {:+.2f} {}".format(n, note, diff, decibel))
        if ((abs(diff) < DIFF_CUTOFF and note != "N") or (n > B_FLAT_MIN and n < B_FLAT_MAX)):
            if(note == "N"):
                if(ATHEON):
                    continue
                note = "Bb"
            if (DEBUG == 2):
                print("note: {:>3s} {:+.2f} {}".format(note, diff, decibel))
            sequence.append(note)
            if ((sum(elem == note for elem in sequence)) == NOTES_IN_QUEUE_REQUIRED and last_printed_note!=note):
                if(DEBUG != 0):
                    print("IF NOT DEBUG", note_to_location(note))
                else:
                    print(note_to_location(note), end='')
                    sys.stdout.flush()
                last_printed_note = note
                samples_without_char = 0
