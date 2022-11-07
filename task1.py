# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

list_of_dicts = [{'bin':bin(value),'dec':value,'hex':hex(value),'oct':oct(value)} for value in range(16)]
pprint(list_of_dicts)

# dict_1={ 'bin':bin(value)  for value in range(16)}
