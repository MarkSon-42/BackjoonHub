#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
int ans_swd = 1e9;  // 검을 줍고 벽 부수며 공주를 구했을때 거리
int ans = 1e9;  // 검 줍지 않고 길 따라 갔을때 거리
vector<vector<int>> _map;
vector<vector<bool>> visited;
vector<vector<int>> dist;

void bfs(int n, int m, int t) {
    queue<pair<int, int>> q;
    q.push({ 0, 0 });
    visited[0][0] = true;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        if (x == n - 1 && y == m - 1) {
            ans = min(ans, dist[x][y]);
        }
        if (_map[x][y] == 2) {
            ans_swd = min(ans_swd, dist[x][y] + (n - x - 1) + (m - y - 1));
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= n || nx < 0 || ny >= m || ny < 0) continue;
            if (_map[nx][ny] == 1 || visited[nx][ny]) continue;
            visited[nx][ny] = true;
            dist[nx][ny] = dist[x][y] + 1;
            q.push({ nx, ny });
        }
    }
}

int main() {
    int n, m, t;
    cin >> n >> m >> t;
    _map = vector<vector<int>>(n, vector<int>(m));
    visited = vector<vector<bool>>(n, vector<bool>(m, false));
    dist = vector<vector<int>>(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> _map[i][j];
        }
    }
    bfs(n, m, t);

    int result = min(ans, ans_swd);
    if (result > t || result == 1e9) {
        cout << "Fail";
    } else {
        cout << result;
    }
    return 0;
}