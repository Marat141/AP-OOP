# main.py
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
from settings_window import SettingsWindow
from new_window import NewWindow
from turtle_drawings import draw_sun_1, draw_sun_2, draw_sun_3, draw_snowman
from pathlib import Path
from tkinter import messagebox

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Moje Aplikace")
        self.geometry("800x600")
        self.minsize(400, 300)

        self.default_font_size = 14
        self.text_color = "#000000"
        self.bg_color = "#ffffff"
        self.font_family = "Arial"

        self.configure(bg=self.bg_color)

        self.create_widgets()
        self.create_menu()

        self.bind("<Configure>", self.on_resize)

    def is_light_color(self, hex_color):
        r, g, b = tuple(int(hex_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        return brightness > 128

    def create_widgets(self):
        self.label = tk.Label(
            self,
            text="Vítej v aplikaci!",
            font=(self.font_family, self.default_font_size),
            fg=self.text_color,
            bg=self.bg_color
        )
        self.label.pack(pady=20)

        # --- Kontejner pro tlačítka vedle sebe ---
        button_frame = tk.Frame(self, bg=self.bg_color)
        button_frame.pack(pady=10)

        # Tlačítka pro otevření oken
        for i in range(1, 5):
            tk.Button(
                button_frame,
                text=f"Otevřít okno {i}",
                command=lambda i=i: self.open_new_window(f"Okno {i}")
            ).pack(side="left", padx=5)

    def create_menu(self):
        image_path = IMAGE_DIR / "Cogwheel-black.png"
        if not image_path.exists():
            messagebox.showerror("Chyba", f"Obrázek nebyl nalezen:\n{image_path}")
            return
        original_image = Image.open(image_path)

        try:
            resample = Image.Resampling.LANCZOS
        except AttributeError:
            resample = Image.ANTIALIAS

        resized_image = original_image.resize((24, 24), resample)
        self.settings_icon = ImageTk.PhotoImage(resized_image)

        self.settings_button = tk.Button(
            self,
            image=self.settings_icon,
            command=self.open_settings,
            borderwidth=1,
            relief="solid",
            bg="#f0f0f0",
            activebackground="#e0e0e0",
            highlightthickness=1
        )
        self.settings_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    def on_resize(self, event):
        self.settings_button.place_configure(relx=1.0, rely=0.0, x=-10, y=10)

    def open_settings(self):
        settings_window = SettingsWindow(self, self.apply_settings)
        settings_window.grab_set()
        self.wait_window(settings_window)

    def open_new_window(self, title="Nové okno"):
        new_window = NewWindow(self, title=title)
        new_window.grab_set()
        self.wait_window(new_window)

    def apply_settings(self, font_size, text_color, bg_color):
        self.default_font_size = font_size
        self.text_color = text_color
        self.bg_color = bg_color

        self.configure(bg=self.bg_color)
        self.label.config(
            font=(self.font_family, self.default_font_size),
            fg=self.text_color,
            bg=self.bg_color
        )

        image_path = IMAGE_DIR / "Cogwheel-black.png"


        image_path = Path(
            "/images/Cogwheel-white.png"
            if not self.is_light_color(bg_color)
            else IMAGE_DIR / "Cogwheel-black.png"
        )
        original_image = Image.open(image_path)
        resized_image = original_image.resize((24, 24), Image.Resampling.LANCZOS)
        self.settings_icon = ImageTk.PhotoImage(resized_image)

        self.settings_button.config(
            image=self.settings_icon,
            bg=self.bg_color,
            activebackground=self.bg_color
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
