import turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(730, 490)
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
guessed_states_list = []
score = Scoreboard()
all_states_list = df.state.to_list()

while len(guessed_states_list) < 50:
    #    Get the user's answer
    answer_state = (screen.textinput(title="Guess the State", prompt="Write a state's name: ")).title()
    #    If the answer is a valid US state write its name on the state on the map,
    #    else don't write anything and wait for another answer
    if answer_state in all_states_list:
        dr = df[df.state == answer_state]
        guessed_states_list.append(answer_state)
        score.increment_score()
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(dr.x), int(dr.y))
        t.write(answer_state, False, "center", ("Arial", 8, "normal"))
    #    If the user wants to exit, generate a csv file with the names of all the states
    #    that the user couldn't guess
    if answer_state == "exit" or answer_state == "Exit" or answer_state == "EXIT":
        missing_states_list = [state for state in all_states_list if state not in guessed_states_list]
        states_to_learn = pandas.DataFrame(missing_states_list)
        states_to_learn.to_csv("states_to_learn.csv")
        break
