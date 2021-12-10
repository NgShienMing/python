# Q1
def findMostChar(str: str):
    countObj = {}
    for char in str:
        if (char in countObj):
            countObj[char] += 1
        else:
            countObj[char] = 1
    maxCount = 0
    maxChar = []
    for key in countObj.keys():
        if (countObj[key] > maxCount):
            maxCount = countObj[key]
            maxChar = []
            maxChar.append(key)
        elif (countObj[key] == maxCount):
            maxChar.append(key)
    return maxChar

str1 = "apple"
str2 = "prettier"
str3 = "behaviour"
print(findMostChar(str1))
print(findMostChar(str2))
print(findMostChar(str3))

# Q2
def anagram1(str1: str, str2: str):
    if (len(str1) != len(str2)):
        return ("{} and {} are not anagrams" .format(str1, str2))
    else:
        Str1 = "".join(sorted(str1))
        Str2 = "".join(sorted(str2))
        if (Str1 == Str2):
            return ("{} and {} are anagrams" .format(str1, str2))
        else:
            return ("{} and {} are not anagrams" .format(str1, str2))

def anagram2(str1: str, str2: str):
    if (len(str1) != len(str2)):
        return "{} and {} are not anagrams" .format(str1, str2)
    else:
        countObj1 = {}
        countObj2 = {}
        for char in str1:
            if (char in countObj1):
                countObj1[char] += 1
            else:
                countObj1[char] = 1
        for char in str2:
            if (char in countObj2):
                countObj2[char] += 1
            else:
                countObj2[char] = 1

        flag = True
        for key in countObj1:
            if (countObj2.get(key)):
                if (countObj1[key] != countObj2[key]):
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
def reverseNum(num: int):
    reverseNumber = 0
    while (num > 0):
        remainder = num % 10
        reverseNumber = reverseNumber*10 + remainder
        num = math.floor(num / 10)
    return reverseNumber

num = 9278
print(reverseNum(num))

# Q4
def isPrime(num):
    flag = True
    for i in range(2,num):
        if (num % i == 0):
            flag = False
            break
    if (flag):
        return "{} is a prime number" .format(num)
    else:
        return "{} is not a prime number" .format(num)
prime = 16777216
print(isPrime(prime))

# Q5
def isPalindrome(word: str):
    lowercaseWord = word.lower()
    for i in range(math.floor(len(word)/2)):
        j = len(word) - 1 - i
        if (lowercaseWord[i] != lowercaseWord[j]):
            return "{} is not a palindrome" .format(word)
    return "{} is a palindrome" .format(word)

wordArr = ["racecar", "RACEcar", "Madam", "Acrobat", "9360639"]
for i in range(len(wordArr)):
    word = wordArr[i]
    print(isPalindrome(word))