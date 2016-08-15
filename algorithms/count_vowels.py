vowels = ['a', 'e', 'i', 'o']
 
word = 'iuewinxjnaaa'
count = 0
for letter in word:
    if letter in vowels:
        count = count + 1
         
print count