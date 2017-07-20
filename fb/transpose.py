def transpose_matrix(matrix):
    rows = len(matrix)
    col = len(matrix[0])

    for i in xrange(rows):
    	for j in xrange(col):
    		temp = matrix[i][j]
    		matrix[i][j] = matrix[j][i]
    		matrix[j][i] = temp

	print matrix

transpose_matrix([[1, 0, 1], [1, 0, 1], [1, 0, 1]])
