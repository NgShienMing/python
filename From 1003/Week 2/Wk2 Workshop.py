# Q1
def power(num_arr: list, power: int):
    for i in range(len(num_arr)):
        number = num_arr[i]**power
        print("{}: {}" .format(num_arr[i], number))

num_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
POWER = 5
power(num_arr, POWER)

print("\n")

# Q2
def multiplication_table(min_ID: int, max_ID: int, min_series: int, max_series):
    product = 0
    for series in range(min_series, max_series + 1):
        for index in range(min_ID, max_ID + 1):
            product = index*series
            print("{} X {} = {}" .format(index, series, product))
        print()

MIN_ID = 1;
MAX_ID = 12;
MIN_SERIES = 1;
MAX_SERIES = 12;
multiplication_table(MIN_ID, MAX_ID, MIN_SERIES, MAX_SERIES)