# coding = utf-8

"""
    作者：shao
    功能：分形树1-turtle使用
    版本：v1.0
    时间：2018年11月15日23:04:28
"""


import turtle


def main():
    """
    主函数
    :return:
    """
    count = 1
    while count <= 5:
        turtle.forward(100)
        turtle.right(108)
        count = count + 1
    turtle.exitonclick()


if __name__ == '__main__':
    main()