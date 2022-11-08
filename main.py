import logic


def game():
    game_end = False
    logic.logo()  # Отображаем баннер-приветсвие

    game_field, turn = logic.new_game_field_creator()  # Создаем пустое игровое поле и счетчик ходов

    logic.show_game_field(game_field)  # Отображаем текущее состояние игровых полей

    while not game_end:
        player_chose = logic.player_step(game_field, turn)  # Получаем ход от игрока и проверяем его корректность
        turn += 1
        if player_chose:
            game_end = True
    one_more_time = logic.new_game()
    if one_more_time:
        game()


game()
