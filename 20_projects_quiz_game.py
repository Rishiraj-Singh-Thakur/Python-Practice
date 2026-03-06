questions = [
["Who is Virat Kohli?", "a","b","c","d","a"]
]

for q in questions:

    print(q[0])

    answer = input("Enter answer: ")

    if answer == q[5]:
        print("Correct")
    else:
        print("Wrong")