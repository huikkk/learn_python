#coding:utf-8
import random
print('你有100元的初始金额，游戏正在准备中')
all_mon_number = 100
print("***游戏开始了***")
def guess_number(win_mon_number):
    str_input = input('买定离手了兄弟们，要大还是要小？：')
    number_a = random.randrange(1,7)
    number_b = random.randrange(1,7)
    number_c = random.randrange(1,7)
    number_result = number_a + number_b + number_c
    if 3 <= number_result <= 10  :
        str_result = '小'
    else:
        str_result = '大'
    str_bool = str_input == str_result
    if str_bool:
        print('投掷的三个点数分别为{},{},{}'.format(number_a,number_b,number_c))
        print('***你猜对了***钱你拿去QAQ，再来！！！')
    else:
        print('投掷的三个点数分别为{},{},{}'.format(number_a, number_b, number_c))
        print('***你猜错了***钱全归我了，O(∩_∩)O')
        win_mon_number = - win_mon_number
    return win_mon_number
while all_mon_number > 0:
    if all_mon_number == 999:
        print('骚年，还挺厉害的啊！')
    elif all_mon_number == 9999:
        print('别玩了，直接去赌场把！')
    win_mon_number = 0
    mon_number = input('这把你想押多少？：')
    win_mon_number = int(mon_number)
    all_mon_number = all_mon_number + guess_number(win_mon_number)
    print('你现在有{}元'.format(all_mon_number))


else:
    print('你这穷鬼快快滚蛋!!!')