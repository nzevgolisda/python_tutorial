
# dataTypes
  # word: string
  # wordAsList: array
  # n: integer

word = 'hey' # variable word assigned the string (str) value 'hey'
wordAsList = list(word) # variable wordAsList is an array of characters
n = len(wordAsList) # variable n is the number of characters, as the length of the list

# FOR LOOP 
for i in range(n):
    print(word[i])
for i in range(0, n, 1):
    print(word[i])

for letter in word: # variable letter assigned by the str in word's letter order
    print(letter)
for letter in wordAsList:
    print(letter)


for i in range(n):
    print(wordAsList[i])

# range(n) = [0, 1, 2, 3, ..., n-2, n-1]
# count(n) = [1, 2, 3, 4, ..., n-1, n]
#As we see, we count from 0 to n-1, but still have n options
# range(n) = range(0, n, 1)
#So from 0 to n-1 by step 1 

# SIMPLE HANGMAN

solution = [] # This will be the unmade wordAsList variable ...
for i in range(n):
    solution.append('_ ')
s = '' # ... while this will be the word variable respectively as above
for i in range(n):
    s = s + solution[i]
    # s += solution[i]
print(s)

