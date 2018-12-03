"""
    作者：shao
    功能：密码强度判断
    时间：2018年12月3日22:44:58
    版本：V2.0
    增加功能：定义一个Password工具类
"""


class PasswordTool:
    """
        密码工具类
    """

    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    # 字符串处理
    def process_password(self):
        # 规则1 长度大于6
        if len(self.password) >= 6:
            self.strength_level += 1
        else:
            print('密码长度必须大于6！')

        # 规则2 包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码必须包含数字！')

        # 规则3 包含字母
        if self.check_alpha_exist():
            self.strength_level += 1
        else:
            print('密码必须包含字母！')

    # 类的方法
    def check_len(self):
        """
        判断密码长度
        :param password:
        :return:
        """
        len_ok = False
        if len(self.password) >= 6:
            len_ok = True

        return len_ok

    def check_number_exist(self):
        """
        判断密码是否包含数字
        :param password:
        :return:
        """
        number_exist = False
        for c in self.password:
            if c.isnumeric():
                number_exist = True
                break

        return number_exist

    def check_alpha_exist(self):
        """
        判断密码是否包含字母
        :param password:
        :return:
        """
        alpha_exist = False
        for c in self.password:
            if c.isalpha():
                alpha_exist = True
                break

        return alpha_exist


def main():
    try_time = 5
    while try_time > 0:
        password = input('请输入密码： ')

        # 实例化对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        f = open('password_record.txt', 'a')
        f.write('密码:{}, 强度：{} \n'.format(password_tool.password, password_tool.strength_level))
        f.close()

        if password_tool.strength_level >= 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！请重新输入！')
            try_time -= 1


if __name__ == '__main__':
    main()
