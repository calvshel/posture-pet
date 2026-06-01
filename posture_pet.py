#!/usr/bin/env python3
"""A tiny tray app that reminds you to stand up before your spine files a complaint."""

from __future__ import annotations

import threading
import time
from argparse import ArgumentParser
from pathlib import Path

import pystray
from PIL import Image, ImageDraw

TIMER_SECONDS = 45 * 60
ICON_SIZE = 64


def make_icon(happy: bool) -> Image.Image:
    face = Image.new("RGBA", (ICON_SIZE, ICON_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(face)
    bg = (34, 197, 94, 255) if happy else (239, 68, 68, 255)
    eye = (15, 23, 42, 255)
    mouth = eye

    draw.rounded_rectangle((6, 6, 58, 58), radius=14, fill=bg)
    draw.ellipse((20, 22, 27, 29), fill=eye)
    draw.ellipse((37, 22, 44, 29), fill=eye)
    if happy:
        draw.arc((19, 26, 45, 47), start=10, end=170, fill=mouth, width=4)
    else:
        draw.arc((19, 33, 45, 54), start=190, end=350, fill=mouth, width=4)
        draw.line((24, 46, 40, 46), fill=mouth, width=3)
    return face


def parse_args(argv: list[str] | None = None):
    parser = ArgumentParser(description="Run a tray posture reminder with a pixel-art status icon.")
    parser.add_argument("--minutes", type=float, default=45, help="stretch reminder interval in minutes (default: 45)")
    parser.add_argument("--preview-icons", action="store_true", help="write a local posture_pet_preview.png and exit")
    return parser.parse_args(argv)


def interval_seconds(minutes: float) -> int:
    seconds = int(round(minutes * 60))
    if seconds <= 0:
        raise ValueError("--minutes must be greater than 0")
    return seconds


def save_preview(path: str = "posture_pet_preview.png") -> Path:
    canvas = Image.new("RGBA", (152, 80), (255, 255, 255, 0))
    canvas.alpha_composite(make_icon(True), (8, 8))
    canvas.alpha_composite(make_icon(False), (80, 8))
    output = Path(path)
    canvas.save(output)
    return output


class PosturePet:
    def __init__(self, timer_seconds: int = TIMER_SECONDS) -> None:
        self._lock = threading.Lock()
        self._stop_event = threading.Event()
        self._timer_seconds = timer_seconds
        self._deadline = time.monotonic() + self._timer_seconds
        self._alerted = False
        self.icon = pystray.Icon(
            "posture-pet",
            make_icon(True),
            "Posture Pet",
            menu=pystray.Menu(
                pystray.MenuItem("I Stretched!", self.on_stretched),
                pystray.MenuItem("Quit", self.on_quit),
            ),
        )
        self._timer_thread = threading.Thread(target=self._watch_timer, daemon=True)

    def start(self) -> None:
        self._timer_thread.start()
        self.icon.run()

    def _watch_timer(self) -> None:
        while not self._stop_event.is_set():
            with self._lock:
                expired = time.monotonic() >= self._deadline
                if expired and not self._alerted:
                    self._alerted = True
                    self.icon.icon = make_icon(False)
                    self.icon.title = "Posture Pet - stretch now"
                elif not expired and self._alerted:
                    self.icon.icon = make_icon(True)
                    self.icon.title = "Posture Pet"
                    self._alerted = False
            time.sleep(1)

    def reset_timer(self) -> None:
        with self._lock:
            self._deadline = time.monotonic() + self._timer_seconds
            self._alerted = False
            self.icon.icon = make_icon(True)
            self.icon.title = "Posture Pet"

    def on_stretched(self, icon, item) -> None:
        self.reset_timer()

    def on_quit(self, icon, item) -> None:
        self._stop_event.set()
        icon.stop()


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    if args.preview_icons:
        save_preview()
        return
    try:
        timer_seconds = interval_seconds(args.minutes)
    except ValueError as error:
        raise SystemExit(str(error)) from error
    PosturePet(timer_seconds=timer_seconds).start()


if __name__ == "__main__":
    main()
