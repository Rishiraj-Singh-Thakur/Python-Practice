# read file

file = open("my.txt" , "r")
content = file.read()
print(content)

file.close()

# write a content in file using write() , it clean all content of file

# file = open("my.txt" , "w")

# content = "did practice on me"

# file.write(content)
# file.close()

# Append the file

file = open("my.txt" , "a")

content = "I am a para for practice the append method of python "

file.write(content)
