import turtle
import pandas

screen = turtle.Screen()
screen.title("South African Provinces Game")

image = "sa_map.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("9_Provinces.csv")

list_of_provinces = []
for province in data.province:
    list_of_provinces.append(province)

correct_guesses = 0
guessed_provinces = []

while correct_guesses < len(list_of_provinces):
    if correct_guesses == 0:
        answer_province = screen.textinput(title=f"{correct_guesses}/{len(list_of_provinces)} Provinces Correct",
                                        prompt="What's the name of a province?:")
    elif correct_guesses == 1:
        answer_province = screen.textinput(title=f"{correct_guesses}/{len(list_of_provinces)} Province Correct",
                                        prompt="What's another province's name?:")
    else:
        answer_province = screen.textinput(title=f"{correct_guesses}/{len(list_of_provinces)} Provinces Correct",
                                        prompt="What's another province's name?:")

    if answer_province == "Exit":
        # Generate list of states not guessed by the user
        unguessed_provinces = [province for province in list_of_provinces if province not in guessed_provinces]

        new_data = pandas.DataFrame(unguessed_provinces)
        new_data.to_csv("new_file.csv")

        if len(unguessed_provinces) == 0:
            print("You Got Them All")
        else:
            print(f"You missed the following:")
            for x in unguessed_provinces:
                print(x)
        break

    for province in list_of_provinces:
        if province == answer_province:
            correct_answer = (data[data.province == answer_province])
            x_coor = int(correct_answer.x)
            y_coor = int(correct_answer.y)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x_coor, y_coor)
            t.write(answer_province, font=("Arial", 15, "normal"))
            correct_guesses += 1
            guessed_provinces.append(answer_province)


#
# turtle.mainloop()

screen.exitonclick()
