try:
    n = 0
    file = open("sample.txt", "r")
    lines = file.readlines()
    for line in lines:
        n += 1
        print("Line {}: ".format(n), line)
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")