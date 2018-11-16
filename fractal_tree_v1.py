#coding = utf-8
"""
    作者：shao
    功能：分形树绘制
    版本：v1.0
    日期：2018-11-16
"""
import turtle


def draw_branch(brach_length):
    """
    绘制分支
    :return:
    """
    if brach_length > 10:
        # 绘制右侧树枝
        turtle.forward(brach_length)
        turtle.right(20)
        draw_branch(brach_length-10)

        # 绘制左侧树枝
        turtle.left(40)
        draw_branch(brach_length - 10)

        # 返回原来树枝
        turtle.right(20)
        turtle.backward(brach_length)


def main():
    # 主函数
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.forward(1)
    turtle.pendown()

    draw_branch(40)

    turtle.exitonclick()

if __name__ == '__main__':
    main()