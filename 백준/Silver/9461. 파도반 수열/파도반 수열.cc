#include <iostream>

#define MAX_N 1000

using namespace std;



int main() {
    int t;
    cin >> t;


    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;

        long long dp[MAX_N] = {};

        dp[1] = 1;
        dp[2] = 1;
        dp[3] = 1;

        for(int j = 4; j <= n; j++) {
            dp[j] = dp[j - 2] + dp[j - 3];
        }
        cout << dp[n] << '\n';
    }
    return 0;
}