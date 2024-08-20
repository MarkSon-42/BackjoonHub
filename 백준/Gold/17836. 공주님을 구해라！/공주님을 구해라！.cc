#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N, M, T;
vector<vector<int>> _map;
vector<vector<bool>> visited;
vector<vector<int>> dist;

int bfs() {
    queue<pair<int, int>> q;
    q.push({0, 0});
    visited[0][0] = true;
    
    int sword_x = -1, sword_y = -1;
    int princess_dist = -1;
    
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        if (x == N-1 && y == M-1) {
            princess_dist = dist[x][y];
            break;
        }
        
        if (_map[x][y] == 2) {
            sword_x = x;
            sword_y = y;
        }
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (_map[nx][ny] == 1 || visited[nx][ny]) continue;
            
            visited[nx][ny] = true;
            dist[nx][ny] = dist[x][y] + 1;
            q.push({nx, ny});
        }
    }
    
    if (sword_x != -1) {
        int sword_dist = dist[sword_x][sword_y];
        int direct_to_princess = (N-1 - sword_x) + (M-1 - sword_y);
        int with_sword = sword_dist + direct_to_princess;
        
        if (princess_dist == -1 || with_sword < princess_dist) {
            princess_dist = with_sword;
        }
    }
    
    return princess_dist;
}

int main() {
    cin >> N >> M >> T;
    _map = vector<vector<int>>(N, vector<int>(M));
    visited = vector<vector<bool>>(N, vector<bool>(M, false));
    dist = vector<vector<int>>(N, vector<int>(M, 0));
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> _map[i][j];
        }
    }
    
    int result = bfs();
    
    if (result == -1 || result > T) {
        cout << "Fail" << endl;
    } else {
        cout << result << endl;
    }
    
    return 0;
}