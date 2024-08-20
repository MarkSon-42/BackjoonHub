#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> board(n, vector<int>(n));
    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    // 2^63 - 1 이하라서 long long 사용

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }

    // DP 배열 초기화: dp[i][j]는 (i,j)에 도달하는 경로의 수를 저장
    // 시작점 초기화
    dp[0][0] = 1;

    // DP 진행
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dp[i][j] == 0 || board[i][j] == 0) continue; 
            // 도달할 수 없는 칸이거나 종착점

            int jump = board[i][j];
            
            // 오른쪽으로 점프
            if (j + jump < n) {
                dp[i][j + jump] += dp[i][j];
            }
            
            // 아래로 점프
            if (i + jump < n) {
                dp[i + jump][j] += dp[i][j];
            }
        }
    }

    cout << dp[n-1][n-1] << endl;

    return 0;
}