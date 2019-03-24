a = [[0, 1, 0],
	[1, 0, 0],
	[0, 1, 1]]

# def diagonal_sum(array_2d):
# 	total = 0
# 	for i in range(len(array_2d)):
# 		total += array_2d[i][i]
# 	return total

# print(diagonal_sum(a))


def can_attack(board):
	# horisontals = []
	# verticals = []
	# for i in range(len(board)):
	# 	print(board[i])
	# 	for square in board[i]:
	# 		print(square)
	# 		if square == 1:
	# 			print("Found a figure")
	# 			horisontals.append(square)
	# 		if len(horisontals) > 1:
	# 			return True
	# 	horisontals = []
	# 	print("==========")

	n = len(board)
	print(range(n))

	for row_i in range(n):
		row_count = 0
		for col_i in range(n):
			row_count += board[row_i][col_i]
			print(row_count)
		if row_count > 1:
			return True

	return False

print(can_attack(a))

a = [1, 2, 3]

seen = {}
for n in a:
	if n in seen:
		print("Yep")
	else:
		seen[n] = 1
