# conding = utf-8
"""
    作者：shao
    功能：52周存钱计算
    版本：V3.0 使用for循环
    时间：2018-11-18 20:42:41
"""

import math


def main():
    """
        主函数
    :return:
    """

    money_per_week = 10   # 每周存入金额
    i = 1                 # 周数记录
    increase_money = 10   # 递增的存额
    total_week = 52       # 总共时间（周数）
    saving = 0            # 账户累计

    money_list = []       # 记录每周存款的列表

    while i <= total_week:
        # 存钱操作
        # saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        # 输出信息
        print('第{}周，存入钱数为{}，存款总额为{}'.format(i, money_per_week, saving))
        # 更新下一周的存款信息
        money_per_week += increase_money
        i += 1

if __name__ == '__main__':
    main()