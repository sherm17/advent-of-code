from enum import Enum

class Rating(Enum):
    CO2_SCRUB = 'CO2_SCRUB'
    OXYGEN_GENERATOR = 'OXYGEN_GENERATOR'

def read_file_into_list(file_input):
    with open(file_input) as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines


def get_most_frequent(lst):
    dict = {}
    most_common_count, most_common = 0, ''

    for item in lst:
        dict[item] = dict.get(item, 0) + 1
        if dict[item] > most_common_count:
            most_common_count, most_common = dict[item], item
    return most_common


def get_opposite_bit(bit):
    if bit == '1':
        return '0'
    return '1'


def convert_bit_to_num(bit_str):
    return int(bit_str, 2)
    

def filter_by_common(bit_str, position, common_bit):
    if bit_str[position] == common_bit:
        return True
    return False


def get_binary_between_two(lst, position, bit):
    if lst[0][position] == bit:
        return lst[0]
    return lst[1] 


def convert_bit_to_num(bit_str):
    return int(bit_str, 2)


def get_rates(binary_list, rate):
    first_binary = binary_list[0]
    lst = binary_list.copy()
    for i in range(len(first_binary)):
        nth_bit_list = map(lambda x: x[i], lst)
        most_common_bit = get_most_frequent(list(nth_bit_list))

        if rate == Rating.CO2_SCRUB:
            least_common_bit = get_opposite_bit(most_common_bit)
            bit_of_interest = least_common_bit
            bit_to_keep = '0'
        elif rate == Rating.OXYGEN_GENERATOR:
            bit_of_interest = most_common_bit
            bit_to_keep = '1'

        if len(lst) == 2:
            correct_binary_str = get_binary_between_two(lst, i, bit_to_keep)
            return correct_binary_str

        elif len(lst) == 1:
            return lst[0]

        lst = list(filter(lambda a: filter_by_common(a, i , bit_of_interest), lst))


def get_life_support_rating():
    binary_list = read_file_into_list(file_input='./input')
    co2_rating_binary = get_rates(binary_list, Rating.CO2_SCRUB)
    co2_rating = convert_bit_to_num(co2_rating_binary)
    
    oxygen_generator_rating_binary = get_rates(binary_list, Rating.OXYGEN_GENERATOR)
    oxygen_generator_rating = convert_bit_to_num(oxygen_generator_rating_binary)
    return co2_rating * oxygen_generator_rating

if __name__ == '__main__':
    life_support_rating = get_life_support_rating()
    print(life_support_rating)






