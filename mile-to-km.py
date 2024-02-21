from tkinter import *

def miles_to_km():
    km = round(int(input.get()) * 1.60934, 2)
    result_label.config(text=km)

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=25, pady=25)

result_label = Label(text=0, font=24)
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=24)
km_label.grid(column=2, row=1)

miles_label = Label(text="Miles", font=24)
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=(24))
is_equal_to_label.grid(column=0, row=1)

button = Button(text="Calculate", command=miles_to_km, font=24)
button.grid(column=1, row=2)

input = Entry(width=7, font=24)
input.grid(column=1, row=0)
input.get()


window.mainloop()
