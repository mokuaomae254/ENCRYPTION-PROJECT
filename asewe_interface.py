"""
import tkinter as tk


def vigenere_cipher(text, key, mode):
    result = ""
    key_index = 0
    key = key.upper()
    for char in text:
        if char.isalpha():
            char_index = ord(char.upper()) - ord('A')
            key_shift = ord(key[key_index % len(key)]) - ord('A')
            if mode == 'encrypt':
                result += chr((char_index + key_shift) % 26 + ord('A'))
            elif mode == 'decrypt':
                result += chr((char_index - key_shift + 26) % 26 + ord('A'))
            key_index += 1
        else:
            result += char
    return result


class VigenereCipherGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Vigenère Cipher")
        self.geometry("500x500")

        tk.Label(self, text="Encrypt or Decrypt? (e/d):").pack()
        self.mode_entry = tk.Entry(self)
        self.mode_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_mode)
        self.submit_button.pack()

        self.back_button = tk.Button(self, text="Back", state='disabled', command=self.back)
        self.back_button.pack()

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack()

        self.result_label = tk.Label(self)
        self.result_label.pack()

    def submit_mode(self):
        mode = self.mode_entry.get().lower()
        if mode == 'e':
            mode = 'encrypt'
        elif mode == 'd':
            mode = 'decrypt'
        else:
            self.result_label.config(text="Invalid mode. Try again...")
            return

        tk.Label(self, text="Enter a message:").pack()
        self.message_entry = tk.Entry(self)
        self.message_entry.pack()

        tk.Label(self, text="Enter the key:").pack()
        self.key_entry = tk.Entry(self)
        self.key_entry.pack()

        self.result_box = tk.Text(self, height=10, width=50)
        self.result_box.pack()

        self.submit_button.config(text="Encrypt/Decrypt", command=lambda: self.submit_cipher(mode))
        self.back_button.config(state='normal')

    def submit_cipher(self, mode):
        message = self.message_entry.get()
        key = self.key_entry.get()
        result = vigenere_cipher(message, key, mode)
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, result)

    def back(self):
        self.message_entry.destroy()
        self.key_entry.destroy()
        self.result_box.destroy()
        self.mode_entry.delete(0, tk.END)
        self.submit_button.config(text="Submit", command=self.submit_mode)
        self.back_button.config(state='disabled')
        self.result_label.config(text="")


if __name__ == '__main__':
    app = VigenereCipherGUI()
    app.mainloop()
"""



import streamlit as st

def vigenere_cipher(text, key, mode):
    result = ""
    key_index = 0
    key = key.upper()
    for char in text:
        if char.isalpha():
            char_index = ord(char.upper()) - ord('A')
            key_shift = ord(key[key_index % len(key)]) - ord('A')
            if mode == 'encrypt':
                result += chr((char_index + key_shift) % 26 + ord('A'))
            elif mode == 'decrypt':
                result += chr((char_index - key_shift + 26) % 26 + ord('A'))
            key_index += 1
        else:
            result += char
    return result

def main():
    st.title("Vigenère Cipher")

    mode = st.selectbox("Encrypt or Decrypt?", options=['Encrypt', 'Decrypt'])
    if mode == 'Encrypt':
        mode = 'encrypt'
    elif mode == 'Decrypt':
        mode = 'decrypt'

    message = st.text_input("Enter a message:")
    key = st.text_input("Enter the key:")

    if st.button("Encrypt/Decrypt"):
        result = vigenere_cipher(message, key, mode)
        st.text_area("Result", value=result)

if __name__ == '__main__':
    main()
   


#streamlit run asewe_interface.py
#bitcoin address 3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5