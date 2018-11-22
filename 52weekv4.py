# conding = utf-8
"""
    作者：shao
    功能：52周存钱计算
    版本：V4.0 使用for循环代替while 使用range计数，封装函数
    时间：2018-11-18 20:42:41
"""

import math


def money_compute(money_per_week, increase_money, total_week):
    """
    :param money_per_week: 每周存入金额
    :param increase_money: 每周递增金额
    :param total_week: 总共存钱周数
    :return:
    """
    money_list = []
    for i in range(total_week):
        # 存钱操作
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        # 输出信息
        print('第{}周，存入钱数为{}，存款总额为{}'.format(i+1, money_per_week, saving))
        # 更新下一周存款信息
        money_per_week += increase_money

def main():
    """
        主函数
    :return:
    """
    print('请输入您的存款计划，用空格分割：')
    input_str = input('每周存款金额（元） 每周递增存款金额（元） 总共存款周数（周）')
    input_str_list = input_str.split(' ')

    money_compute(money_per_week=int(input_str_list[0]), increase_money=int(input_str_list[1]), total_week=int(input_str_list[2]))


if __name__ == '__main__':
    main()