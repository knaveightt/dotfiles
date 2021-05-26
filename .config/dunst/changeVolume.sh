#!/bin/bash
# changeVolume

# Arbitrary but unique message id
msgId="991049"

# Change the volume using alsa(might differ if you use pulseaudio)
if [[ $@ == "mute" ]]; then
    amixer -q set Master toggle
else
    amixer -D pulse sset Master "$@"
fi

# Query amixer for the current volume and whether or not the speaker is muted
volume="$(amixer -D pulse get Master | tail -1 | awk '{print $5}' | sed 's/[^0-9]*//g')"
mute="$(amixer -D pulse get Master | tail -1 | awk '{print $6}')"
if [[ $volume == 0 || "$mute" == "[off]" ]]; then
    # Show the sound muted notification
    dunstify -a "changeVolume" -u low -i audio-volume-muted -r "$msgId" "Volume Muted" 
else
    # Show the volume notification
    dunstify -a "changeVolume" -u low -i audio-volume-high -r "$msgId" -h int:value:"$volume" "Volume: ${volume}%"
fi

