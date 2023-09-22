import tkinter as tk
import tkinter as ttk

root = tk.Tk()
root.geometry("1520x780")
root.title("Patient Identification and Monitoring")
root.configure(bg="gray")
general_overview = tk.Button(root, text="General Overview", font=("Helvetica", 32), bg="#D4DFB5")
general_overview.grid(row=0, column=0, padx=50, pady=50, sticky="nw")

camera_access = tk.Button(root, text="Camera Access", font=("Helvetica", 32), bg="#D4DFB5")
camera_access.grid(row=0, column=0, padx=1100, pady=50, sticky="se")


root.mainloop()
