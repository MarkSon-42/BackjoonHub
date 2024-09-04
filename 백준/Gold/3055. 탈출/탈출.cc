#include <iostream>
#include <queue>
using namespace std;

int R, C;
char maze[50][50];
int dist[50][50];
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int bfs() {
    queue<pair<int, int>> water;
    queue<pair<int, int>> dochi;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            dist[i][j] = -1;
            if (maze[i][j] == 'S') {
                dochi.push({ i, j });
                dist[i][j] = 0;
            }
            else if (maze[i][j] == '*') {
                water.push({ i, j });
            }
        }
    }

    while (!dochi.empty()) {
        int water_size = water.size();
        while (water_size--) {
            int x = water.front().first;
            int y = water.front().second;
            water.pop();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < R && ny >= 0 && ny < C && maze[nx][ny] == '.') {
                    maze[nx][ny] = '*';
                    water.push({ nx, ny });
                }
            }
        }

        int dch = dochi.size();
        while (dch--) {
            int x = dochi.front().first;
            int y = dochi.front().second;
            dochi.pop();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < R && ny >= 0 && ny < C) {
                    if (maze[nx][ny] == 'D') {
                        return dist[x][y] + 1;
                    }
                    if (maze[nx][ny] == '.' && dist[nx][ny] == -1) {
                        dist[nx][ny] = dist[x][y] + 1;
                        dochi.push({ nx, ny });
                    }
                }
            }
        }
    }

    return -1;
}

int main() {
    cin >> R >> C;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> maze[i][j];
        }
    }

    int result = bfs();
    if (result == -1) {
        cout << "KAKTUS" << endl;
    }
    else {
        cout << result << endl;
    }

    return 0;
}