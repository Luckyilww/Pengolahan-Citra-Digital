import tkinter as tk
from tkinter import messagebox


def rle_compress(text):
    compressed = ''
    count = 1
    n = len(text)

    if n == 0:
        return ''

    for i in range(1, n):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    compressed += text[n - 1] + str(count)
    return compressed


def compress_text():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Peringatan", "Mohon masukkan teks yang akan dikompresi.")
        return

    compressed_text = rle_compress(text)
    compressed_entry.delete("1.0", tk.END)
    compressed_entry.insert(tk.END, compressed_text)


def clear_text():
    text_entry.delete("1.0", tk.END)
    compressed_entry.delete("1.0", tk.END)


window = tk.Tk()
window.title("Kompresi Teks RLE")

# Label dan Text Entry untuk masukan teks
text_label = tk.Label(window, text="Masukkan teks:")
text_label.pack()

text_entry = tk.Text(window, height=5)
text_entry.pack()

# Tombol Kompresi
compress_button = tk.Button(window, text="Kompresi", command=compress_text)
compress_button.pack()

# Label dan Text Entry untuk hasil kompresi
compressed_label = tk.Label(window, text="Teks Kompresi:")
compressed_label.pack()

compressed_entry = tk.Text(window, height=5)
compressed_entry.pack()

# Tombol Hapus
clear_button = tk.Button(window, text="Hapus", command=clear_text)
clear_button.pack()

window.mainloop()