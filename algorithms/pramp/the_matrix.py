M = [[1, 2, 3, 4, 5], 
	 [6, 7, 8, 8, 10],
	 [11, 12, 13, 14, 15],
	 [16, 17, 18, 19, 20]]
# print(len(m[0]))


def spiral_matrix_print(m):
	top_row = 0
	btm_row = len(m) - 1
	left_col = 0
	right_col = len(m[0]) -1

	# for i in range(len(m[0])):
	# 	print m[0][i]

	while left_col <= right_col:
		#print the next top row
		for i in range(0, 5):
			print m[0][i]
		top_row += 1

		for i in range(1, 4):
			print m[i][4]
		right_col -= 1

		if (top_row <= btm_row):
			for i in reversed(range(0, 4)):
				print m[3][i]
			btm_row -= 1

		if (left_col <= right_col):
			for i in reversed(range(2, 1)):
				print m[i][0]
				print "AJKAJKJ"
			left_col += 1

# matrixSpiralPrint


def pramp():
   print "Practice Makes Perfect"

pramp()

def matrixSpiralPrint(M):
   rows = len(M)
   cols = len(M[0])
   if rows == 0:
      return None
   for depth in xrange(min(rows,cols)/2):
      for n in xrange(depth, cols - depth):
         print M[depth][n]
      for e in xrange(depth + 1, rows - depth):
         print M[e][cols-depth-1]
      for s in xrange(cols - depth - 2, depth - 1, -1):
         print M[rows-depth-1][s]
      for w in xrange(rows - depth - 2, depth, -1):
         print M[w][depth]
         
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
8
14
13
12

print(matrixSpiralPrint(M))