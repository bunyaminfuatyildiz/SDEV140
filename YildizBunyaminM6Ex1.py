from tkinter import Tk, Label, Entry, Button

def convert_to_fahrenheit():
  """
  This function retrieves the temperature from the Celsius entry,
  converts it to Fahrenheit, and displays the result.
  """
  try:
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_label.config(text=f"{fahrenheit:.2f} °F")
  except ValueError:
    fahrenheit_label.config(text="Invalid Input")

def convert_to_celsius():
  """
  This function retrieves the temperature from the Fahrenheit entry,
  converts it to Celsius, and displays the result.
  """
  try:
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5/9
    celsius_label.config(text=f"{celsius:.2f} °C")
  except ValueError:
    celsius_label.config(text="Invalid Input")

# Create the main window
window = Tk()
window.title("Temperature Converter")

# Create labels
celsius_label = Label(window, text="Celsius:")
celsius_label.grid(row=0, column=0)

fahrenheit_label = Label(window, text="Fahrenheit:")
fahrenheit_label.grid(row=1, column=0)

# Create entry fields
celsius_entry = Entry(window)
celsius_entry.grid(row=0, column=1)

fahrenheit_entry = Entry(window)
fahrenheit_entry.grid(row=1, column=1)

# Create buttons
celsius_to_fahrenheit_button = Button(window, text="Celsius to Fahrenheit", command=convert_to_fahrenheit)
celsius_to_fahrenheit_button.grid(row=2, columnspan=2)

fahrenheit_to_celsius_button = Button(window, text="Fahrenheit to Celsius", command=convert_to_celsius)
fahrenheit_to_celsius_button.grid(row=3, columnspan=2)

# Run the main event loop
window.mainloop()
