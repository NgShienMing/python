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
print("Mark: {}" .format(result[0]["units"][2]["mark"]))

# Q2
mark = 80
if (mark >= 0 and mark <= 100):
    print("Valid result")

# Q3
spiders = 1;
while(spiders < 10):
    if (spiders == 1):
        print("There is {} spider!" .format(spiders))
    else:
        print("There are {} spiders!" .format(spiders))
    spiders += 1

# Q4
data = [
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
];
sortedData = {
    "integer": [],
    "string": [],
    "boolean": []
}
for i in range(len(data)):
    if (type(data[i]) == int):
        sortedData["integer"].append(data[i])
    elif(type(data[i]) == str):
        sortedData["string"].append(data[i])
    elif(type(data[i]) == bool):
        sortedData["boolean"].append(data[i])
print(sortedData)

# Q5
numData = [7976, 5580, 4832, 2520, 3089, 6275, 9894, 3850, 2760, 1078, 2691, 8934, 1152, 4335, 7212, 7524, 4797, 5016, 3996, 8310]
largestNumber = numData[0]
smallestNumber = numData[0]
for i in range(len(numData)):
    if (numData[i] > largestNumber):
        largestNumber = numData[i]
    elif (numData[i] < smallestNumber):
        smallestNumber = numData[i]
print("Largest number = {}\nSmallest number = {}" .format(largestNumber, smallestNumber))

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
sortedNum = {
    "odd": [],
    "even": []
}
for i in range(len(odd_even)):
    if (odd_even[i] % 2 == 0):
        sortedNum["even"].append(odd_even[i])
    else:
        sortedNum["odd"].append(odd_even[i])
print(sortedNum)

# Q7
import numpy as np
LIMIT = 50
list = []
while (len(list) < LIMIT):
    num = np.random.rand() * 100
    list.append(round(num, 2))
print(list)