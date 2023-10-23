#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import time
import tkinter
from typing import Generator

import pygame


def get_selected_text() -> str:
    selection = subprocess.check_output(['xclip', '-selection', 'primary', '-o'])
    return selection.decode('utf-8')


def display_text(text_generator: Generator[str, None, None]) -> None:
    root = tkinter.Tk()
    root.title("Modified Text")

    text_widget = tkinter.Text(root, wrap=tkinter.WORD)
    text_widget.pack(padx=10, pady=10, expand=True, fill=tkinter.BOTH)

    for text_chunk in text_generator:
        text_widget.insert(tkinter.END, text_chunk)

        root.update_idletasks()
        root.update()

    pygame.mixer.init()
    pygame.mixer.music.load('/usr/share/sounds/gnome/default/alerts/glass.ogg')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(.1)

    root.mainloop()


def main() -> None:
    """
    selected_text = get_selected_text()
    if not selected_text:
        return

    print(f"Selected text: {selected_text}")

    # result = respond(selected_text, model="gpt-4", temperature=.0)
    """

    def result_generator():
        yield "Hello"
        time.sleep(1)
        yield "World"
        time.sleep(1)
        yield "!"
        time.sleep(1)

    result = result_generator()

    display_text(result)


if __name__ == "__main__":
    main()
