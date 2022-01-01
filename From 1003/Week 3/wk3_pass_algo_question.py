"""Week 3 Algorithm Questions"""
import math
# Q1
def find_most_char(string: str):
    """Find the character that appear most in a word"""
    count_obj = {}
    for char in string:
        if char in count_obj:
            count_obj[char] += 1
        else:
            count_obj[char] = 1
    max_count = 0
    max_char = []
    for item in count_obj.items():
        if item[1] > max_count:
            max_count = item[1]
            max_char = []
            max_char.append(item[0])
        elif item[1] == max_count:
            max_char.append(item[0])
    return max_char

WORD1 = "apple"
WORD2 = "prettier"
WORD3 = "behaviour"
print(find_most_char(WORD1))
print(find_most_char(WORD2))
print(find_most_char(WORD3))

# Q2
def anagram1(str1: str, str2: str):
    """Check whether the two strings are anagrams"""
    if len(str1) != len(str2):
        output = f"{str1} and {str2} are not anagrams"
    else:
        sorted_str1 = "".join(sorted(str1))
        sorted_str2 = "".join(sorted(str2))
        if sorted_str1 == sorted_str2:
            output = f"{str1} and {str2} are anagrams"
        else:
            output = f"{str1} and {str2} are not anagrams"
    return output

def anagram2(str1: str, str2: str):
    """Check whether the two strings are anagrams"""
    if len(str1) != len(str2):
        output = f"{str1} and {str2} are not anagrams"
    else:
        count_obj1 = {}
        count_obj2 = {}
        for char in str1:
            if char in count_obj1:
                count_obj1[char] += 1
            else:
                count_obj1[char] = 1
        for char in str2:
            if char in count_obj2:
                count_obj2[char] += 1
            else:
                count_obj2[char] = 1

        flag = True
        for item in count_obj1.items():
            if count_obj2.get(item[0]):
                if item[1] != count_obj2[item[0]]:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            output = f"{str1} and {str2} are anagrams"
        else:
            output = f"{str1} and {str2} are not anagrams"
    return output

STR1 = "listen"
STR2 = "silent"
STR3 = "teal"
STR4 = "tail"
print(anagram1(STR1, STR2))
print(anagram2(STR1, STR2))
print(anagram1(STR3, STR4))
print(anagram2(STR3, STR4))

# Q3
def reverse_num(num: int):
    """Reverse the given number"""
    reverse_number = 0
    while num > 0:
        remainder = num % 10
        reverse_number = reverse_number*10 + remainder
        num = math.floor(num / 10)
    return reverse_number

NUMBER = 9278
print(reverse_num(NUMBER))

# Q4
def is_prime(num):
    """Check whether the number is a prime number"""
    flag = True
    for i in range(2, math.floor(math.sqrt(num))+1):
        if num % i == 0:
            flag = False
            break
    if flag:
        output = f"{num} is a prime number"
    else:
        output = f"{num} is not a prime number"
    return output

PRIME = 16777216
print(is_prime(PRIME))

# Q5
def is_palindrome(string: str):
    """Check whether the word is a palindrome"""
    lowercase_word = string.lower()
    for i in range(math.floor(len(string)/2)):
        j = len(string) - 1 - i
        if lowercase_word[i] != lowercase_word[j]:
            return f"{string} is not a palindrome"
    return f"{string} is a palindrome"

word_list = ["racecar", "RACEcar", "Madam", "Acrobat", "9360639"]
for word in word_list:
    print(is_palindrome(word))
