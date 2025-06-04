def write():
    file_w = open("output.txt","w")
    writing = input("Enter text to write to the file: ")
    file_w.write(writing + "\n")
    print("Data successfully written to output.txt.\n")
    file_w.close()

def append():
    file_a = open("output.txt","a")
    appending = input("Enter additional text to append: ")
    file_a.write(appending + "\n")
    print("Data successfully appended.\n")
    file_a.close()

def read():
    file_r = open("output.txt","r")
    print("Final content of output.txt:")
    lines = file_r.readlines()
    for line in lines:
        print(line)
    file_r.close()

write()
append()
read()