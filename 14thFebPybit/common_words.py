"""
Bite 272. Find common words
Given two sentences that each contains words in case insensitive way, you have to check the common case insensitive words appearing in both sentences.

If there are duplicate words in the results, just choose one. The results should be sorted by words length.

The sentences are presented as list of words. Example:

S = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything']
##                  **                       **
T = ['We', 'are', 'what', 'we', 'repeatedly', 'do', 'is', 'not', 'an', 'act']
##                                             **          **
Result = ['do', 'not']
"""
S = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything','not']
T = ['We', 'are', 'what', 'we', 'repeatedly', 'do', 'is', 'not', 'an', 'act']

Result = set()

for i in S:
    for j in T:
        if i == j:
            Result.add(i)

print(Result)