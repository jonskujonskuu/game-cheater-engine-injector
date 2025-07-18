import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import threading
import time

# Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Cheater Engine")
app.geometry("600x500")

# Global state
flashing = False
flashing_label = None

# Entry validators
def validate_entries(*args):
    if all([game_entry.get(), code_entry.get(), acc_entry.get(), pw_entry.get()]):
        enter_btn.configure(state="normal")
    else:
        enter_btn.configure(state="disabled")

# Flashing effect
def start_flashing():
    global flashing, flashing_label
    flashing = True

    flashing_label = ctk.CTkLabel(app, text="YOU JUST GOT HACKED", font=("Arial Black", 28), text_color="red")
    flashing_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def flash():
        colors = ["black", "red"]
        i = 0
        while flashing:
            app.configure(fg_color=colors[i % 2])
            flashing_label.configure(text_color=colors[(i + 1) % 2])
            i += 1
            time.sleep(0.2)

    threading.Thread(target=flash, daemon=True).start()

# Enter button action
def enter_pressed():
    messagebox.showinfo("Injecting...", f"Injecting {game_entry.get()}...\nUsing {code_entry.get()}...\nCode made!")
    messagebox.showinfo("Leak Alert", f"The account '{acc_entry.get()}' password got leaked HAHAHAHAAA!")
    output_text.insert("0.0", "GET HACKED! " * 10000)
    start_flashing()

# UI layout
game_entry = ctk.CTkEntry(app, placeholder_text="What game you wanna inject?", width=400)
game_entry.pack(pady=10)

code_entry = ctk.CTkEntry(app, placeholder_text="What is the game's code language?", width=400)
code_entry.pack(pady=10)

acc_entry = ctk.CTkEntry(app, placeholder_text="Please type account name", width=400)
acc_entry.pack(pady=10)

pw_entry = ctk.CTkEntry(app, placeholder_text="What is the account password?", width=400)
pw_entry.pack(pady=10)

# Validate on every change
for entry in [game_entry, code_entry, acc_entry, pw_entry]:
    entry.bind("<KeyRelease>", validate_entries)

enter_btn = ctk.CTkButton(app, text="ENTER", command=enter_pressed, state="disabled")
enter_btn.pack(pady=20)

output_text = ctk.CTkTextbox(app, height=80, width=500)
output_text.pack(pady=10)

# Run app
app.mainloop()
