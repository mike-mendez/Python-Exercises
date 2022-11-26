import turtle
import pandas

# DATA
data = pandas.read_csv("./data/50_states.csv")
states = data.state.tolist()
# INITIALIZED VARIABLES
correct_states = []

# TURTLE
screen = turtle.Screen()
screen.title("U.S States Game")
image = "./images/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# USER INPUT
while len(correct_states) < 50:
    user_answer = screen.textinput(title="Guess A State", prompt="Enter a state:").title()
    if user_answer == "Exit":
        # result = [new_item for item in list if test]
        missing_states = [state for state in states if state not in correct_states]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("./data/states_to_learn.csv")
        break
    if user_answer not in correct_states:
        if len(data[data.state == user_answer]):
            state_data = data[data.state == user_answer]
            correct_states.append(user_answer)

            # WRITING STATE NAME ON SCREEN
            text = turtle.Turtle()
            text.hideturtle()
            text.penup()
            text.goto(int(state_data.x), int(state_data.y))
            text.write(state_data.state.item())
