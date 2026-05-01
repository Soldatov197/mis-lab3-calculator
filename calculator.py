import tkinter as tk


def add_symbol(symbol):
    entry.insert(tk.END, symbol)


def clear():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill=tk.BOTH)
    for btn in row:
        action = clear if btn == '=' else lambda x=btn: add_symbol(x)
        tk.Button(row_frame, text=btn, font=("Arial", 14), command=action).pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

root.mainloop()
