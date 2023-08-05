# -*- coding: utf-8 -*-
from libqtile.dgroups import simple_key_binder
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import backlight
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal
from typing import List  # noqa: F401

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration


mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "firefox"     # My browser of choice
fileExplorer = "caja"       #My file manager of choice
reboot = "reboot"         # Reboot command
shutdown = "shutdown now"  # Shutdown command
wallpaper = "/home/bibek/pictures/Wallpaper/best"
# myConfig = "~/.config/qtile/config.py" # The Qtile config file location

def go_to_layout(qtile, index):
    qtile.current_group.use_layout(index)

keys = [
    # The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal'
        ),
    Key([mod, "shift"], "Return",
        lazy.spawn("rofi -show drun"),
        desc='Run Launcher'
        ),
    Key([mod], "b",
        lazy.spawn(myBrowser),
        desc='Firefox Browser'
        ),
    Key([mod], "c",
        lazy.spawn("code"),
        desc='VS Code'
        ),
    Key([mod], "v",
        lazy.spawn(myTerm + " -e nvim  /home/bibek/.config/qtile/config.py"),
        desc='NeoVim'
        ),
    Key([mod], "e",
        lazy.spawn(fileExplorer),
        desc="File Manager"
        ),

    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
        ),
    Key([mod, "shift"], "c",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod, "shift"], "r",
        lazy.spawn(reboot),
        desc='Restart Device'
        ),
    Key(["control", "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "s",
        lazy.spawn(shutdown),
        desc='Shutdown'
        ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Restart Qtile'
        ),
    Key(
        [mod], "s",
        # run scrot to take a screenshot
        # name the file in format year-month-day-hour-minute-second.png
        # save it to ~/Pictures/Screenshots
        # name of screenshot is the name of current window
        lazy.spawn("scrot -s /home/bibek/Pictures/Screenshots/Picture'%H%M%S.png'"),
        desc='Take a screenshot'

    ),
    Key(
        [mod], "d",
         lazy.spawn("scrot /home/bibek/Pictures/Screenshots/Picture'%H%M%S.png'"),
        desc='Take a screenshot'
    ),
    # Switch focus to specific monitor (out of three)
    Key([mod], "w",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "e",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),
    Key([mod], "r",
        lazy.to_screen(2),
        desc='Keyboard focus to monitor 3'
        ),
    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
    # Treetab controls
    Key([mod, "shift"], "h",
        lazy.layout.move_left(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "shift"], "l",
        lazy.layout.move_right(),
        desc='Move down a section in treetab'
        ),
    # Window controls
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    # switch to monadtall layout
    Key([mod, "shift"], "m",
        lazy.function(go_to_layout, 2),
        desc='switch to spiral layout'
    ),
    # Stack controls
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([mod, "shift"], "space",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),

    # key for volume
    Key([], "XF86AudioRaiseVolume", lazy.widget["volume"].increase_vol()),
    Key([], "XF86AudioLowerVolume", lazy.widget["volume"].decrease_vol()),
    # key for brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
]

# workspaces = [
#     {"name": " ",  "matches": [Match(wm_class=["caja"])]},
#     {"name": " ",  "matches": [Match(wm_class=["Alacritty"])]},
#     {"name": " ",  "matches": [Match(wm_class=[""])]},
#     {"name": "󰨞 ",  "matches": [Match(wm_class=["Visual Studio Code"])]},
#     {"name": " ",  "matches": [Match(wm_class=["Discord"])]},
#     {"name": "󰕼 ",  "matches": [Match(wm_class=["VLC media player"])]},
#     {"name": " ",  "matches": [Match(wm_class=["Firefox"])]},
# ]

# groups = [Group(**kwargs) for kwargs in workspaces]

# normal workspaces
groups = [Group(_name) for _name in [" ", " ", " ", "󰨞 ", " ", "󰕼 ", "󰭹 "]]
# how to escape this rule
# https://docs.qtile.org/en/stable/manual/config/groups.html

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    # layout.MonadWide(**layout_theme),
    layout.Spiral(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font="Ubuntu Bold",
        fontsize=15,
        sections=["FIRST", "SECOND"],
        section_fontsize=10,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200
    ),
    layout.Floating(**layout_theme)
]

