from tkinter import *

def convert():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilo_result_label.config(text=f"{km}")

window = Tk()
window.title('Miles to Kilometers Converter')
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=2,row=1)

miles = Label(text='miles')
miles.grid(column=3, row=1)

equal_to = Label(text='is equal to')
equal_to.grid(column=1, row=2)

kilo_result_label = Label(text='0')
kilo_result_label.grid(column=2, row=2)

kilo_label = Label(text='km')
kilo_label.grid(column=3, row=2)

calc_button = Button(text='Calculate', command=convert)
calc_button.grid(column=2, row=3)


window.mainloop()