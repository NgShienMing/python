"""Drawing shapes by printing *"""
def cross(size: int):
    """Draw a cross"""
    arr = ["*"]*size
    front = 0
    back = size - 1
    output = ""
    while not front == size and not back == -1:
        for i in range(size):
            arr[i] = " "
        arr[front] = "*"
        arr[back] = "*"
        for j in range(size):
            output += arr[j]
        output += "\n"
        front += 1
        back -= 1
    print(output)
cross(7)
