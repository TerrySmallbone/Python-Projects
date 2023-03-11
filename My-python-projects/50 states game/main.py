import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = ("blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

## create lists from data rowss
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 states correct",
                                    prompt= "Please type your guess").title()

    ## Exit game command
    if answer_state == "Exit":
        states_to_learn = [item for item in states if item not in guessed_states]
        # states_to_learn = []
        # for state in states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    ## if answer is in list of states
    if answer_state in states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            state_data = data[data.state == answer_state]
            new_turtle.goto(x= int(state_data.x), y= int(state_data.y))
            new_turtle.write(answer_state)
