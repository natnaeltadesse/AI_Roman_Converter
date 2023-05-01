import tkinter as tk
from tkinter import messagebox


# Function to check if a given Roman numeral is valid
def is_valid_roman(roman):
    if not roman:
        return False

    valid_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    if not all(char in valid_chars for char in roman):
        return False

    for char, max_repeats in [('I', 3), ('X', 4), ('C', 4), ('M', 4),('V',1)]:
        if roman.count(char * (max_repeats + 1)) > 0:
            return False

    for invalid_substring in ['VIV', 'LXL', 'DCD']:
        if invalid_substring in roman:
            return False

    return True


# Function to convert a given Roman numeral to its decimal equivalent
def roman_to_decimal(roman):
    if not is_valid_roman(roman):
        raise ValueError("Invalid Roman numeral")

    roman_to_decimal_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    decimal = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_to_decimal_map[char]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value

    return decimal


# Function to convert the given Roman numeral to its decimal equivalent
def convert():
    roman_number = entry.get().strip().upper()
    try:
        decimal_number = roman_to_decimal(roman_number)
        result_var.set(f"The decimal equivalent of \"{roman_number}\" is {decimal_number}.")
    except ValueError as e:
        messagebox.showerror("Error", e)


# Create the GUI window
app = tk.Tk()
app.title("Roman to Decimal Converter")

frame = tk.Frame(app, padx=50, pady=20)
frame.pack()
# Create the label and entry widgets
label = tk.Label(frame, text="Enter a Roman number between 1 and 3999:", font="15")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame, width=40,font="10",border=False)
entry.grid(row=1, column=0, sticky="w")
# Create the button and result label widgets
convert_button = tk.Button(frame, text="Convert", command=convert, background="blue",foreground="white",border=False)
convert_button.grid(row=2, column=0, pady=10, sticky="w")

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var,font="15", foreground="green")
result_label.grid(row=3, column=0, sticky="w")
# Start the main loop
app.mainloop()