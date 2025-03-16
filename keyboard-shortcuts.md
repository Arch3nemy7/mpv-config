# mpv Keyboard Shortcut Guide

This document provides a comprehensive guide to the keyboard shortcuts configured for the mpv media player. These shortcuts are designed to enhance your media viewing experience by providing quick access to various playback controls, navigation options, and other useful features. This configuration is based on the `input.conf` file and may include custom scripts and settings.

## Essential Playback Controls

| Action | Shortcut | Description |
|---|---|---|
| Play/Pause | `SPACE` | Universal play/pause toggle |
| Quit | `q` | Quick exit from mpv |
| Quit and Save Position | `shift+q` | Save position and quit player |
| Reset Playback Speed | `\` | Reset speed to normal (1.0x) |
| Decrease Playback Speed | `[` | Decrease playback speed by 0.1x |
| Increase Playback Speed | `]` | Increase playback speed by 0.1x |
| Frame Step Forward | `.` | Advance a single frame |
| Frame Step Backward | `,` | Go back a single frame |

## Navigation

| Action | Shortcut | Description |
|---|---|---|
| Next File | `n` | Next file in playlist |
| Previous File | `p` | Previous file in playlist |
| Go to Beginning | `HOME` | Jump to beginning of file |
| Go to End | `END` | Jump to end of file |
| Seek Forward 5 Seconds | `RIGHT` | Short seek forward |
| Seek Backward 5 Seconds | `LEFT` | Short seek backward |
| Seek Forward 10 Seconds | `shift+RIGHT` | Medium seek forward |
| Seek Backward 10 Seconds | `shift+LEFT` | Medium seek backward |
| Seek Forward 30 Seconds | `shift+UP` | Long seek forward |
| Seek Backward 30 Seconds | `shift+DOWN` | Long seek backward |
| Next Chapter | `shift+c` | Jump to next chapter |
| Previous Chapter | `c` | Jump to previous chapter |
| Next Chapter (Mouse) | `MOUSE_BTN8` | Next chapter using mouse button |
| Previous Chapter (Mouse) | `MOUSE_BTN7` | Previous chapter using mouse button |
| Jump to Position | `0-9` | Jump to 0-90% of the media (0=0%, 1=10%, etc.) |

## Volume Control

| Action | Shortcut | Description |
|---|---|---|
| Increase Volume | `UP` | Increase volume by 5% |
| Decrease Volume | `DOWN` | Decrease volume by 5% |
| Increase Volume (Mouse Wheel) | `AXIS_UP` | Increase volume using mouse wheel |
| Decrease Volume (Mouse Wheel) | `AXIS_DOWN` | Decrease volume using mouse wheel |
| Toggle Mute | `m` | Mute/unmute audio |

## Subtitle Controls

| Action | Shortcut | Description |
|---|---|---|
| Cycle Subtitles | `s` | Switch to next subtitle track |
| Toggle Subtitle Visibility | `shift+s` | Show/hide subtitles |
| Secondary Subtitle Track | `alt+s` | Cycle through secondary subtitle tracks |
| Toggle Secondary Subtitle | `alt+shift+s` | Show/hide secondary subtitles |
| Shift Subtitles Earlier | `ctrl+LEFT` | Shift subtitles earlier by 0.025s |
| Shift Subtitles Later | `ctrl+RIGHT` | Shift subtitles later by 0.025s |
| Reset Subtitle Timing | `ctrl+s` | Reset subtitle synchronization |
| Move Subtitles Up | `ctrl+UP` | Move subtitles higher on screen |
| Move Subtitles Down | `ctrl+DOWN` | Move subtitles lower on screen |
| Decrease Subtitle Size | `ctrl+-` | Make subtitles smaller |
| Increase Subtitle Size | `ctrl+=` | Make subtitles larger |
| Reset Subtitle Position/Size | `ctrl+0` | Reset subtitle scale and position to defaults |
| Cycle Subtitle Style Override | `k` | Cycle between subtitle style override modes |

## Audio Controls

| Action | Shortcut | Description |
|---|---|---|
| Cycle Audio Tracks | `a` | Switch to next available audio track |
| Advance Audio | `alt+LEFT` | Shift audio earlier by 0.100s |
| Delay Audio | `alt+RIGHT` | Shift audio later by 0.100s |
| Shift Balance Left | `alt+UP` | Shift audio balance toward left channel |
| Shift Balance Right | `alt+DOWN` | Shift audio balance toward right channel |
| Reset Audio Sync | `alt+a` | Reset audio delay to 0 |
| Reset Audio Balance | `alt+0` | Reset audio balance to center |

## Display & UI Controls

| Action | Shortcut | Description |
|---|---|---|
| Toggle Fullscreen | `f` | Switch between fullscreen and windowed mode |
| Show Playlist | `l` | Display the current playlist |
| Toggle Statistics | `i` | Show/hide playback statistics |
| Display Duration | `d` | Show total duration of current file |
| Display File Path | `u` | Show path of current media file |
| Cycle OSD Information | `o` | Cycle through OSD information levels |
| Toggle OSD Visibility | `shift+o` | Show/hide on-screen display |
| Toggle Console | `` ` `` | Show/hide console |
| Show Help | `F1` | Display essential shortcuts guide |

