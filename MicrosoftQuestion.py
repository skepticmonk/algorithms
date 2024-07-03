def solution(board):
    n = len(board);
    m = len(board[0]);
    dp_A = [[0] * (m) for _ in range(n)];
    dp_B = [[0] * (m) for _ in range(n)];
    for i in range(n):
        for j in range(m):
            if(i== 0 and j ==0):
                dp_A[i][j] = (1 if board[i][j] == 'A' else 0);
                dp_B[i][j] = (1 if board[i][j] == 'B' else 0);
            elif(i ==0):
                dp_A[i][j] = dp_A[i][j-1] + (1 if board[i][j] == 'A' else 0);
                dp_B[i][j] = dp_B[i][j-1] + (1 if board[i][j] == 'B' else 0);
            elif(j ==0):
                dp_A[i][j] = dp_A[i-1][j] + (1 if board[i][j] == 'A' else 0);
                dp_B[i][j] = dp_B[i-1][j] + (1 if board[i][j] == 'B' else 0);
            else:
                dp_A[i][j] = abs(dp_A[i-1][j] + dp_A[i][j-1]- 2*dp_A[i-1][j-1] + (1 if board[i][j] == 'A' else 0));
                dp_B[i][j] = abs(dp_B[i-1][j] +dp_B[i][j-1] - 2*dp_B[i-1][j-1]+ (1 if board[i][j] == 'B' else 0));

    def get_sum(dp, r1, c1, r2, c2):
        return abs(dp[r1][c1] + dp[r2][c2] - dp[r1][c2] - dp[r2][c1])
    count = 0;
    print(dp_A)
    print(dp_B)
    for i in range(n):
        for j in range(m):
            numA = get_sum(dp_A, 0, 0, i, j);
            numB = get_sum(dp_B, 0, 0, i, j);
            print(i, j, numA, numB)
            if(numA == numB):
                count += 1;
    return count;


board = ["AB.", "B..", "..A"]
print(solution(board));