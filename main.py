import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=490)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=F"{len(guessed_state)} / 50 states correct",
                                    prompt="What's another state in teh US").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state ]
        data = pandas.DataFrame({"missing state": missing_states})
        data.to_csv("Missing_states.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        write = turtle.Turtle()
        write.hideturtle()
        write.penup()
        state_data = data[data.state == answer_state]
        write.goto(int(state_data.x), int(state_data.y))
        write.write(state_data.state.item())


def get_mouse_click_coordinates(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coordinates)


turtle.mainloop()