## Screenshot Controls

| Action | Shortcut | Description |
|---|---|---|
| Screenshot with Subtitles | `z` | Take screenshot including subtitles |
| Screenshot without Subtitles | `shift+z` | Take screenshot of video only |

## Video Appearance

| Action | Shortcut | Description |
|---|---|---|
| Cycle Aspect Ratio | `r` | Cycle through various aspect ratios |
| Rotate Video | `shift+r` | Rotate video 90/180/270/0 degrees |
| Toggle Video Scaling | `v` | Enable/disable video scaling |

## Video Adjustments

| Action | Shortcut | Description |
|---|---|---|
| Decrease Brightness | `ctrl+b` | Lower video brightness |
| Increase Brightness | `alt+b` | Raise video brightness |
| Decrease Contrast | `ctrl+c` | Lower video contrast |
| Increase Contrast | `alt+c` | Raise video contrast |
| Decrease Saturation | `ctrl+t` | Lower video saturation |
| Increase Saturation | `alt+t` | Raise video saturation |
| Zoom Out | `alt+-` | Reduce video zoom level |
| Zoom In | `alt+=` | Increase video zoom level |
| Reset Zoom | `alt+0` | Reset zoom to original size |
| Pan Left | `ctrl+alt+LEFT` | Pan video view left |
| Pan Right | `ctrl+alt+RIGHT` | Pan video view right |
| Pan Up | `ctrl+alt+UP` | Pan video view up |
| Pan Down | `ctrl+alt+DOWN` | Pan video view down |
| Reset Pan | `ctrl+alt+r` | Reset panning to center |

## Advanced Features

| Action | Shortcut | Description |
|---|---|---|
| Toggle Loop | `shift+l` | Enable/disable file looping |
| Set/Clear A-B Loop | `;` | Set loop start/end points |
| Toggle Deband Filter | `F2` | Enable/disable debanding |
| Cycle Simulcast Profiles | `F3` | Toggle simulcast-specific settings |
| Cycle Denoise Profiles | `F4` | Toggle noise reduction settings |
| Toggle Interpolation | `F5` | Enable/disable frame interpolation |
| Toggle Gamma Correction | `F6` | Fix QuickTime gamma issues |
| Cycle DRC Profiles | `F7` | Toggle dynamic range compression |
| Cycle Colorspace Profiles | `F8` | Switch between color space settings |
| Cycle Info Overlays | `F9` | Toggle technical information displays |
| Cycle Histogram Modes | `F10` | Switch between video analysis histograms |
| Shuffle Playlist | `w` | Randomize playlist order |
| Remove Current File | `shift+w` | Remove current file from playlist |
| Toggle Hardware Decoding | `h` | Switch between hardware/software decoding |
| Cycle Editions | `e` | Switch between different editions of media |
| Toggle Seeker | `g` | Show/hide interactive seeking UI |

---

This guide covers all keyboard shortcuts configured in the mpv player. Happy watching!