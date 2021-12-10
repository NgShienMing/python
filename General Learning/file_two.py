"""Learning if __name__ == "__main__" check"""
print(f"File two __name__ is set to {__name__}")

if __name__ == "__main__":
    print("File two is executed directly")
else:
    print("File two is executed when imported")

def greet():
    """Greet the user"""
    print("Hello user, welcome to Python!")
