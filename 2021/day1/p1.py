def get_num_time_depths_increase(file_input):
    num_times_increase = 0;
    with open(file_input) as f:
        curr_num_to_check = int(f.readline().rstrip())

        rest_of_nums = f.readlines()
        for num in rest_of_nums:
            num = int(num.rstrip())
            if num > curr_num_to_check:
                num_times_increase += 1
            curr_num_to_check = num
    return num_times_increase

total_num_times_increase = get_num_time_depths_increase(file_input='./input')
