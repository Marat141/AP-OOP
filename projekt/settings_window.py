 # Okno s nastavením (třída SettingsWindow)

import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
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