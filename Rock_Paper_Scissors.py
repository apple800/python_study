'''
Make a rock-paper-scissors game where it is the player vs the computer. The computer’s answer will be randomly generated, while the program will ask the user for their input. This project will better your understanding of while loops and if statements.
'''
from random import *
print('가위 바위 보 게임에 오신 여러분을 환영합니다.')
print('여러분은 가위(1번), 바위(2번), 보(3번)을 누르시면 됩니다.')

options = ['가위', '바위', '보', '종료']

while True:
    print('종료를 원하시면 숫자 4를 눌러주세요.')
    player = options[int(input('무엇을 내시렵니까? '))-1]

    if player == '종료':
        print('게임이 종료가 됩니다.4')
        break

    com = options[randint(0, 2)]

    print('-'*6)
    print(f'유저 : {player}\n컴퓨터 : {com}')
    print('-'*6)
    if player == com:
        print('서로 비겼습니다.\n')
    elif (player == '가위') and (com == '바위'):
        print('컴퓨터가 이겼습니다.\n')
    elif (player == '보') and (com == '가위'):
        print('컴퓨터가 이겼습니다.\n')
    elif (player == '바위') and (com == '보'):
        print('컴퓨터가 이겼습니다.\n')
    elif (player == '가위') and (com == '보'):
        print('유저가 이겼습니다.\n')
    elif (player == '보') and (com == '바위'):
        print('유저가 이겼습니다.\n')
    elif (player == '바위') and (com == '가위'):
        print('유저가 이겼습니다.\n')
