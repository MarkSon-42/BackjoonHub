#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
bool flag;
int _map[305][305];
int copy_map[305][305];
int N, M, hour, visited[305][305];
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };
bool allMapZero() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (_map[i][j] != 0) return false;
        }
    }
    return true;
}
void dfs(int y, int x) {
    visited[y][x] = 1;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 0 || nx >= M || ny < 0 || ny >= N || _map[ny][nx] == 0 || visited[ny][nx]) {
            continue;
        }
        dfs(ny, nx);
    }
    return;
}
bool check() {
    fill(&visited[0][0], &visited[0][0] + 305 * 305, 0);
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (_map[i][j] != 0 && !visited[i][j]) {
                dfs(i, j);
                cnt++;
            }
        }
    }
    return cnt >= 2;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> _map[i][j];
        }
    }
    while (true) {

        if (check()) {
            flag = true;
            break;
        }
        else if (allMapZero()) break;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                copy_map[i][j] = _map[i][j];
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (copy_map[i][j]) {
                    int cnt = 0;
                    for (int d = 0; d < 4; d++) {
                        int nx = j + dx[d];
                        int ny = i + dy[d];
                        if (nx < 0 || nx >= M || ny < 0 || ny >= N || copy_map[ny][nx]) {
                            continue;
                        }
                        cnt++;
                    }
                    _map[i][j] = max(copy_map[i][j] - cnt, 0);
                }
            }
        }
        hour++;
    }
    if (flag) cout << hour << "\n";
    else cout << 0 << "\n";
    return 0;
}