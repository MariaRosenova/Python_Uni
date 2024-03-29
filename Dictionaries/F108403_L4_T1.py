import sys

d = {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'd', 6: 'e', 7: 'a', 8: 'b'}

data_to_check = input('Enter an array of values to check, separated by comma: ').split(',')
data_to_check = [int(x) for x in data_to_check]


for key, value in d.items():
    if key in data_to_check:
        print(key,value)
