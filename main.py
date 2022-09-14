import pandas
import turtle

screen = turtle.Screen()
screen.title("Nigeria. States Game")
image = "Nigerian_map.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("nigeria_states")
nigeria_states = data["nigeria_states"].tolist()
correct_guesses = []
while len(correct_guesses) <= len(nigeria_states):
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/36 States + F.C.T",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = [state for state in nigeria_states if state not in correct_guesses]
        missing_states_dict = {"states_to_learn": missing_states}
        states_data = pandas.DataFrame(missing_states_dict)
        states_data.to_csv("states_to_learn.csv")
        break
    if answer_state in nigeria_states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        state = data[data.nigeria_states == answer_state]
        x_cor = state.x.item()
        y_cor = int(state.y)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x_cor, y_cor)
        pen.write(f"{answer_state}", align="center", font=("courier", 9, "bold"))

screen.exitonclick()

