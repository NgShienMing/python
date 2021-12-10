"""Week 2 Workshop Quiz"""
import numpy as np
# Q1
result = [
    {
        "year": 2021,
        "sem": 1,
        "units": [
            {
                "code": "ENG1001",
                "grade": "HD",
                "mark": 83
            },
            {
                "code": "ENG1005",
                "grade": "HD",
                "mark": 84
            },
            {
                "code": "ENG1060",
                "grade": "HD",
                "mark": 90
            },
            {
                "code": "PHS1002",
                "grade": "HD",
                "mark": 83
            }
        ]
    }
]

ENG1060_MARK = result[0]["units"][2]["mark"]
print(f"Mark: {ENG1060_MARK}")

# Q2
MARK = 80
if 0 <= MARK <= 100:
    print("Valid result")

# Q3
SPIDERS = 1
while SPIDERS < 10:
    if SPIDERS == 1:
        print(f"There is {SPIDERS} spider!")
    else:
        print(f"There are {SPIDERS} spiders!")
    SPIDERS += 1

# Q4
data_arr = [
    506, False, "164", 514, 135, 547, "18", 743, 838, 313, 885,
    652, False, False, "949", 353, 855, "963", 368, False,
    "179", 706, "189", 573, "744", 149, "266", True, True,
    "781", False, 224, "643", 176, False, "845", 465, 235, 968,
    302, "238", "755", 959, "540", 249, 622, "547", "193", 158,
    True, "177", True, "582", "427", False, "849", 418, "545",
    True, "990", "497", "724", False, 544, 141, False, "102",
    183, 633, "847", 992, 271, 835, 551, "972", 574, False,
    271, False, 810, 54, True, True, 513, 13, False, 268,
    "418", 77, 707, "936", False, False, 628, 932, False, 319,
    148, "207", False
]
sorted_data = {
    "integer": [],
    "string": [],
    "boolean": []
}
for data in data_arr:
    if isinstance(data, bool):
        sorted_data["boolean"].append(data)
    elif isinstance(data, str):
        sorted_data["string"].append(data)
    elif isinstance(data, int):
        sorted_data["integer"].append(data)
print(sorted_data)

# Q5
num_data = [
    7976, 5580, 4832, 2520, 3089, 6275, 9894, 3850, 2760, 1078,
    2691, 8934, 1152, 4335, 7212, 7524, 4797, 5016, 3996, 8310
]
LARGEST_NUMBER = num_data[0]
SMALLEST_NUMBER = num_data[0]
for num in num_data:
    if num > LARGEST_NUMBER:
        LARGEST_NUMBER = num
    elif num < SMALLEST_NUMBER:
        SMALLEST_NUMBER = num
print(f"Largest number = {LARGEST_NUMBER}\nSmallest number = {SMALLEST_NUMBER}")

# Q6
odd_even = [
    -151, 497, 920, -849, -473, -213, 365, -338, -23, -712,
    161, 595, -914, 157, -768, 64, 749, 781, 539, -201, -377,
    -85, 267, 230, -197, 616, -605, 669, -133, -36, -65, -794,
    -146, -440, -79, 867, 533, 341, -982, 181, 975, -958, -562,
    -707, 130, 730, -86, 769, 47, 658, -68, -470, 619, -797,
    259, -572, -455, 454, -780, 145, 668, 489, -840, 380, 974,
    25, 89, -573, -539, 892, 457, 295, 936, -847, -282, 905,
    973, -918, -684, -942, -129, 26, -15, -678, 158, 421, -229,
    -32, 426, -836, 923, -442, 736, -984, -547, 582, 797, 209,
    -784, -842
]
sorted_num = {
    "odd": [],
    "even": []
}
for num in odd_even:
    if num % 2 == 0:
        sorted_num["even"].append(num)
    else:
        sorted_num["odd"].append(num)
print(sorted_num)

# Q7
LIMIT = 50
num_list = []
while len(num_list) < LIMIT:
    num = np.random.rand()*100
    num_list.append(round(num, 2))
print(num_list)
