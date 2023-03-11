from tkinter import *
import playground


def button_clicked():
    new_text = input.get()
    label.config(text= new_text)


window = Tk()
window.title("My first GUI")
window.minsize(width= 500, height= 300)
window.config(padx= 20, pady= 20)

#label
label = Label(text= "Label", font= ("arial", 24, "bold"))
label.grid(column= 0, row= 0)

#button
button = Button(text= "Click Here", command= button_clicked)
button.grid(column= 1, row= 1)

#new button
new_button = Button(text= "Exit")
new_button.grid(column= 2, row= 0)

#Entry
# replace Label with input below when button (above) is clicked
input = Entry(width= 10,)
input.grid(column= 3, row= 3)






window.mainloop()