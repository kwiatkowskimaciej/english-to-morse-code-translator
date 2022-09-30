from tkinter.ttk import Style
from morse_code_dict import MORSE_CODE_DICTIONARY
from tkinter import *


def encrypt():
    encrypted_message = ''
    message = message_entry.get("1.0", 'end-1c')

    for char in message.lower():
        if char == ' ':
            encrypted_message += ' '
        else:
            encrypted_message += MORSE_CODE_DICTIONARY[char] + ' '

    cipher_entry.delete("1.0", 'end')
    cipher_entry.insert(INSERT, encrypted_message)


def decrypt():
    decrypted_message = ''
    encrypted_message = cipher_entry.get("1.0", 'end-1c')
    char_codes = encrypted_message.split(' ')
    inv_morse_code_dict = {code: char for char, code in MORSE_CODE_DICTIONARY.items()}

    for char_code in char_codes:
        if char_code == '':
            decrypted_message += ' '
        else:
            decrypted_message += inv_morse_code_dict[char_code]

    message_entry.delete("1.0", 'end')
    message_entry.insert(INSERT, decrypted_message)


root = Tk()
root.title('English to Morse Code Translator')
root.config(padx=50, pady=50)
root.resizable(False, False)

message_label = Label(text="English", font=("Inter", 20))
message_label.grid(sticky='W', column=0, row=0, pady=(0, 16))

message_entry = Text(width=70, height=10, font=("Inter", 16))
message_entry.grid(column=0, row=1, columnspan=3)

msg_translate_button = Button(text="Translate", bg='blue', command=encrypt)
msg_translate_button.grid(column=2, row=2, sticky='NE')

cipher_label = Label(text="Morse", font=("Inter", 20))
cipher_label.grid(sticky='W', column=0, row=3, pady=(48, 16))

cipher_entry = Text(width=70, height=10, font=("Inter", 16))
cipher_entry.grid(column=0, row=4, columnspan=3)

cph_translate_button = Button(text="Translate", command=decrypt)
cph_translate_button.grid(column=2, row=5, sticky='NE')

root.mainloop()
