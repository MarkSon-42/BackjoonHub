#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int t, w, h;
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
char maze[1001][1001];
int dist[1001][1001];

int bfs() {
    queue<pair<int, int>> q;
    queue<pair<int, int>> fire;

    // 상근이와 불의 초기 위치를 찾아 큐에 넣습니다.
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (maze[i][j] == '@') {
                q.push({ i, j });
                dist[i][j] = 0;
            }
            else if (maze[i][j] == '*') {
                fire.push({ i, j });
            }
            if (maze[i][j] != '#') dist[i][j] = -1;
        }
    }

    while (!q.empty()) {
        // 불을 먼저 확산시킵니다.
        int fire_size = fire.size();
        while (fire_size--) {
            int x = fire.front().first;
            int y = fire.front().second;
            fire.pop();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
                if (maze[nx][ny] == '.' || maze[nx][ny] == '@') {
                    maze[nx][ny] = '*';
                    fire.push({ nx, ny });
                }
            }
        }

        // 상근이를 이동시킵니다.
        int size = q.size();
        while (size--) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();

            // 탈출 조건: 가장자리에 도달했을 때
            if (x == 0 || x == h - 1 || y == 0 || y == w - 1) {
                return dist[x][y] + 2;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
                if (maze[nx][ny] == '.' && dist[nx][ny] == -1) {
                    dist[nx][ny] = dist[x][y] + 1;
                    q.push({ nx, ny });
                }
            }
        }
    }
    return -1; // 탈출 불가능
}

int main() {

//    FILE* file;
//    freopen_s(&file, "input.txt", "r", stdin);

    cin >> t;
    while (t--) {
        cin >> w >> h;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                cin >> maze[i][j];
                dist[i][j] = -1;
            }
        }

        int result = bfs();
        if (result == -1) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            cout << result << endl;
        }
    }
    return 0;
}