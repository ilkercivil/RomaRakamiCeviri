import tkinter as tk
import roman

def convert_roman():
    roman_input = roman_entry.get().upper()
    try:
        decimal_output = roman.fromRoman(roman_input)
        if 1 <= decimal_output <= 4999:
            result_label.config(text="Normal sayı sistemi: " + str(decimal_output))
        else:
            result_label.config(text="Girilen Roma rakamı 1 ile 4999 arasında olmalıdır.")
    except roman.InvalidRomanNumeralError:
        result_label.config(text="Geçersiz bir Roma rakamı girdiniz.")


def clear_input():
    roman_entry.delete(0, 'end')


# GUI
root = tk.Tk()
root.title("Roma Rakamı Dönüştürücü")

roman_entry = tk.Entry(root, width=20, font=('Arial', 14))
roman_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
for i, button in enumerate(buttons):
    tk.Button(root, text=button, width=5, font=('Arial', 14), command=lambda b=button: roman_entry.insert('end', b)).grid(row=(i//3)+1, column=i%3)

tk.Button(root, text="Sil", width=5, font=('Arial', 14), command=clear_input).grid(row=3, column=2)

convert_button = tk.Button(root, text="Çevir", width=10, font=('Arial', 14), command=convert_roman)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.grid(row=4, column=0, columnspan=3)

root.mainloop()
