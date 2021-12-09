def get_depth_increase_by_three_measurement(file_input):
    num_times_increase = 0;

    with open(file_input) as f:
        depth_list = [int(line.rstrip()) for line in f]
    curr_num_to_check = sum(depth_list[:3])
    for i in range(1, len(depth_list)-2):
        next_three_measurement_sum = sum(depth_list[i:i+3])
        print(next_three_measurement_sum)
        if next_three_measurement_sum > curr_num_to_check:
            num_times_increase += 1
        curr_num_to_check = next_three_measurement_sum
    return num_times_increase
        

total_depth_increase = get_depth_increase_by_three_measurement(file_input='./input')
