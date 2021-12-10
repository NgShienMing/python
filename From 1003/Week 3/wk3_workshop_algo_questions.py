"""Week 3 Coding"""
# Q1
def find_number(digit, data):
    """Find the numbers in data that meet the criteria"""
    numbers_meeting_criteria = []
    for number in data:
        num_str = str(number)
        if len(num_str) == digit:
            digits = list(num_str)
            digit_sum = 0
            for string in digits:
                num = int(string)
                digit_sum += num
            if digit_sum < 10:
                numbers_meeting_criteria.append(number)
    return numbers_meeting_criteria

DIGIT = 3
numbers = [
    1590, 276, 580, 246, 5005, 3315, 6595, 9788, 223, 6613,
    2836, 3891, 6204, 7035, 401, 912, 662, 123, 472, 428, 8507,
    9259, 78, 1817, 8075, 3581, 3669, 680, 740, 2569, 0, 7827,
    2402, 8311, 1955, 453, 9014, 402, 8323, 6941, 692, 8565,
    3568, 3471, 4916, 807, 3610, 938, 633, 743
]
print(find_number(DIGIT, numbers))

#Q2
def sort_positive_negative(num_arr):
    """Sort the array of numbers into positive numbers and negative numbers"""
    sorted_numbers = {
        "positive_number": [],
        "negative_number": []
    }
    for number in num_arr:
        if number > 0:
            sorted_numbers["positive_number"].append(number)
        else:
            sorted_numbers["negative_number"].append(number)
    return sorted_numbers

pos_neg = [
	372, -659, 339, -781, 351, 531, 709, 16, -899, -18, -649,
	907, 769, -666, 884, -475, 45, 225, -188, -50, -449, 483,
	978, 837, -724, 131, -365, -984, -601, -526, 346, -665,
	188, 273, 979, -62, 513, 995, -536, 276, -934, -110, 931,
	-170, -680, -468, 810, 21, 922, -968, -391, 6, 246, 759,
	-114, -457, -603, -132, -880, -23, 164, -494, -61, 676,
	-941, 788, -911, 449, -708, 989, 833, 621, -389, -197, -53,
	-52, 215, -898, 795, -487, 109, 257, 293, -500, 852, 195,
	-348, -954, 970, 501, -870, 653, 564, 522, -948, -793, 796,
	-913, 617, -756
]
print(sort_positive_negative(pos_neg))
