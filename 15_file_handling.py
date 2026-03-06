with open("sample.txt", "w") as f:
    f.write("Python practice file")


with open("sample.txt", "r") as f:
    print(f.read())