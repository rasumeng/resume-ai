import customtkinter as ctk

# System theme detection - one line
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("BTF Resume")
app.geometry("500x600")

app.mainloop()