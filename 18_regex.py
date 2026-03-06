import re

text = "The quick brown fox"

match = re.search("brown", text)

if match:
    print("Match Found")