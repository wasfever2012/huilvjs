"""
	作者：shao
	时间：11/16/2018
    版本：
"""


# def convert_currency(im, er):
#     """
#         汇率兑换函数
#     """
#     out = im * er
#     return out


def main():
    # 汇率
    USD_VS_CNY = 6.77

    # 带单位的输入
    currency_str_value = input("请输入带单位的货币金额：")
    # 获取单位
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_CNY

    elif unit == 'USD':
        exchange_rate = USD_VS_CNY

    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])

        # out_money = convert_currency(in_money, exchange_rate)
        convert_currency = lambda x: x * exchange_rate
        out_money = convert_currency(in_money)
        print('转换后的金额为: ', out_money)

    else:
        print('不支持该种货币')


if __name__ == '__main__':
    main()