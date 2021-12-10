"""Learning if __name__ == "__main__" check"""
import file_two

print(f"File one __name__ is set to {__name__}")

if __name__ == "__main__":
    print("File one is executed directly")
else:
    print("File one is executed when imported")

file_two.greet()
