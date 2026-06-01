# Posture Pet

Posture Pet is a cross-platform Python system tray app that uses a friendly pixel-art face to keep your posture timer visible all day. It stays green and happy while you are on track, then turns red and slumped when forty-five minutes pass without a stretch break.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python posture_pet.py
```

## Runtime Architecture

- `pystray` owns the system tray lifecycle and menu actions
- `Pillow` draws the tray icon programmatically so no image assets are needed
- A background daemon thread tracks a 45-minute countdown
- When the timer expires, the tray icon redraws as a sad red face
- Choosing `I Stretched!` resets the timer and restores the happy icon

## OS Requirements

- macOS, Windows, or Linux with a desktop tray environment
- Python 3.10 or newer recommended
- A system tray implementation that supports icon updates from a running process

## MIT License

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
