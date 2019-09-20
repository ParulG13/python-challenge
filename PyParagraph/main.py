import csv
import os
import re

input_file = "paragraph_1.txt"

with open(input_file, 'r')as file:
    file_read = file.read()
    #regex need correction
    wordCount = len(re.findall(r'\w+',file_read))
    sentenceCount = file_read.count('.')
    letterCount = len(file_read)
    averageLength = wordCount / sentenceCount
    averageCount = letterCount / wordCount

# print analysis
print("Paragraph Analysis")
print("---------------------")
print("Approximate Word Count: " + str(wordCount))
print('Approximate Sentence Count:' + str(sentenceCount))
print('Average Letter Count: {:.1f}'.format(averageCount))
print('Average Sentence Length: {:.1f}'.format(averageLength))

