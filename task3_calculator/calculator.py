import tkinter as tk

window = tk.Tk()
window.title("Calculator")

expression = tk.StringVar()

entry = tk.Entry(window, textvariable=expression, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10)

buttons_frame = tk.Frame(window)
buttons_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+" ,"C"
]


for i, symbol in enumerate(buttons):
    row = i // 4
    column = i % 4
    button = tk.Button(buttons_frame, text=symbol, width=5, height=2,
                       command=lambda s=symbol: button_click(s))
    button.grid(row=row, column=column)

def button_click(symbol):
    if symbol == "=":
        try:
            result = eval(expression.get())
            expression.set(result)
        except Exception:
            expression.set("Error")
    elif symbol == "C":
        expression.set("")
    else:
        current = expression.get()
        expression.set(current + symbol)


window.mainloop()
