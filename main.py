import tkinter as tk
import os
from tkinter import filedialog, messagebox
from deep_translator import GoogleTranslator


AVAILABLE_LANGUAGES = GoogleTranslator().get_supported_languages()

def translate_file(file_path, target_language, output_folder):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if not lines:
            messagebox.showerror("Error", "File is empty or cannot be read.")
            return

        translated_lines = [GoogleTranslator(source='auto', target=f'{target_language}').translate(line) for line in lines]

        output_file_path = os.path.join(output_folder, f"translated_{os.path.basename(file_path)}")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for translated_line in translated_lines:
                if translated_line is not None:
                    output_file.write(translated_line + '\n')

        messagebox.showinfo("Success", f"File translated and saved to {output_file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def browse_file():
    filename = filedialog.askopenfilename()
    if filename:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, filename)


def browse_folder():
    foldername = filedialog.askdirectory()
    if foldername:
        entry_output_folder.delete(0, tk.END)
        entry_output_folder.insert(0, foldername)


def translate():
    file_path = entry_file_path.get()
    target_language = selected_language.get()
    output_folder = entry_output_folder.get()

    if not file_path or not target_language or not output_folder:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    translate_file(file_path, target_language, output_folder)

root = tk.Tk()
root.title("File Translator")

root.configure(bg='black')

# style = tk.Style()
# style.configure('TLabel', foreground='white', background='black')
# style.configure('TButton', foreground='black', background='white')
# style.configure('TEntry', foreground='black', background='white')

selected_language = tk.StringVar(root)
selected_language.set(AVAILABLE_LANGUAGES[0])  
language_menu = tk.OptionMenu(root, selected_language, *AVAILABLE_LANGUAGES)
language_menu.grid(row=1, column=1, padx=10, pady=5)


label_file_path = tk.Label(root, text="File Path:")
label_file_path.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_file_path = tk.Entry(root, width=50)
entry_file_path.grid(row=0, column=1, padx=10, pady=5)
button_browse_file = tk.Button(root, text="Browse", command=browse_file)
button_browse_file.grid(row=0, column=2, padx=5, pady=5)

label_target_language = tk.Label(root, text="Target Language:")
label_target_language.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
# entry_target_language = tk.Entry(root, width=20)
# entry_target_language.grid(row=1, column=1, padx=10, pady=5)

label_output_folder = tk.Label(root, text="Output Folder:")
label_output_folder.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_output_folder = tk.Entry(root, width=50)
entry_output_folder.grid(row=2, column=1, padx=10, pady=5)
button_browse_folder = tk.Button(root, text="Browse", command=browse_folder)
button_browse_folder.grid(row=2, column=2, padx=5, pady=5)

button_translate = tk.Button(root, text="Translate", command=translate)
button_translate.grid(row=3, column=1, pady=10)

root.mainloop()