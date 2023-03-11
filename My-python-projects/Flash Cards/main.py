from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
card_front = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(400, 150, text="Title", font=("arial", 40, "italic"))
canvas.create_text(400, 300, text="Text", font=("arial", 60, "bold"))

# buttons
wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, width=50, height=50)
unknown_button.grid(column=0, row=1, pady=30, padx=30)
right_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=right_image, highlightthickness=0, width=50, height=50)
correct_button.grid(column=1, row=1, pady=30, padx=30)

window.mainloop()
