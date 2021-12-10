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

print(findMostChar("apple"))
print(findMostChar("prettier"))
print(findMostChar("behaviour"))

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

print(anagram1("listen", "silent"))
print(anagram2("listen", "silent"))
print(anagram1("teal", "tail"))
print(anagram2("teal", "tail"))

# Q3
import math
def reverseNum(num: int):
    reverseNumber = 0
    while (num > 0):
        remainder = num % 10
        reverseNumber = reverseNumber*10 + remainder
        num = math.floor(num / 10)
    return reverseNumber

print(reverseNum(9278))

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

print(isPrime(8388608))

# Q5
def isPalindrome(word: str):
    word = word.lower()
    for i in range(math.floor(len(word)/2)):
        j = len(word) - 1 - i
        if (word[i] != word[j]):
            return "{} is not a palindrome" .format(word)
    return "{} is a palindrome" .format(word)

print(isPalindrome("racecar"))