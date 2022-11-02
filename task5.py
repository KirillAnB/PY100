from random import sample
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p','q','r','s','t','u','v','w','x','y','z']
upper_char_list= []

for char in char_list:
    if char.upper() not in char_list:
        char_list.append(char.upper())

for num in range(0,10):
    if str(num) not in char_list:
        char_list.append(str(num))

def get_random_password(list_1, n=8) -> str:
    random_password_list = (sample(list_1,n))
    random_password_list_str = ''.join(random_password_list)
    return random_password_list_str


print(get_random_password(char_list))
