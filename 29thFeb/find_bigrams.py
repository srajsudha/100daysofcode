"""
Write a function called find_bigrams that takes a sentence or paragraph of strings and returns a list of all its bigrams in order.

Note: A bigram is a pair of consecutive words.

"""

sentence ="Have free hours and love children? Drive kids to school, soccer practice and other activities."

sentence_split = sentence.lower().split()
# print(sentence_split)

bigram_list =[]

for i in range(len(sentence_split)-1):
    bigram_list.append((sentence_split[i],sentence_split[i+1]))

print(bigram_list)