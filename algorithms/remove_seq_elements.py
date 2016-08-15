def remove_seq_elements(seq, elements):
	return [x for x in seq if x not in elements]

my_str = 'abracadabra'

print(remove_seq_elements(my_str, 'ab'))