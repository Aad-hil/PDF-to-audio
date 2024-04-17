import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text, output_file="output.mp3", lang="en"):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    return output_file

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def convert_pdf_to_speech():
    pdf_path = select_pdf_file()
    if pdf_path:
        text = pdf_to_text(pdf_path)
        output_file = text_to_speech(text)
        result_label.config(text=f"Text from PDF has been converted to speech and saved as {output_file}")

# GUI
root = tk.Tk()
root.title("PDF to Speech Converter")

select_file_button = tk.Button(root, text="Select PDF File", command=convert_pdf_to_speech)
select_file_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
