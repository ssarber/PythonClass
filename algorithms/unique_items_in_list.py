a = [1,2,3,4,55,]
b = [1,2,3,4,5,6,6]


# merge the lists and convert them to  set, and eliminate the duplicates
merged_list = a + b
merged_set = set(merged_list)
# merged_set = first_words_set.union(last_words_set)

print('\n\n' + 'There are {} unique words in both lists:'.format(len(merged_set)) + '\n')
print(merged_set)
