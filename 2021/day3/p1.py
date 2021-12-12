from enum import Enum

class Rate(Enum):
    GAMMA = 'GAMMA'
    EPISOLON = 'EPISOLON'

def read_file_into_list(file_input):
    with open(file_input) as f:
        lines = [line.rstrip() for line in  f.readlines()]
    return lines

def get_most_frequent(lst):
    dict = {}
    most_common_count, most_common = 0, ''

    for item in lst:
        dict[item] = dict.get(item, 0) + 1
        if dict[item] > most_common_count:
            most_common_count, most_common = dict[item], item
    return most_common

def flip_bit_str(bit_str):
    return ''.join('1' if x == '0' else '0' for x in bit_str)

def convert_bit_to_num(bit_str):
    return int(bit_str, 2)
    
def get_rates(binary_list, rate):
    first_binary = binary_list[0]
    bit_str = ''
    for i in range(len(first_binary)):
        nth_bit_list = map(lambda x: x[i], binary_list)
        most_common_bit = get_most_frequent(nth_bit_list)
        bit_str += most_common_bit

    if rate == Rate.EPISOLON:
        # invert bit str
        bit_str = flip_bit_str(bit_str)

    num_from_bit = convert_bit_to_num(bit_str)
    return num_from_bit

def get_power_consumption():
    binary_list = read_file_into_list(file_input='./input')
    gamma_rate = get_rates(binary_list, Rate.GAMMA)
    epsilon_rate = get_rates(binary_list, Rate.EPISOLON)
    power_consumption = gamma_rate * epsilon_rate
    return power_consumption

if __name__ == '__main__':
    power = get_power_consumption()
    print(power)
