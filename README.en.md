# pyqt-clk

pyqt-clk is a PyQt-based desktop clock widget.

The widget has both analog and digital clocks, and stays on top of other windows.

## Requirements

- Python 3.x
- PyQt5
- Only tested on Windows10 + Anaconda environment

## Installation

Download, extract, and place qtclk.py to your favorite location.

## Usage

To start, run the command

`pythonw {path to qtclk.py}`

Double click anywhere on the widget to close.

## Known issue(s)

When started directly with pythonw.exe from Windows Explorer, the widget does not stay on top.

## To do

- Compatibility update to macOS and Linux
- JSON stylying capabilities

## Motivation

"Automatically hide the task bar" setting in Windows is useful for laptops where the screen size is limited,
but it is annoying to move your cursor or hit Windows key just to show the clock on the taskbar.

Although there exists plenty of third-party clock widgets that stays on top of other windows,
installation of such software are restricted in some (probably most) of private companies including where I belong for some obvious security reasons.

So I've decided to create one from scratch(*).

(*) Note that this repository is a separate version from the one that I use for work (since it is also restricted to distribute codes that I develop during work hours).