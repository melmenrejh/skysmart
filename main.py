
board = list(range(0, 9))
print(board)

cells = 3
dashes = 13
spaces = 14
counter = 0
player_token = ''

is_win = False
win_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

print('Tic-tac toe the game for two players')


while not is_win:
    for i in range(cells):
        print(' ' * dashes, end='')
        print('-' * dashes)
        print(' ' * dashes, end='')
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
        print(' ' * dashes, end='')
        print('-' * dashes)

    if counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = 'O'

    is_valid = False
    while not is_valid:
        player_answer = (input(f'Where we put a {player_token}?'))

        try:  # Try - пытаться. Пробуем преобразовать строку в число
            player_answer = int(player_answer)
            # Если не получается, срабатывает ошибка.

        except:  # Except - исключение. Выполняем другой код, если возникла ошибка
            print('Неправильный ввод. Нужно ввести число.')
            continue

        if player_answer > 8 or player_answer < 0:
            print('Число должно быть от 0 до 8!')
            continue
        else:
            is_valid = True

    if str(board[player_answer]) not in 'XO':
        board[player_answer] = player_token
    else:
        print('This cell is already taken!')
        continue
    counter += 1

    if counter > 4:
        for each in win_coords:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                is_win = True
                break
        if is_win:
            print(f'{player_token} is win!')
            break
    if counter == 9:
        print('Draw!')
















