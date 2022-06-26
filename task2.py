# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.

# PS: Компьютер получился глупый, так как ставит нолики рандомно. Это доработаю потом...

import random

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = ' -------------- \n ' \
        '| 1 | 2 | 3 | \n ' \
        '-------------- \n ' \
        '| 4 | 5 | 6 | \n ' \
        '-------------- \n ' \
        '| 7 | 8 | 9 | \n ' \
        '-------------- \n'

change_board = board
players_moves = []
pc_moves = []
all_moves: list = []

win = False
win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


print(board)

while not win:
    print('Ваш ход: ', end='')
    player_move = int(input())
    while player_move in all_moves:
        print('Похоже это место уже занято. Сделайте другой ход: ', end='')
        player_move = int(input())
    players_moves.append(player_move)
    all_moves.append(player_move)
    change_board = change_board.replace(str(player_move), 'X')
    # print(change_board)
    for i in win_list:
        if i[0] in players_moves and i[1] in players_moves and i[2] in players_moves:
            win = True
    if win:
        print('Вы победили, поздравляем!')
        print(change_board)
        break

    pc_move = random.randint(1, 10)
    while pc_move in all_moves:
        pc_move = random.randint(1, 10)
    print(f'Ход компьютера: {pc_move}')
    pc_moves.append(pc_move)
    all_moves.append(pc_move)
    change_board = change_board.replace(str(pc_move), 'O')
    print(change_board)
    for i in win_list:
        if i[0] in pc_moves and i[1] in pc_moves and i[2] in pc_moves:
            win = True
    if win:
        print('Вы проиграли( Попробуйте еще раз.')
        print(change_board)
        break