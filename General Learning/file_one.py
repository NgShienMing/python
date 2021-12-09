import file_two

print("File one __name__ is set to %s" % __name__)

if __name__ == "__main__":
    print("File one is executed directly")
else:
    print("File one is executed when imported")