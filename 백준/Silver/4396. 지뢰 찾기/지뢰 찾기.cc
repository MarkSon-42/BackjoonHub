#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    
    int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
    
    vector<vector<char>> boom(n, vector<char>(n));
    vector<vector<char>> map(n, vector<char>(n));
    vector<vector<char>> ans(n, vector<char>(n, '.'));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> boom[i][j];
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }
    
    bool game_over = false;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (map[i][j] == 'x') {
                if (boom[i][j] == '*') {
                    game_over = true;
                } else {
                    int count = 0;
                    for (int k = 0; k < 8; k++) {
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        if (nx >= 0 && nx < n && ny >= 0 && ny < n && boom[nx][ny] == '*') {
                            count++;
                        }
                    }
                    ans[i][j] = count + '0';
                }
            }
        }
    }
    
    if (game_over) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (boom[i][j] == '*') {
                    ans[i][j] = '*';
                }
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << ans[i][j];
        }
        cout << endl;
    }
    
    return 0;
}