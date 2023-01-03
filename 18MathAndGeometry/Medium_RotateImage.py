def rotate(matrix):
    l, r = 0, len(matrix) - 1  # We know that matrix has same length in row and columns as n x n therefor instead of len(
                               # matrix[0]) - 1 -> len(matrix) - 1

    while l < r:
        for i in range(r - l):  # Iterate throw entire row except last one
            top, bottom = l, r

            # Save the top left
            top_left = matrix[top][l + i]

            # Move the bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # Move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # Move top right into top bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # Move top left into top right
            matrix[top + i][r] = top_left

        l += 1
        r -= 1


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)  # [[7,4,1], [8,5,2], [9,6,3]]
