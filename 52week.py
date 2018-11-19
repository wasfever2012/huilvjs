# conding = utf-8
"""
    作者：shao
    功能：52周存钱计算
    版本：V1.0
    时间：2018-11-18 20:42:41
"""

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

    while i <= 52:
        # 存钱操作
        saving += money_per_week
        # 输出信息
        print('第{}周，存入钱数为{}，存款总额为{}'.format(i, money_per_week, saving))
        # 更新信息
        money_per_week += increase_money
        i += 1

if __name__ == '__main__':
    main()