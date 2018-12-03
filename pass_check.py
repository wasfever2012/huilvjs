"""
    作者：shao
    功能：密码强度判断
    时间：2018年11月27日22:47:23
"""


def check_len(password):
    """
    判断密码长度
    :param password:
    :return:
    """
    len_ok = False
    if len(password) >= 6:
        len_ok = True

    return len_ok


def check_number_exist(password):
    """
    判断密码是否包含数字
    :param password:
    :return:
    """
    number_exist = False
    for c in password:
        if c.isnumeric():
            number_exist = True
            break

    return number_exist


def check_alpha_exist(password):
    """
    判断密码是否包含字母
    :param password:
    :return:
    """
    alpha_exist = False
    for c in password:
        if c.isalpha():
            alpha_exist = True
            break

    return alpha_exist


def main():
    try_times = 5
    while try_times >= 0:
        password_input = input('请输入密码：')
        # 记录密码强度，大于3合格
        password_strength = 0

        # 规则1：判断密码长度是否符合要求
        if check_len(password_input):
            password_strength += 1
        else:
            print('密码长度不合要求,长度必须大于6位！')

        # 规则2：判断密码是否包含数字
        if check_number_exist(password_input):
            password_strength += 1
        else:
            print('密码必须包含数字！')

        # 规则3：判断密码是否包含字母
        if check_alpha_exist(password_input):
            password_strength += 1
        else:
            print('密码必须包含字母！')

        if password_strength == 3:
            print('恭喜密码设置成功！')
            f = open('password_record.txt', 'a')
            f.write('密码:{},强度:{} \n'.format(password_input, password_strength))
            f.close()
            break
        else:
            try_times -= 1
            print('密码设置失败，请重新设置！')

        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()
