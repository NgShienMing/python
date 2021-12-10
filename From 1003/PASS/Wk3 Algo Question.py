# Q1
def find_most_char(str: str):
    count_obj = {}
    for char in str:
        if (char in count_obj):
            count_obj[char] += 1
        else:
            count_obj[char] = 1
    max_count = 0
    max_char = []
    for key in count_obj.keys():
        if (count_obj[key] > max_count):
            max_count = count_obj[key]
            max_char = []
            max_char.append(key)
        elif (count_obj[key] == max_count):
            max_char.append(key)
    return max_char

str1 = "apple"
str2 = "prettier"
str3 = "behaviour"
print(find_most_char(str1))
print(find_most_char(str2))
print(find_most_char(str3))

# Q2
def anagram1(str1: str, str2: str):
    if (len(str1) != len(str2)):
        return ("{} and {} are not anagrams" .format(str1, str2))
    else:
        sorted_str1 = "".join(sorted(str1))
        sorted_str2 = "".join(sorted(str2))
        if (sorted_str1 == sorted_str2):
            return ("{} and {} are anagrams" .format(str1, str2))
        else:
            return ("{} and {} are not anagrams" .format(str1, str2))

def anagram2(str1: str, str2: str):
    if (len(str1) != len(str2)):
        return "{} and {} are not anagrams" .format(str1, str2)
    else:
        count_obj1 = {}
        count_obj2 = {}
        for char in str1:
            if (char in count_obj1):
                count_obj1[char] += 1
            else:
                count_obj1[char] = 1
        for char in str2:
            if (char in count_obj2):
                count_obj2[char] += 1
            else:
                count_obj2[char] = 1

        flag = True
        for key in count_obj1:
            if (count_obj2.get(key)):
                if (count_obj1[key] != count_obj2[key]):
                    flag = False
                    break
            else:
                flag = False
                break
        if (flag):
            return "{} and {} are anagrams" .format(str1, str2)
        else:
            return "{} and {} are not anagrams" .format(str1, str2)

str1 = "listen"
str2 = "silent"
str3 = "teal"
str4 = "tail"
print(anagram1(str1, str2))
print(anagram2(str1, str2))
print(anagram1(str3, str4))
print(anagram2(str3, str4))

# Q3
import math
def reverse_num(num: int):
    reverse_number = 0
    while (num > 0):
        remainder = num % 10
        reverse_number = reverse_number*10 + remainder
        num = math.floor(num / 10)
    return reverse_number

num = 9278
print(reverse_num(num))

# Q4
def is_prime(num):
    flag = True
    for i in range(2, num):
        if (num % i == 0):
            flag = False
            break
    if (flag):
        return "{} is a prime number" .format(num)
    else:
        return "{} is not a prime number" .format(num)

prime = 16777216
print(is_prime(prime))

# Q5
def is_palindrome(word: str):
    lowercase_word = word.lower()
    for i in range(math.floor(len(word)/2)):
        j = len(word) - 1 - i
        if (lowercase_word[i] != lowercase_word[j]):
            return "{} is not a palindrome" .format(word)
    return "{} is a palindrome" .format(word)

word_list = ["racecar", "RACEcar", "Madam", "Acrobat", "9360639"]
for i in range(len(word_list)):
    word = word_list[i]
    print(is_palindrome(word))