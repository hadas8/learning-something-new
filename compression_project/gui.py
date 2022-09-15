import tkinter as tk
from compress_module import compress, decompress
from tkinter import filedialog

def compression(i, o):
    compress(i, o)

def decompression(i, o):
    decompress(i, o)

def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title="Select input file")
    return filename


window = tk.Tk()
window.title("Compression engine")
window.geometry("600x400")

"""
input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
input_label = tk.Label(window, text="Input file: ")
output_label = tk.Label(window, text="Output file: ")
"""


compress_button = tk.Button(window, text="Compress", command=lambda: compression(open_file(), 'compressed_outputfile.txt'))
decompress_button = tk.Button(window, text="Decompress", command=lambda: decompression(open_file(), 'decompressed_outputfile.txt'))
"""
input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
output_label.grid(row=1, column=0)
output_entry.grid(row=1, column=1)
"""

compress_button.grid(row=2, column=1)
decompress_button.grid(row=3, column=1)


window.mainloop()