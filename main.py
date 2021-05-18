import tkinter as tk
from tkinter import messagebox, INSERT

window = tk.Tk()
window.geometry("450x200")
window.config(bg='purple')
window.resizable(height=False, width=False)
window.title("Calculating area of a circle")

# labels
label1 = tk.Label(window, text="Enter number :")
label1.place(x=20, y=30)
label2 = tk.Label(window, text="Enter radius :")
label2.place(x=20, y=60)
label2 = tk.Label(window, text="Enter radius :")
label2.place(x=20, y=60)


# entry boxes
entry1 = tk.Entry(window, bg='light blue', fg='black')
entry1.place(x=200, y=30, width=100)
entry2 = tk.Entry(window, bg='light blue', fg='black')
entry2.place(x=200, y=60, width=100)

# calculate button
button = tk.Button(window, text="Calculate area", fg='black', border=4, bg="light blue")
button.place(x=320, y=40 )

window.mainloop()

