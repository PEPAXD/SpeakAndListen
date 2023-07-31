import customtkinter
import speak_and_listen
# Main Window
class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window appearance
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")

        # configure window size
        self.geometry(f"{400}x{500}")
        self.resizable(False, False)

        # configure window title
        self.title("word-replacement 'By Mauro Pepa'")

        # create canvas
        self.frame = customtkinter.CTkFrame(self, corner_radius=30)
        self.frame.pack(fill="both", expand=True,  padx=20, pady=20)

        # TEXT-LABEL
        self.label = customtkinter.CTkLabel(self.frame, text="SPEAK AND LISTEN", font=("Arial Black", 22, "underline"))
        self.label.grid(row=0, column=1, padx=60, pady=15)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.frame, width=300, height=300, wrap='word')
        self.textbox.grid(row=1, column=1)

        # print loremText in textbox
        self.textbox.insert("0.0", "GRACIAS POR USAR SPEAK AND LISTEN\n\nCLICKEE EL SWITCH PARA CAMBIAR \nENTRE ESCUCHAR O HABLAR Y LUEGO \nOPRIMA EL BOTON PLAY PARA \nREPRODUCIR O GRABAR"+"\n\n")

        # create CTkSwitch
        self.switch = customtkinter.CTkSwitch(self.frame, text="Listen", command=self.switch_button)
        self.switch.select()
        self.switch.grid(row=2, column=1, padx=0, pady=15)

        # create Button play/stop
        self.button_playStop = customtkinter.CTkButton(self.frame, text="PLAY", width=300, command=self.startStop_recogning_button)
        self.button_playStop.grid(row=3, column=1, padx=0, pady=0)

        # copy text icon button
        self.copy_text_icon = customtkinter.CTkButton(self.frame, fg_color="transparent", corner_radius=0, border_width=2, text_color=("gray10", "#DCE4EE") ,text="COPY", width=50, command=self.copy_text_button)
        self.copy_text_icon.place(x=275, y=330)

    def switch_button(self):
        if self.switch.get() == 1:
            self.switch.configure(text="Listen")
            self.copy_text_icon.configure(text="COPY")

        else:
            self.switch.configure(text="Speak")
            self.copy_text_icon.configure(text="SAVE")

    def startStop_recogning_button(self):

        if self.switch.get() == 1:
            # Check the current text of the button
            current_text = self.button_playStop.cget("text")

            if current_text == "PLAY":
                self.button_playStop.configure(text="GRABANDO")
                self.button_playStop.configure(hover_color="darkred", fg_color="red")

                # disable the switch and texboxt
                self.switch.configure(state="disabled")
                self.textbox.configure(state="disabled")

                # Update the interface to apply the color change
                self.update()

                # Call Speak_and_Listen.hear_me()
                hearText = speak_and_listen.hear_me()

                # enable the switch and texboxt#
                self.switch.configure(state="normal")
                self.textbox.configure(state="normal")

                if hearText != "":
                    # erase the text in the textbox
                    self.textbox.delete("0.0", "end")
                    self.textbox.insert("0.0", hearText)
                    self.button_playStop.configure(text="PLAY")
                    self.button_playStop.configure(hover_color="#106a43", fg_color="#2fa572")
                else:
                    self.textbox.delete("0.0", "end")
                    self.textbox.insert("0.0", "NO SE RECONOCIO EL TEXTO, HABLE LENTO Y CLARO")
                    self.button_playStop.configure(text="PLAY")
                    self.button_playStop.configure(hover_color="#106a43", fg_color="#2fa572")

        else:
            #copy tex in textbox in a variable
            text_to_copy = self.textbox.get("0.0", "end")
            speak_and_listen.say_me(text_to_copy)


    def copy_text_button(self):

        if self.switch.get() == 1:
            #copy text for textbox in clipboard
            self.textbox.clipboard_clear()
            self.textbox.clipboard_append(self.textbox.get("0.0", "end"))
            self.textbox.event_generate("<<Copy>>")
            self.textbox.focus()

        else:
            text_to_copy = self.textbox.get("0.0", "end")
            speak_and_listen.save_mp3(text_to_copy)

def main():
    app = App()
    app.mainloop()