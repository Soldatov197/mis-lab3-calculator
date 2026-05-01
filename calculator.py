import tkinter as tk
from tkinter import messagebox


# Функция добавления символов в поле ввода
def add_symbol(symbol):
    entry.insert(tk.END, symbol)


# Функция вычисления выражения
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # вычисляем выражение
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль!")
    except Exception:
        messagebox.showerror("Ошибка", "Некорректное выражение!")


# Очистка поля
def clear():
    entry.delete(0, tk.END)


# Перевод в восьмеричную систему
def to_octal():
    try:
        value = entry.get()

        # Проверяем, что число натуральное
        number = int(float(value))

        if number < 0:
            raise ValueError

        oct_value = oct(number)[2:]  # убираем "0o"
        messagebox.showinfo(
            "Восьмеричная система",
            f"{number} в восьмеричной системе = {oct_value}"
        )

    except ValueError:
        messagebox.showerror(
            "Ошибка",
            "Введите натуральное число для перевода!"
        )


# Создание окна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

# Поле ввода
entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

# Кнопки
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
        if btn == "=":
            action = calculate
        else:
            action = lambda x=btn: add_symbol(x)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial", 14),
            command=action
        ).pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Нижние кнопки
bottom_frame = tk.Frame(root)
bottom_frame.pack(expand=True, fill=tk.BOTH)

tk.Button(
    bottom_frame,
    text="C",
    font=("Arial", 14),
    command=clear
).pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

tk.Button(
    bottom_frame,
    text="Oct",
    font=("Arial", 14),
    command=to_octal
).pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

root.mainloop()
