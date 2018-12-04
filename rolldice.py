# coding=utf8
"""
    作者：shao
    版本：V1.0
    时间：2018年12月4日
    功能：模拟掷骰子，计算概率
"""
import random


def roll_dice():
    """
        模拟掷骰子
    :return: roll，骰子的值
    """
    roll = random.randint(1, 6)
    return roll


def main():
    # 定义骰子list,初始值为[0,0,0,0,0,0],记录掷骰子的次数
    roll_list = [0] * 6
    # 模拟次数
    total_times = 10

    for i in range(total_times):
        roll = roll_dice()
        for j in range(1, 7):
            if roll == j:
                roll_list[j - 1] += 1

    for i, result in enumerate(roll_list):
        print('点数{}的次数为：{},概率为：{}'.format(i + 1, result, result / total_times))


if __name__ == '__main__':
    main()
