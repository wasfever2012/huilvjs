"""
    作者：shao
    功能：集合的训练
    版本：v1.0  使用元组
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
    # 计算之前的天数
    days_in_month_trp = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month_trp[:month - 1]) + day
    # 判断是否为闰年
    if month > 2 and is_leap_year(year):
        days += 1
    if is_leap_year(year):
        print('{}年是闰年'.format(year))
    else:
        print('{}年不是闰年'.format(year))
    print('您输入的日期是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()
