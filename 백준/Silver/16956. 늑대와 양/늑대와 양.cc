#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int r, c;
vector<vector<char>> matrix;
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

bool is_valid(int x, int y) {
    return x >= 0 && x < r && y >= 0 && y < c;
}

bool bfs() {
    queue<pair<int, int>> q;
    
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (matrix[i][j] == 'W') {
                q.push({i, j});
            }
        }
    }
    
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (is_valid(nx, ny)) {
                if (matrix[nx][ny] == 'S') {
                    return false; 
                }
                if (matrix[nx][ny] == '.') {
                    matrix[nx][ny] = 'D';
                }
            }
        }
    }
    
    return true;
}

int main() {
    cin >> r >> c;
    matrix.resize(r, vector<char>(c));
    
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cin >> matrix[i][j];
        }
    }
    
    bool is_safe = bfs();
    
    if (is_safe) {
        cout << "1\n";
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                cout << matrix[i][j];
            }
            cout << "\n";
        }
    } else {
        cout << "0\n";
    }
    
    return 0;
}