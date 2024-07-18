def GraphMatrix():
    while True:
        try:
            # Get the number of vertices (n) from the user
            n = int(input('Enter the number of vertices (an integer from 2 to 5): '))
            if 2 <=n <= 5:
                break
            else:
                print('Invalid input. Please enter a number between 2 and 5')
        except ValueError:
            print('Invalid input. Please enter an integer')

    # Initialize an empty n x n adjacency matrix with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    print(f'Enter {2 * n} triplets of edges '
          f'composed by three Integers i, j, w (origin, destination, weight): ')

    for _ in range(2 * n):
        while True:
            try:
                i, j, w = map(int, input('Enter the triplet (i j w): ').split())
                if 0 <= i < n and 0 <= j < n:
                    matrix[i][j] = w
                    break
                else:
                    print(f'Invalid vertex indices. Please enter values between 0 and {n - 1}.')
            except ValueError:
                print('Invalid input. Please enter three integers separated by spaces.')

        # Print the resulting adjacency matrix
        print('The adjacency matrix is: ')
        for row in matrix:
            print(' '.join(map(str, row)))  # Print each row with spaces

# Call the function to start the program
GraphMatrix()

