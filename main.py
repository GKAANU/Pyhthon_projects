import turtle as t
import random
color_list = [(204, 155, 102), (239, 242, 245), (70, 107, 129), (165, 76, 49), (239, 245, 242), (123, 153, 169), (132, 173, 156), (115, 83, 99), (224, 197, 135), (50, 37, 22), (182, 93, 107), (158, 140, 75), (185, 127, 142), (80, 115, 111), (22, 39, 52), (82, 166, 132), (211, 101, 75), (30, 74, 86), (232, 166, 162), (9, 27, 25), (39, 32, 34), (147, 35, 29), (145, 35, 40), (113, 122, 156), (91, 139, 151), (226, 169, 173), (170, 204, 193), (36, 76, 74)]
t.colormode(255)
# colors = colorgram.extract('image.png', 30)
# print(colors[0].rgb)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
tim = t.Turtle()
tim.speed(0)
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(10):
    for j in range(10):
        random_color = random.choice(color_list)
        tim.dot(10, random_color)
        tim.forward(50)
    tim.backward(50*10)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)





screen = t.Screen()
screen.exitonclick()
