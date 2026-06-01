# Posture Pet

A tiny cross-platform tray companion that turns sad when you have been sitting too long.

Posture Pet lives in your system tray with a happy green pixel face. Every 45 minutes, it flips into a sad red slouch reminder until you choose `I Stretched!` from the tray menu. The icon is drawn entirely in Python, so the app ships without image assets.

## Features

- Cross-platform tray app powered by `pystray`
- Programmatic pixel-style icons drawn with `Pillow`
- Happy green default state and sad red reminder state
- Background timer thread with a 45-minute stretch interval
- Tray menu action to reset the timer after stretching
- Clean quit action from the tray menu
- No bundled image files or external services

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\activate
```

## Run

```bash
python posture_pet.py
```

Once running, use the tray menu to reset the timer or quit the app.

## Runtime Architecture

Posture Pet keeps the application deliberately small:

- `pystray.Icon` owns the tray icon, title, and menu lifecycle
- `PIL.ImageDraw` generates the happy and sad icons at runtime
- A daemon thread checks the stretch deadline once per second
- `threading.Lock` protects shared timer and alert state
- `threading.Event` stops the timer loop cleanly when the app quits

## OS Requirements

- Python 3.10 or newer recommended
- macOS, Windows, or Linux with a desktop tray environment
- Linux users may need AppIndicator or a compatible system tray package installed by their desktop environment

## Development

Run a syntax check with:

```bash
python3 -m py_compile posture_pet.py
```

The app has no asset pipeline. Change the icon drawing in `make_icon()` and restart the app to test new states.

## Roadmap

- Configurable reminder interval
- Optional desktop notification when the timer expires
- Pause mode for meetings or screen sharing
- Lightweight session history

## License

MIT License

Copyright (c) 2026 Calvin Shelwell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
