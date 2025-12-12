import tkinter as tk
from tkinter import ttk

# Basic Welcome Screen for Extraction Device

def main():
    root = tk.Tk()
    root.title("DNA DNA DNA AARay")
    root.attributes("-fullscreen", True)
    root.configure(bg="#1e1e1e")

    # Center Frame
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True)

    # Title Label
    title = tk.Label(frame, text="Welcome to DNA Extraction Device", 
                     font=("Arial", 36, "bold"), fg="white", bg="#1e1e1e")
    title.pack(pady=40)

    # Start Button
    start_btn = tk.Button(frame, text="START", font=("Arial", 28, "bold"), 
                          bg="#4CAF50", fg="white", padx=40, pady=20,
                          relief="raised", bd=5)
    start_btn.pack(pady=20)

    # Exit Button
    exit_btn = tk.Button(frame, text="EXIT", font=("Arial", 22), 
                         bg="#f44336", fg="white", padx=30, pady=15,
                         command=root.destroy)
    exit_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
