# coding = utf-8

"""
    作者：shao
    功能：分形树1-turtle使用
    版本：v2.0-绘制渐大五角星
    时间：2018年11月15日23:04:28
"""


import turtle


def draw_pentagram(size):
    """
    绘制五角星
    :return:
    """
    # 计数器
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    """
    主函数
    :return:
    """
    # 抬起笔
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    # 设定笔的宽度
    turtle.pensize(1.5)
    turtle.pencolor('yellow')
    size = 50
    while size <= 250:
        draw_pentagram(size)
        size += 50


    turtle.exitonclick()


if __name__ == '__main__':
    main()