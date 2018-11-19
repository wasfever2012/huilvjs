# coding = utf-8
"""
    作者：shao
    功能：bmr指数计算
    版本：V1.0
    时间：2018-11-16
"""
def bmr_compute(str_list):
    """
    计算bmr指数
    :param str_list:
    :return:
    """
    try:
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == '男':
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 56
        elif gender == '女':
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('您的性别：{}， 体重：{} 公斤，身高：{} 厘米， 年龄：{} 岁'.format(gender, weight, height, age))
            print('您的基础代谢率为：{}大卡'.format(bmr))
        else:
            print('性别不支持')
    except IndexError:
        print('您输入的信息不全')
    except ValueError:
        print('您输入的信息格式有误')
    except:
        print('程序错误！')

def main():
    y_or_n = input("是否退出程序（y/n）？")
    while y_or_n == 'n':
        print('请输入您的身份信息，用空格分割：')
        input_str = input('性别（男/女） 体重（kg） 身高（厘米） 年龄 ：')
        input_str_list = input_str.split(' ')
        bmr_compute(input_str_list)
        print()
        y_or_n = input("是否退出程序（y/n）？")

if __name__ == '__main__':
    main()