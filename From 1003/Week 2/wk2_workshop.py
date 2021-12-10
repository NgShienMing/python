"""Week 2 Workshop"""
# Q1
def power(num_arr: list, expo: int):
    """Calculate the power of an array of number"""
    for num in num_arr:
        pow_num = num**expo
        print(f"{num}: {pow_num}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
POWER = 5
power(numbers, POWER)

print("\n")

# Q2
def multiplication_table(min_id: int, max_id: int, min_series: int, max_series):
    """Generate a multiplication table"""
    product = 0
    for series in range(min_series, max_series + 1):
        for index in range(min_id, max_id + 1):
            product = index*series
            print(f"{index} X {series} = {product}")
        print()

MIN_ID = 1
MAX_ID = 12
MIN_SERIES = 1
MAX_SERIES = 12
multiplication_table(MIN_ID, MAX_ID, MIN_SERIES, MAX_SERIES)
