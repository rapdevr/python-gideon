import customtkinter as ck
import time
import threading
import gideonCore

ck.set_appearance_mode("System")
ck.set_default_color_theme("dark-blue")

class GideonUI(ck.CTk):
    def __init__(self):
        super().__init__()

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ck.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # text
        self.logo_label = ck.CTkLabel(self.sidebar_frame, text="Begin a conversation!", font=ck.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="n")
        # buttons
        self.sidebar_button_1 = ck.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Ask")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=(200,0), sticky="s")
        self.sidebar_button_2 = ck.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Quit")
        self.sidebar_button_2.grid(row=0, column=0, padx=20, pady=(120,0), sticky="s")
        # radio button
        self.sidebar_radiobutton_1 = ck.CTkRadioButton(self.sidebar_frame, state="disabled", hover=False, command=None, border_color="orange", text="Listening", text_color_disabled="white")
        self.sidebar_radiobutton_1.grid(row=0, column=0, pady=(20,0))


        # create textbox
        self.textbox = ck.CTkTextbox(self, width=40, height=285)
        self.textbox.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.textbox_2 = ck.CTkTextbox(self, width=40, height=10)
        self.textbox_2.grid(row=1, column=1, sticky="ew", padx=(20,20))
        
        self.update_radiobutton_color("orange") 

    def sidebar_button_event(self):
        self.destroy()

    def update_radiobutton_color(self, color):
        self.sidebar_radiobutton_1._border_color = color
        self.after(1000, self.update_radiobutton_color, gideonCore.radiobutton_color)  # Update every second

    def outbox_clear(self):
        self.textbox.insert("0.0", "Some example text!\n" * 50)

ui_instance = None  # Global variable to hold the UI instance

def start_ui_thread():
    global ui_instance

    ui = GideonUI()
    ui.title("GideonUI")
    ui.geometry(f"{600}x{400}")

    ui_instance = ui  # Store the UI instance in the global variable

    # Start the Tkinter main loop
    ui.mainloop()

def change_radiobutton_color(color):
    global ui_instance

    if ui_instance:
        ui_instance.after(0, ui_instance.update_radiobutton_color, color)

def get_ui_instance():
    return ui_instance  # Return the stored UI instance

if __name__ == "__main__":
    start_ui_thread()