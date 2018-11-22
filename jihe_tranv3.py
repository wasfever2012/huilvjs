"""
    作者：shao
    功能：集合的训练
    版本：v3.0
    V1.0：使用元组tuple
    V2.0：使用list
    新增功能：使用集合set
    时间：2018-11-22
"""

from datetime import datetime


def is_leap_year(year):
    """
        判断年份是否为闰年
    :param year: 输入年份
    :return: True 是闰年 FALSE 不是闰年
    """
    is_leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
    return is_leap


def main():
    input_year_str = input('请按格式输入需要判断的年份（yyyy-mm-dd）: ')
    input_year = datetime.strptime(input_year_str, '%Y-%m-%d')
    year = input_year.year
    month = input_year.month
    day = input_year.day
    # 30天月数集合,不包括2月份
    _30_in_month_set = {4, 6, 9, 11}
    # 31天月数集合
    _31_in_month_set = {1, 3, 5, 7, 8, 10, 12}
    days = day
    for i in range(1, month):
        if i in _30_in_month_set:
            days += 30
        elif i in _31_in_month_set:
            days += 31
        else:
            days += 28  # 默认假设不是闰年

    # 针对闰年的处理
    if is_leap_year(year) and month > 2:
        days += 1

    print('{}年是否为闰年：{}'.format(year, is_leap_year(year)))
    print('您输入的日期是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()
