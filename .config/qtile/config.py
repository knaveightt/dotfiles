# -*- coding: utf-8 -*-
# -*- mode: python; python-indent-offset: 4 -*-
# Imports for the config
import os
import re
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, Rule, KeyChord
from libqtile.lazy import lazy

# starting defaults
mod = "mod4"
terminal = "st -z 18"

keys = [
      # Define the Basic Shortcuts
      Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
      Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
      Key([mod, "control"], "s", lazy.spawn(os.path.expanduser("~/.config/qtile/logoff.sh")), desc="Shutdown/Restart"),
      Key([mod, "control"], "x", lazy.spawn("xscreensaver-command -lock"), desc="Lock Screen w/ Xscreensaver"),
      Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
      Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
      Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen focused window"),
      Key([mod, "shift"], "q", lazy.spawn("xkill"), desc="Spawn xkill mode"),
      Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Spawn a command using a prompt widget"),

      # Basic Rofi Command Shortcuts
      Key([mod], "w", lazy.spawn("rofi -show window -theme dmenu-list"), desc="Launch Rofi in Window mode"),
      Key([mod], "r", lazy.spawn("rofi -show run -theme dmenu"), desc="Launch Rofi in Run mode"),
      Key([mod], "d", lazy.spawn("rofi -show drun -theme dmenu-list-ex -show-icons"), desc="Launch Rofi in Drun mode"),
      Key([mod], "e", lazy.spawn("st -z 18 -e ranger"), desc="Launch Ranger"),

      # "Extended" Command Shortcuts
      Key([mod, "shift"], "w", lazy.next_layout(), desc="Toggle between layouts"),
      Key([mod, "shift"], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
      #Key([mod, "shift"], "d", lazy.spawncmd(), desc="Spawn a custom script which launches apps with a preset configuration"),
      Key([mod, "shift"], "e", lazy.spawn("pcmanfm"), desc="Spawn the file manager"),

      # Quick Launch Applications
      KeyChord([mod], "a", [
          Key([], "f", lazy.spawn("firefox"), desc="Web Browser"),
          Key([], "r", lazy.spawn("st -z 18 -e ranger")),
          Key([], "e", lazy.spawn("emacsclient -c"))
      ]),

      # Toggle Scratchpad visibility
      Key([mod], "s", lazy.group['scratchpad'].dropdown_toggle('term'), desc="Toggle Terminal Scratchpad"),

      # Application / Utility / External Hot Keys
      Key([mod], "b", lazy.hide_show_bar()),
      Key([mod], "c", lazy.spawn(os.path.expanduser("~/Prog/go-chromecast/dmenu/go-chromecast-rofi")), desc="Google Chromecast Control"),
      Key([mod], "v", lazy.spawn("gscreenshot"), desc="Take a screenshot"),

      # Focus Movement
      Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
      Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
      Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
      Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
      Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

      # Window Movement
      Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
      Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
      Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
      Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

      # Change Window Sizing and Layout Functions
      Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
      Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
      Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
      Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
      Key([mod, "control"], "i", lazy.layout.shrink(), desc="Grow window up"),
      Key([mod, "control"], "o", lazy.layout.grow(), desc="Grow window up"),
      Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
      Key([mod, "control"], "b", lazy.layout.minimize(), desc="Reset all window sizes"),
      Key([mod, "control"], "m", lazy.layout.maximize(), desc="Maximize window"),
      Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
      Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
      Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),

      # Window Movement / Functions related to TreeTab layout
      Key([mod, "mod1"], "j", lazy.layout.move_down()),
      Key([mod, "mod1"], "k", lazy.layout.move_up()),
      Key([mod, "mod1"], "h", lazy.layout.move_left()),
      Key([mod, "mod1"], "l", lazy.layout.move_right()),
      Key([mod, "mod1"], "o", lazy.layout.expand_branch()),
      Key([mod, "mod1"], "i", lazy.layout.collapse_branch()),
      Key([mod, "mod1", "shift"], "j", lazy.layout.section_down()),
      Key([mod, "mod1", "shift"], "k", lazy.layout.section_up()),

      # Multimedia Keybindings
      Key([], "XF86AudioMute", lazy.spawn(os.path.expanduser("~/.config/dunst/changeVolume.sh mute"))),
      Key([], "XF86AudioLowerVolume", lazy.spawn(os.path.expanduser("~/.config/dunst/changeVolume.sh 5%-"))),
      Key([], "XF86AudioRaiseVolume", lazy.spawn(os.path.expanduser("~/.config/dunst/changeVolume.sh 5%+")))
  ]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

group_labels = [
    " ??? ",
    " ??? ",
    " ??? ",
    " ??? ",
    " ??? "
]
group_names = ["1", "2", "3", "4", "5"]

group_layouts = [
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "floating"
]

group_matches = [
    None,
    [Match(wm_class=["st-256color"])],
    [Match(wm_class=["firefox"])],
    [Match(wm_class=["pcmanfm", "Pcmanfm"])],
    None
]

group_exclusives = [
    False, False, False,
    False, False
]

group_persists = [
    True, True, True,
    True, True
]

group_inits = [
    True, True, True,
    True, True
]

groups = []

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            matches=group_matches[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            exclusive=group_exclusives[i],
            init=group_inits[i],
            persist=group_persists[i]
        ))

for i in groups:     
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], i.name, lazy.window.togroup(i.name))) # Send window to another group

groups.append( ScratchPad("scratchpad", [
    DropDown("term", "st", opacity=0.8)
    ]))

layout_theme = {
        "border_width": 2,
        "margin": 10,
        "border_focus": "d06d32",
        "border_normal": "888888"
        }

floating_theme = {
        "border_width": 2,
        "border_focus": "c44332",
        "border_normal": "888888"
        }

