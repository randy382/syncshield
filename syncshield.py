import os
import ctypes
from tkinter import Tk, filedialog, colorchooser, simpledialog, messagebox

class SyncShield:
    def __init__(self):
        self.theme = {
            "background": "#000000",
            "text_color": "#FFFFFF",
            "highlight_color": "#FF0000",
            "font_size": 12,
        }

    def set_background(self):
        Tk().withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(
            title="Select Background Image",
            filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")),
        )
        if file_path:
            try:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 0)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to set background: {e}")

    def set_colors(self):
        self.theme['background'] = colorchooser.askcolor(title="Choose Background Color")[1]
        self.theme['text_color'] = colorchooser.askcolor(title="Choose Text Color")[1]
        self.theme['highlight_color'] = colorchooser.askcolor(title="Choose Highlight Color")[1]

    def set_font_size(self):
        self.theme['font_size'] = simpledialog.askinteger("Input", "Enter Font Size:", minvalue=6, maxvalue=72)

    def apply_theme(self):
        try:
            # Placeholder for applying theme logic, as Windows theming involves system-level changes.
            # Normally, this would require significant integration with Windows' system APIs.
            messagebox.showinfo("Apply Theme", f"Background: {self.theme['background']}, "
                                               f"Text Color: {self.theme['text_color']}, "
                                               f"Highlight Color: {self.theme['highlight_color']}, "
                                               f"Font Size: {self.theme['font_size']}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply theme: {e}")

    def run(self):
        while True:
            action = simpledialog.askstring("SyncShield", "Choose action: (background, colors, font, apply, exit)")
            if action == "background":
                self.set_background()
            elif action == "colors":
                self.set_colors()
            elif action == "font":
                self.set_font_size()
            elif action == "apply":
                self.apply_theme()
            elif action == "exit":
                break
            else:
                messagebox.showwarning("Invalid Action", "Please choose a valid action.")

if __name__ == "__main__":
    app = SyncShield()
    app.run()