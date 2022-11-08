from art import game_logo as banner
def game():
    """основная функция, запускает процесс игры"""
    pass


def logo():
    """выводит лого игры в консоли"""
    print(banner)


def new_game_field_creator():
    """Создает пустое поле для игры и новый счетчик ходов"""
    empty_dict = {
        '1':' ','2':' ','3':' ',
        '4':' ','5':' ','6':' ',
        '7':' ','8':' ','9':' '
    }
    steps_counter = 0
    return empty_dict, steps_counter

def player_step(game_fields,step):
    """Принимает ход игрока"""
    correct_input = False
    count = step
    while correct_input == False:
        try:
            simbol = 'X' if count%2 == 0 else 'O'
            print(f"Ваш ход {simbol}")
            field = int(input("Выберите свободное поле для хода: "))
            if field > 9 or field < 1:
                print("Номер поля должен быть от 1 до 9")
                continue
            elif check_field(game_fields,field) == False:
                print("Это поле занято, выберите другое поле")
                continue
            else:
                correct_input = True
                field = str(field)
                set_field(game_fields, field, count)
        except:
            print("Проверьте правильность ввода(цифры от 1 до 9)")
    show_game_field(game_fields)
    if win_or_draw_check(game_fields,step) == True:
        return True


def check_field(dict_:dict,field_num:int)->bool:
    """Проверяет если поле свободно для хода игрока"""
    if dict_[str(field_num)] != ' ':
        return False
    else:
        return True

def set_field(dict_,field,step):
    if step % 2 == 0:
        dict_[field] = 'X'
    else:
        dict_[field] = 'O'


def show_game_field(board):
    """Отображает игровое поле после хода"""
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def win_or_draw_check(theBoard:dict,step:int)->bool:
    """Проверяет закончена ли игра"""
    if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # top
        print(f"Игрок {theBoard['1']} выиграл.")
        return True
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # middle
        print(f"Игрок {theBoard['4']} выиграл.")
        return True
    elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # bottom
        print(f"Игрок {theBoard['7']} выиграл.")
        return True
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # left side
        print(f"Игрок {theBoard['1']} выиграл.")
        return True
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # middle 
        print(f"Игрок {theBoard['2']} выиграл.")
        return True
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # right side
        print(f"Игрок{theBoard['3']} выиграл.")
        return True
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal 1
        print(f"Игрок {theBoard['1']} выиграл.")
        return True
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal 2
        print(f"Игрок {theBoard['7']} выиграл.")
        return True
    elif step == 8:
        print("Ничья.Игра закочнена.")
        return True
    else:
        return False


def new_game()-> bool:
    """Проверяет, если гроки хотят продолжит игру"""
    try:
        user_input = input("Запустить новую игру?('Y' для запуска)")
        return True if user_input.lower() =='y' else False
    except:
        return False


# def player_simbol(count:int)-> str:
#     """Определяем символ, который ставит игрок"""
#     if count % 2 == 0:
#         return 'X'
#     else:
#         return 'O'