# colors = [["#292d3e", "#292d3e"],  # panel background
#           # background for current screen tab
#           ["#434758", "#434758"],
#           ["#ffffff", "#ffffff"],  # font color for group names
#           # border line color for current tab
#           ["#bc13fe", "#bc13fe"],  # Group down color
#           # border line color for other tab and odd widgets
#           ["#8d62a9", "#8d62a9"],
#           ["#668bd7", "#668bd7"],  # color for the even widgets
#           ["#e1acff", "#e1acff"],  # window name

#           ["#000000", "#000000"],
#           ["#AD343E", "#AD343E"],
#           ["#f76e5c", "#f76e5c"],
#           ["#F39C12", "#F39C12"],
#           ["#F7DC6F", "#F7DC6F"],
#           ["#f1ffff", "#f1ffff"],
#           ["#4c566a", "#4c566a"], ]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"],
          ["#AD343E", "#AD343E"],
          ]

prompt = "{0}".format(socket.gethostname().split('.')[0])

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=10,
    padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():

    widgets_list = [

        # display a text for hostname
        # widget.TextBox(
        #     text=" ",
        #     foreground=colors[2],
        #     background=colors[0],
        #     fontsize=13,
        #     margin_y=3,
        #     margin_x=1,
        #     padding_y=5,
        #     padding_x=3,
        #     borderwidth=3,
        # ),
        # widget.TextBox(
        #     text=prompt,
        #     foreground=colors[2],
        #     background=colors[0],
        #     fontsize=15,
        #     margin_y=3,
        #     margin_x=1,
        #     padding_y=5,
        #     padding_x=3,
        #     borderwidth=3,
        # ),

        widget.GroupBox(
            font="Fira Code Nerd Font",
            fontsize=15,
            margin_y=3,
            margin_x=1,
            padding_y=5,
            padding_x=3,
            borderwidth=3,

            active=colors[2],
            inactive=colors[7],
            rounded=True,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0],

        ),

        widget.CurrentLayout(
            foreground=colors[6],
            background=colors[0],
            padding=2,
            format='({name})'
        ),

        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=2,
            format = '[{name}]'
        ),


        widget.Systray(
            background=colors[0],
            padding=3,
            icon_size=12,

        ),
        #widget.Wallpaper(
        #    directory=wallpaper,
        #    random_selection=True,
        #    foreground=colors[6],
        #    background=colors[0],
        #    label=' 󰸉 ',
        #    fontsize=12,
        #    padding=2,
        #),

        # widget.Net(
        #     interface="wlan0",

        #     format='Net: {down} {up}',
        #     foreground=colors[7],
        #     background=colors[0],
        #     padding=2
        # ),

        widget.Backlight(
            foreground=colors[7],
            background=colors[0],
            backlight_name='intel_backlight',
            brightness_file='brightness',
            max_brightness_file='max_brightness',
            # fmt='[Br.] {}',
            font="Jet Brains Mono Nerd Font",
            fontsize=12,
            fmt='󰃠 {}',
            step=5,
            padding=5,
            mouse_callbacks={
                'Button4': lambda: qtile.cmd_spawn('brightnessctl set +5%'),
                'Button5': lambda: qtile.cmd_spawn('brightnessctl set 5%-'),
            },
                            
        ),

        widget.Volume(
            foreground=colors[7],
            background=colors[0],
            # fmt='[V] {}',
            fmt='󰕾 {}',
            font="Jet Brains Mono Nerd Font",
            fontsize=12,
            padding=2,

        ),

        widget.Battery(
            foreground=colors[7],
            background=colors[0],
            format='{char}{percent:2.0%}',
            font="Jet Brains Mono Nerd Font",
            fontsize=12,
            charge_char='󱐋',
            full_char='󰂄',
            discharge_char='󱊣 ',
            show_short_text=True,
            notify_below=40,
            low_percentage=40,
            update_interval=15,
            low_foreground=colors[9],
            padding=2
        ),

        widget.Clock(
            foreground=colors[7],
            background=colors[0],
            format="%a, %b %d[%H:%M]"
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # Slicing removes unwanted widgets (systray) on Monitors 1,3
    del widgets_screen1[9:10]
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    # Monitor 2 will display all widgets in widgets_list
    return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
    Match(title='BiblioCrypt'),  # BiblioCrypt Window
    Match(title='Test'),  # Test window
    Match(title='ImGUI'),  # ImGUI window
    Match(title='matplot'),
    Match(title='matplotlib'),
    Match(title='test'),
    Match(title='py'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@ hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
