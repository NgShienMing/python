"""Iterators"""
# Tuple
mytuple = ("apple", "banana", "cherry")
myit_tuple = iter(mytuple)

print(next(myit_tuple))
print(next(myit_tuple))
print(next(myit_tuple))
print("\n")

for x in mytuple:
    print(x)
print("\n")

# String
mystr = "banana"
myit_str = iter(mystr)

print(next(myit_str))
print(next(myit_str))
print(next(myit_str))
print(next(myit_str))
print(next(myit_str))
print(next(myit_str))
print("\n")

for x in mystr:
    print(x)
print("\n")

# Create an Iterator using Class
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
