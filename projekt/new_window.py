# Třída NewWindow a logika pro podokna

import tkinter as tk
from turtle_drawings import draw_sun_1, draw_sun_2, draw_sun_3, draw_snowman

class NewWindow(tk.Toplevel):
    def __init__(self, master, title="Nové okno"):
        super().__init__(master)
        self.title(title)
        self.geometry("300x200")
        self.resizable(False, False)

        tk.Label(self, text="Zatím prázdné okno").pack(pady=10)

        # Pokud je to "Okno 1", přidáme další tlačítka
        if title == "Okno 1":
            self.create_sun_snow_buttons()

    def create_sun_snow_buttons(self):
        btn_frame = tk.Frame(self, bg="white")
        btn_frame.pack(pady=10)

        button_style = {
            "width": 12,
            "height": 2,
            "font": ("Helvetica", 12, "bold"),
            "relief": "raised",
            "bd": 2,
            "cursor": "hand2"
        }

        sun_btn = tk.Button(
            btn_frame,
            text="☀️ Sluníčko",
            bg="#FFD700",        # zlatá
            fg="black",
            command=self.open_sun_choice_window,
            **button_style
        )
        sun_btn.pack(side="left", padx=10)

        snow_btn = tk.Button(
            btn_frame,
            text="☃️ Sněhulák",
            bg="#4A90E2",        # modrá
            fg="white",
            activebackground="#357ABD",
            command=self.draw_snowman_and_close,
            **button_style
        )
        snow_btn.pack(side="left", padx=10)


    def draw_snowman_and_close(self):
        self.withdraw()  # schová aktuální okno
        draw_snowman()
        self.deiconify()  # ukáže zpět

    def open_sun_choice_window(self):
        self.withdraw()

        sun_window = tk.Toplevel(self)
        sun_window.title("Výběr sluníčka")
        sun_window.geometry("250x200")
        sun_window.resizable(False, False)

        def on_draw_sun(sun_index):
            sun_window.withdraw()
            if sun_index == 1:
                draw_sun_1()
            elif sun_index == 2:
                draw_sun_2()
            elif sun_index == 3:
                draw_sun_3()
            sun_window.deiconify()

        for i in range(1, 4):
            tk.Button(
                sun_window,
                text=f"Sluníčko {i}",
                command=lambda i=i: on_draw_sun(i)
            ).pack(pady=5)

        def on_close(event=None):
            sun_window.destroy()
            self.deiconify()

        sun_window.bind("<Return>", on_close)

        ok_button = tk.Button(sun_window, text="OK", command=on_close)
        ok_button.pack(pady=10)
