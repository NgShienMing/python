# Q1
def power(numArr: list, power: int):
    for i in range(len(numArr)):
        number = numArr[i]**power
        print("{}: {}" .format(numArr[i], number))

numArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
POWER = 5
power(numArr, POWER)

print("\n")

# Q2
def multiplicationTable(minID: int, maxID: int, minSeries: int, maxSeries):
    product = 0
    for series in range(minSeries, maxSeries + 1):
        for index in range(minID, maxID + 1):
            product = index*series
            print("{} X {} = {}" .format(index, series, product))
        print()

MIN_ID = 1;
MAX_ID = 12;
MIN_SERIES = 1;
MAX_SERIES = 12;
multiplicationTable(MIN_ID, MAX_ID, MIN_SERIES, MAX_SERIES)