treetab_theme = {
        "bg_color": "131313",
        "inactive_bg": "212121",
        "inactive_fg": "bdbdbd",
        "active_bg": "333333",
        "active_fg": "d06d32",
        "font": "Inconsolata Nerd Font",
        "fontsize": 12,
        "sections": ['Workspace'],
        "section_fontsize": 14,
        "panel_width": 210
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme,border_focus_stack='#d75f5f'),
    layout.TreeTab(**treetab_theme),
    layout.Floating(**floating_theme)
]

# colors for panel theming
colors = [["#131313", "#131313"], # panel background
    ["#333333", "#333333"], # background for current selected group
    ["#d06d32", "#d06d32"], # font color for selected group active 
    ["#9f9f9f", "#d06d32"], # border line color for current tab
    ["#333333", "#333333"], # border line color for 'other tabs' and color for 'odd widgets'
    ["#555555", "#555555"], # color for the 'even widgets'
    ["#d06d32", "#d06d32"], # window name and line color
    ["#bdbdbd", "#bdbdbd"]] # font color for non-selected groups

# Default Widget settings
widget_defaults = dict(
    font='Inconsolata Nerd Font',
    fontsize=16,
    padding=3,
    backround=colors[2]
)
extension_defaults = widget_defaults.copy()

# Widget Definitions and Settings
def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[2],
            background = colors[0]
            ),
        widget.GroupBox (
            font = "Inconsolata Nerd Font",
            fontsize = 16,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 2,
            active = colors[2],
            inactive = colors [7],
            rounded = False,
            highlight_color = colors [1],
            highlight_method = "line",
            this_current_screen_border = colors[6],
            this_screen_border = colors [4],
            foreground = colors[2],
            background = colors[0]
            ),
        widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[2],
            background = colors[0]
            ),
        widget.Prompt(
            foreground = colors[6],
            background = colors[0],
            # prompt = "Run Command: "
            ),
        widget.WindowName(
            foreground = colors[6],
            background = colors[0],
            padding = 0
            ),
        widget.Sep (
            linewidth = 0,
            padding = 6,
            foreground = colors[0],
            background = colors[0]
            ),
        widget.TextBox (
            text= '???',
            foreground = colors[4],
            background = colors[0],
            padding = 0,
            fontsize = 26
            ),
        widget.TextBox (
            text = '???',    
            foreground = colors[6],
            background = colors[4],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + '-e ncmpcpp')}
            ),
        widget.Mpd2 (
            foreground = colors[6],
            background = colors[4],
            play_states = {'pause': '???', 'play': '???', 'stop': '???'}
            ),
        widget.TextBox (
            text= '???',
            foreground = colors[0],
            background = colors[4],
            padding = 0,
            fontsize = 26
            ),
        widget.TextBox(
            text = '???',
            foreground = colors[2],
            background = colors[0]
            ),
        widget.Volume (
            background = colors[0],
            foreground = colors[2],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')}
            ), 
        widget.TextBox (
            text= '???',
            foreground = colors[4],
            background = colors[0],
            padding = 0,
            fontsize = 26
            ),
        widget.TextBox (
            text = "??? ",
            background = colors[4],
            foreground = colors[2],
            padding = 0,
            fontsize = 14
            ),
        widget.Net ( # requires python-psutil package
            interface = "wlp10s0",
            format = '{down} ??? {up} ',
            foreground = colors[2],
            background = colors[4],
            padding = 1,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('nm-connection-editor')}
            ),
        widget.TextBox (
            text= '???',
            foreground = colors[0],
            background = colors[4],
            padding = 0,
            fontsize = 26
            ),
        widget.TextBox (
            text = " ??? ",
            foreground = colors[2],
            background = colors[0],
            padding = 0,
            fontsize = 14
            ),
        widget.Memory (
            foreground = colors[2],
            background = colors[0],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + 'e htop')},
            padding = 5
            ),
        widget.TextBox (
            text= '???',
            foreground = colors[4],
            background = colors[0],
            padding = 0,
            fontsize = 26
            ),
        widget.Clock (
            foreground = colors[2],
            background = colors[4],
            format = "%Y-%m-%d %H:%M (%A)"
            ),
        widget.CurrentLayoutIcon (
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = colors[0],
            background = colors[4],
            padding = 5
            ),
        widget.Systray(
                background = colors[4],
                padding = 0
            )
        ]
    return widgets_list

# Initialize Screens and Widgets
screens = [
    Screen(
        top=bar.Bar(widgets=init_widgets_list(), opacity=1.0, size=20)
    )
]

# Rules and Definitions
dgroups_key_binder = None
dgroups_app_rules = []  # type: List

main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_type='dock'), # cairo-dock
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
],
**floating_theme
)
auto_fullscreen = True
focus_on_window_activation = "focus"

def echo_notify(qtile):
    try:
        mb = qtile.widgets_map["prompt"]
        mb.start_input("Echo", notif, None)
    except:
        mb = None

def notif(args):
    qtile.cmd_spawn('dunstify "%s"' % args)

keys.append(Key([mod], "z", lazy.function(echo_notify)))

def new_section(args):
    qtile.current_layout.cmd_add_section(args)

def get_new_section(qtile):
    try:
        mb = qtile.widgets_map["prompt"]
        mb.start_input("Section", new_section, None)
    except:
        mb = None

keys.append(Key([mod, "mod1"], "t", lazy.function(get_new_section)))

def del_section(args):
    qtile.current_layout.cmd_del_section(args)

def get_remove_section(qtile):
    try:
        mb = qtile.widgets_map["prompt"]
        mb.start_input("Section", del_section, None)
    except:
        mb = None

keys.append(Key([mod, "mod1"], "r", lazy.function(get_remove_section)))

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
