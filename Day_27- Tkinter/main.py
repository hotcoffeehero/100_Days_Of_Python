from tkinter import *

def button_clicked() :
    print('I got clicked.')
    new_thang = input.get()
    my_label.config(text=new_thang )

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=500)


#label
my_label = Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label['text'] = 'New Text'
my_label.config(text='New Text')
my_label.place(x=0, y=0)

#button
button = Button(text='Click Me', command=button_clicked)
button.pack()

#button
input = Entry(width=20)
input.pack()




window.mainloop()