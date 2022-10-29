#def get_count_char(str_):
#  ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
def get_count_char(str_):
    chars_dict={}
    str_=str_.lower()
    for simbol in str_:
         if simbol.isalpha():
            chars_dict[simbol] = str_.count(simbol)
    return chars_dict
chars_dict = get_count_char(main_str)
print(get_count_char(main_str))

def count_char(dict_):
    '''Функция получает словарь и заменяет значения ключей на процент от общей суммы значений'''
    percent_char={}
    total = sum(dict_.values())
    for key in dict_:
        percent_char[key] =round(100/(total/dict_[key]),2)
    return percent_char


chars_in_percents = count_char(chars_dict)
print(chars_in_percents)

