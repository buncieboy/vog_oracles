# How to get PC output as input

The script requires an input audio device, as it needs to read the data coming in. To do this on PC we have to convert the games output to an audio input.

### Stereo mix
If you are just using solo, or your team can shutup / you can mute them during it, then you could just enable stereo mix under recording devices, which is your entire PC audio output. However, I know this won't work for most people as they want to have full VC whilst getting the script to also write the order to verify, so we need to isolate the games output your VC.

If you are using in game voice chat I can't really do much for you. However assuming you are using Discord or some other VC program the following options might help.

## Isolating game and VC audio

Let me know how these options work for you, and if you have any suggestions, code or apps/settings, that could work better. Unfortunately it is not as easy as I would have hoped to isolate the game audio, and I can find 0 ways to make it work through code alone.

As with anything on the internet use your own caution when installing anything, I didn't write any of these so cannot garuntee their safety or effectiveness. Don't blame me if it doesn't work or anything bad happens.

### Option 1 - Virtual Audio Cable (VAC)
1. Install [VAC](https://vac.muzychenko.net/en/download.htm) trial
   - It will warn you it will reset your default devices, follow the instructions to change them back
1. At this point your audio should be exactly the same as it was before
1. Open up sound settings and click on "app volume and device preferences" under the advanced sound options
1. Find Destiny 2 (might have to be running) and change the output from default (or whatever it was) to Line 1
    - You might be able / have to select this from within D2, but I am an xbox player so can't test, do let me know!
1. Right click on the speaker icon in the system tray, click on sound
1. Recording tab, right click on Line 1, properties, listen tab, select listen to this device
   - You should now be able to hear your game audio again, you might need to tweak the volume
1. Now when you run the script you should be able to select Line 1 as an input

### Option 2 - VoiceMeeter
I'm not as keen on this one, as I don't like the application, and it works the same as above but with more steps, and requires the app to run in the background, but it should work. 
1. Install [voicemeeter](https://vb-audio.com/Voicemeeter/) and restart as instructed
1. Voicemeeter will have made itself the default for input and output without warning (see why I don't like it now?), so you'll want to right click on the speaker icon in the system tray, click on sound, and set your old default device and communication device for both input and output (under the playback and recording tabs)
1. At this point your audio should be exactly the same as it was before
1. Launch Voicemeeter
1. Set the hardware out (A1) to your output (Realtek audio etc)
1. Open up sound settings and click on "app volume and device preferences" under the advanced sound options
1. Find Destiny 2 (might have to be running) and change the output from default (or whatever it was) to VoiceMeeter Input
    - You might be able / have to select this from within D2, but I am an xbox player so can't test, do let me know!
1. Within VoiceMeeter Click on menu, click system tray (so you can close the app), and run on windows startup (so you don't have to boot it everytime you boot D2)    
1. Now when you run the script you should be able to select VoiceMeeter Output as an option 
   
Both of these ways should then work, and once set up properly they should not require you to start any app or check any settings to hear your D2 audio as normal. 

I was able to route chrome through both of these, and was able to blast spotify as loud as possible through my standard output, and the script worked as it only received the YouTube video (which I could also hear).