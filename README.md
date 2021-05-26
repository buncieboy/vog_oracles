# vog_oracles
### Audio processor to map oracle notes in the VoG raid in Destiny 2 to call outs.

Huge thanks to [mzucker](https://github.com/mzucker/python-tuner) on GitHub for the note detection code. Also thanks to [u/brainstormcsgo](https://www.reddit.com/r/DestinyTheGame/comments/njo9zl/had_a_bunch_of_people_asking_if_you_have_perfect/) on reddit for mapping the notes to call outs.

#### Requirements
1. [Python 3.6](https://www.python.org/downloads/release/python-360/), PyAudio, NumPy.
    - Has to be 3.6 as PyAudio hasn't been updated since.
    - Should work with any 3.6.x python version, but I have only tested on 3.6.0  
    - If you are new to python PyAudio and NumPy are python packages. To install them try running "pip install NAME", replacing NAME with the package name. If that fails google how to install python packages for your environment, or message me.
1. Game audio as PC input.
    - I have written instructions for this if you are on PC, please checkout the PC Instructions file. 
    - On console I use my monitors output as an audio line in. 
    - I haven't tested using speakers from console and a microphone as input, but it could work.
    - Try to avoid routing VC with game audio, as this will make it harder to detect notes.

#### To use
Set ATHEON constant to true if in Atheon room, false for oracles/templar. Run main.py. Your audio inputs will be listed numbered from 0 upwards, type the number for the audio input you want and press enter.

You will need to modify the constants for better results, use the debug modes to help with tweaking them. DECIBEL_CUTOFF helps to isolate background noise, but if too high it will prevent proper note detection. If you run in DEBUG mode 1 and see no output to the console its likely that DECIBEL_CUTOFF is too high. If it is at 0 and you still get no output to the console it means the audio input you selected has no audio output. 

Variables might need to change between rooms, for example I found I had to drop my decibel cutoff from 20 to 15 for Atheon.

You can change the note_to_location function to modify the callouts you want to use. By default it uses 1-7 left to right for oracles, and far/close left/middle/right for Atheon.

I recommend running in a terminal that you can easily clear, to get rid of any incorrect results between cycles.

#### Usefulness
Script is not perfect, but should help with missed calls, ordering etc. Works a lot better if you are able to isolate the oracle sounds, for example not firing weapons/using abilities.

I have not tested it as much in Atheon room, as you can't easily test it solo and there are fewer videos with good audio for it. Atheon room also has the issue of more sounds / fewer places to avoid damage, making note detection harder. If you sit on the ledge at the back it should work pretty well (if you have tweaked the settings as needed).

#### Potential future improvements
1. Improvement to B flat detection
1. Better filtering out of non oracle sounds
1. Using both rotations of the notes to figure out call, instead of printing all
1. Pulling D2 game audio directly (when on PC) without requiring user to take additional steps

If anyone has any suggestions for improvements please let me know! I'm an average player and programmer, but have no music experience, so there are definitely improvements to be made!
