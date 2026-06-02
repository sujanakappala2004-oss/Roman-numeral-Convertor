import tkinter as tk

def to_roman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_num = ""
    i = 0

    while num > 0:
        for _ in range(num // values[i]):
            roman_num += symbols[i]
            num -= values[i]
        i += 1

    return roman_num


def translate(message):
    words = message.split()
    result = []

    for word in words:
        try:
            num = int(word)

            if num < 4000:
                result.append(to_roman(num))
            else:
                result.append(word)

        except ValueError:
            result.append(word)

    return " ".join(result)


msg = input()

c = "True"

for i in msg:
    if i.isalpha():
        if i.islower():
            c = "False"

if c == "True":
    print(translate(msg))
else:
    print("Please type the letters in uppercase")


def translate_message():
    message = input_text.get("1.0", tk.END).strip()
    translated_message = translate(message)

    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", translated_message)


# Create the main window
window = tk.Tk()
window.title("Arabic to Roman Numeral Translator")

# Create the input label and text box
input_label = tk.Label(
    window,
    text="Enter a message with Arabic numerals (less than 4000) to translate to Roman numerals:"
)
input_label.pack()

input_text = tk.Text(window, height=5)
input_text.pack()

# Create the output label and text box
output_label = tk.Label(window, text="Translated message:")
output_label.pack()

output_text = tk.Text(window, height=5)
output_text.pack()

# Create the translate button
translate_button = tk.Button(
    window,
    text="Translate",
    command=translate_message
)
translate_button.pack()

# Run the GUI loop
window.mainloop()
