import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from pathlib import Path
from PIL import Image, ImageTk
import tkinter.font as tkfont

class SettingsWindow(tk.Toplevel):
    def __init__(self, master, apply_settings_callback):
        super().__init__(master)
        self.master = master

        self.title("Nastavení")
        self.geometry("300x450")
        self.apply_settings_callback = apply_settings_callback

        self.text_color = self.master.text_color
        self.bg_color = self.master.bg_color
        self.font_family = self.master.font_family

        self.font_size_var = tk.StringVar(value="Střední")
        tk.Label(self, text="Velikost písma:").pack(anchor="w", padx=10, pady=5)
        font_sizes = ["Malá", "Střední", "Velká"]
        self.font_size_menu = ttk.Combobox(self, textvariable=self.font_size_var, values=font_sizes, state="readonly")
        self.font_size_menu.pack(fill="x", padx=10)

        tk.Label(self, text="Styl písma:").pack(anchor="w", padx=10, pady=5)
        fonts = sorted(set(tkfont.families()))
        self.font_family_var = tk.StringVar(value=self.font_family)
        self.font_family_menu = ttk.Combobox(self, textvariable=self.font_family_var, values=fonts, state="readonly")
        self.font_family_menu.pack(fill="x", padx=10)

        tk.Label(self, text="Barva písma:").pack(anchor="w", padx=10, pady=5)
        self.text_color_btn = tk.Button(self, text="Vybrat barvu", command=self.pick_text_color)
        self.text_color_btn.pack(padx=10, pady=5)

        tk.Label(self, text="Barva pozadí:").pack(anchor="w", padx=10, pady=5)
        self.bg_color_btn = tk.Button(self, text="Vybrat barvu", command=self.pick_bg_color)
        self.bg_color_btn.pack(padx=10, pady=5)

        self.save_btn = tk.Button(self, text="Použít", command=self.apply_settings)
        self.save_btn.pack(pady=20)

    def pick_text_color(self):
        color = askcolor(title="Vyber barvu písma")[1]
        if color:
            self.text_color = color

    def pick_bg_color(self):
        color = askcolor(title="Vyber barvu pozadí")[1]
        if color:
            self.bg_color = color

    def apply_settings(self):
        size_map = {
            "Malá": 10,
            "Střední": 14,
            "Velká": 18
        }
        font_size = size_map.get(self.font_size_var.get(), 14)
        self.apply_settings_callback(font_size, self.text_color, self.bg_color)
        self.destroy()


class NewWindow(tk.Toplevel):
    def __init__(self, master, title="Nové okno"):
        super().__init__(master)
        self.title(title)
        self.geometry("300x200")
        tk.Label(self, text="Zatím prázdné okno").pack(expand=True, pady=20)


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

        # 1. Tlačítko
        tk.Button(
            button_frame,
            text="Otevřít okno 1",
            command=lambda: self.open_new_window("Okno 1")
        ).pack(side="left", padx=5)

        # 2. Tlačítko
        tk.Button(
            button_frame,
            text="Otevřít okno 2",
            command=lambda: self.open_new_window("Okno 2")
        ).pack(side="left", padx=5)

        # 3. Tlačítko
        tk.Button(
            button_frame,
            text="Otevřít okno 3",
            command=lambda: self.open_new_window("Okno 3")
        ).pack(side="left", padx=5)

        # 4. Tlačítko
        tk.Button(
            button_frame,
            text="Otevřít okno 4",
            command=lambda: self.open_new_window("Okno 4")
        ).pack(side="left", padx=5)



    def create_menu(self):
        image_path = Path("Images/Cogwheel-black.png")
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

        image_path = Path(
            "Images/Cogwheel-white.png"
            if not self.is_light_color(bg_color)
            else "Images/Cogwheel-black.png"
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
