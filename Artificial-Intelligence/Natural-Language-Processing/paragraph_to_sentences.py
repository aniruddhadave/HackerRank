# Breaks paragraphs into its constituent sentences

# Link: https://www.hackerrank.com/challenges/from-paragraphs-to-sentences/problem

# Imports
import sys,re

# Trim whitespaces and add an extra
paragraph = input().rstrip()+' '
while True:
    # Search for more than two characters followed by
    # [.?!] followed by a Capital Letter
    x = re.search(r'(.{2,}?)([\.\?\!])([\sA-Z])', paragraph)
    if not x:
        break
    sentence = x.group(1)+x.group(2)
    print(sentence)
    next_index = len(sentence)
    paragraph=paragraph[next_index:]