from tkinter import *

def calculate():
    new_output = round(float(input.get()) * 1.60934, 2)
    output.config(text= new_output)

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width= 500, height= 300)
# window.config(padx= 20, pady= 20)

is_equal_to_label = Label(text= "is equal to")
is_equal_to_label.grid(row= 1, column= 0)
is_equal_to_label.config(padx= 20, pady= 20)

input = Entry(width= 5)
input.grid(column=1, row= 0)
# input.config(padx= 20, pady= 20)

#output


button = Button(text= "calculate", command= calculate)
button.grid(column= 1, row= 2)
# button.config(padx= 20, pady= 20)

miles = Label(text= "Miles")
miles.grid(row= 0, column= 2)

km_label = Label(text= "Km")
km_label.grid(row= 1, column= 2)

output = Label(text= 0)
output.grid(row= 1, column= 1)


window.mainloop()