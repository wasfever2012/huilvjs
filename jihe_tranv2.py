"""
    作者：shao
    功能：集合的训练
    版本：v2.0
    V1.0：使用元组tuple
    新增功能：使用list
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
    # 默认月份的天数（非闰年）
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 判断是否为闰年
    if month > 2 and is_leap_year(year):
        days_in_month_list[1] = 29  # 闰年，将2月改为29天
    days = sum(days_in_month_list[:month - 1]) + day

    print('您输入的日期是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()
