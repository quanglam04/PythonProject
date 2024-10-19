import subprocess
import os
import tkinter as tk


def process_path():
    path = entry.get()
    if os.path.exists(path):
        result_label.config(text="Valid path: " + path)
        run_cpp_program(path)
    else:
        result_label.config(text="Invalid path! Please try again.")


def run_cpp_program(path):
    try:
        subprocess.run(["reducemap.exe", path])
    except Exception as e:
        print(f"Error: {e}")
root = tk.Tk()
root.title("File Path Search")

label = tk.Label(root, text="Input file path:")
label.pack(padx=10, pady=5)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=process_path)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(padx=10, pady=10)

root.mainloop()