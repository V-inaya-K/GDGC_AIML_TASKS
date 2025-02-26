#TRY1- Getting errors hence rejected
# def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
# 	means=[[sum(for element in row)/3]for row in matrix]
# 	return means
# def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
# 	if mode == 'row':
#         means=[sum(row) / len(row) for row in matrix]
#         return means
#     elif mode == 'column':
#         nRows = len(matrix)
#         nCols = len(matrix[0]) if matrix else 0  

#         means=[sum(matrix[row][col] for row in range(nRows)) / nRows for col in range(nCols)]
# 		return means

#TRY-2 WORKING
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'row':
        means = [sum(row) / len(row) for row in matrix] #To find average of each row elements
        return means #mean returned and exit function

    elif mode == 'column':
        nRows = len(matrix) #length of row
        nCols = len(matrix[0]) if len(matrix) > 0 else 0 #length of column by accessing 0th element of matrix and finding its length.

        means = [sum(matrix[row][col] for row in range(nRows)) / nRows for col in range(nCols)]
        return means #mean returned and exit function
