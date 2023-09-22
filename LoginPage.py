import tkinter as tk
from tkinter import ttk, CENTER
from PIL import Image, ImageTk
from Components.CreateimageLabel import CreateImageLabel
from ConfigureGrid.ConfigureGrid import ConfigureGrid
from Components.CreateTitleLabel import CreateTitleLabel

def on_exit():
    main_window.quit()

def main():
    ConfigureMainWindowSettings(main_window, "Patient Identification and Monitoring", "1520x780", "gray")
    login_frame = CreateFrameAndAttachToMainWindow(main_window)
    PlaceFrameAtCenterBothHorizontallyAndVertically(login_frame)
    GroupWidgetsInsideLoginFrame(login_frame)
    menubar = tk.Menu(main_window)

    # Create a "File" menu and add items to it
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New", command=on_file_new)
    file_menu.add_command(label="Open", command=on_file_open)
    file_menu.add_command(label="Save", command=on_file_save)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=on_file_exit)

    # Create an "Edit" menu and add items to it
    option_menu = tk.Menu(menubar, tearoff=0)
    option_menu.add_command(label="Cut", command=on_edit_cut)
    option_menu.add_command(label="Copy", command=on_edit_copy)
    option_menu.add_command(label="Paste", command=on_edit_paste)
    tools_menu = tk.Menu(menubar, tearoff=0)
    tools_menu.add_command(label="New", command=on_file_new)
    # Add the menus to the menubar
    menubar.add_cascade(label="File", menu=file_menu)
    menubar.add_cascade(label="Option", menu=option_menu)
    menubar.add_cascade(label="Tools", menu=file_menu)

    # Configure the root window to use the menubar
    main_window.config(menu=menubar)
    main_window.resizable(False, False)
    main_window.mainloop()

def ConfigureMainWindowSettings(main_window, window_title, window_dimension="600x600", window_background_color="gray"):
    main_window.title(window_title)
    main_window.geometry(window_dimension)
    main_window.configure(bg=window_background_color)
    return main_window

def CreateFrameAndAttachToMainWindow(main_window):
    login_frame = tk.Frame(main_window)

    return login_frame

def PlaceFrameAtCenterBothHorizontallyAndVertically(frame):
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def GroupWidgetsInsideLoginFrame(login_frame):
    CreateTitleAndConfigureGrid(login_frame)
    # Creates Username Input Field + Icon
    create_entry_with_icon(login_frame, 1, 0, "Enter your username", "username_icon.png")
    password_entry = create_entry_with_icon(login_frame, 2, 0, "Enter your password", "password_icon.png")
    login_button = CreateButtonAndConfigureGrid(login_frame, button_text="Login", button_background_color="#DF7E7E", )

def CreateTitleAndConfigureGrid(frame, title_text="User Login", font=("Roboto", 25, 'bold'),
                                title_text_color="black"):
    title_label = CreateTitleLabel(frame, title_text, font)

    ConfigureGrid(title_label, 0, 1, 10)
    return title_label

def create_entry_with_icon(frame, row, column, default_text, icon_path, width=30):
    icon = LoadAndResizeIconImage(icon_path)

    label = CreateImageLabel(frame, icon)
    ConfigureGrid(label, row, column, 10)

    entry = ttk.Entry(frame, font=("Helvetica", 14), width=width, foreground="gray")
    entry.default_text = default_text
    entry.insert(0, default_text)
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focusout)
    entry.grid(row=row, column=column + 1, ipadx=10, ipady=15, pady=20)

    return entry

def validate_words(P):
    # Split the input text into words
    words = P.split()

    # Set the maximum number of words allowed
    max_words = 5  # Change this value to your desired limit

    # Check if the number of words exceeds the limit
    if len(words) > max_words:
        return False
    else:
        return True

def on_entry_click(event):
    entry = event.widget
    if entry.get() == entry.default_text:
        entry.delete(0, "end")

def on_focusout(event):
    entry = event.widget
    if not entry.get():
        entry.insert(0, entry.default_text)

def login():
    username = username_entry.get()
    password = password_entry.get()
    # Add your authentication logic here (for demonstration, just print the values)
    print("Username:", username)
    print("Password:", password)

def LoadAndResizeIconImage(path_of_icon, icon_size=(32, 32)):
    icon = Image.open(path_of_icon)
    icon = icon.resize(icon_size)
    icon = ImageTk.PhotoImage(icon)
    return icon
def InitializeMainWindow():
    return tk.Tk()
main_window = InitializeMainWindow()
# function for window settings
username_entry = ''
password_entry = ""
def on_file_new():
    print("File -> New clicked")
def on_file_open():
    print("File -> Open clicked")
def on_file_save():
    print("File -> Save clicked")
def on_file_exit():
    main_window.quit()
def on_edit_cut():
    print("Edit -> Cut clicked")
def on_edit_copy():
    print("Edit -> Copy clicked")
def on_edit_paste():
    print("Edit -> Paste clicked")
def CreateButtonAndConfigureGrid(frame, button_text="", button_background_color="",
                                 button_font=("Helvetica", 20, 'bold'), button_width=20, button_text_color="white"):
    widget = tk.Button(frame, text=button_text, bg=button_background_color, fg=button_text_color, width=button_width,
                       font=button_font)
    widget.grid(row=3, column=1, padx=20, pady=20)
    return widget
def quit_application(event):
    main_window.quit()
def toggle_fullscreen(event=None):
    # Toggle fullscreen mode
    state = not main_window.attributes('-fullscreen')
    main_window.attributes('-fullscreen', state)
# Bind the F11 key to toggle fullscreen mode
main_window.bind("<F11>", toggle_fullscreen)
main_window.bind("<Escape>", toggle_fullscreen)
toggle_fullscreen()
main_window.bind("q", quit_application)
exit_button = tk.Button(main_window, text="Exit",  command=on_exit, bg="#A01818", fg="white", width=150, height=2)
exit_button.pack(side="bottom", pady=15)
main()
