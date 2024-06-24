import tkinter as tk
from tkinter import ttk
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + number)
def button_operator(operator):
    global first_number
    global operation
    first_number = float(display.get())
    operation = operator
    display.delete(0, tk.END)
def button_equal():
    second_number = float(display.get())
    display.delete(0, tk.END)
    if operation == "+":
        display.insert(0, first_number + second_number)
    elif operation == "-":
        display.insert(0, first_number - second_number)
    elif operation == "*":
        display.insert(0, first_number * second_number)
    elif operation == "/":
        if second_number == 0:
            display.insert(0, "Ошибка")
        else:
            display.insert(0, first_number / second_number)
def button_clear():
    display.delete(0, tk.END)
def button_dot():
    current = display.get()
    if "." not in current:
        display.insert(tk.END, ".")

root = tk.Tk()
root.title("Калькулятор")

display = tk.Entry(root, width=25, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = ttk.Button(root, text="1", command=lambda: button_click("1"))
button_2 = ttk.Button(root, text="2", command=lambda: button_click("2"))
button_3 = ttk.Button(root, text="3", command=lambda: button_click("3"))
button_4 = ttk.Button(root, text="4", command=lambda: button_click("4"))
button_5 = ttk.Button(root, text="5", command=lambda: button_click("5"))
button_6 = ttk.Button(root, text="6", command=lambda: button_click("6"))
button_7 = ttk.Button(root, text="7", command=lambda: button_click("7"))
button_8 = ttk.Button(root, text="8", command=lambda: button_click("8"))
button_9 = ttk.Button(root, text="9", command=lambda: button_click("9"))
button_0 = ttk.Button(root, text="0", command=lambda: button_click("0"))
button_plus = ttk.Button(root, text="+", command=lambda: button_operator("+"))
button_minus = ttk.Button(root, text="-", command=lambda: button_operator("-"))
button_multiply = ttk.Button(root, text="*", command=lambda: button_operator("*"))
button_divide = ttk.Button(root, text="/", command=lambda: button_operator("/"))
button_equal = ttk.Button(root, text="=", command=button_equal)
button_clear = ttk.Button(root, text="C", command=button_clear)
button_dot = ttk.Button(root, text=".", command=button_dot)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_plus.grid(row=1, column=3)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)
button_dot.grid(row=5, column=0)


root.mainloop()
