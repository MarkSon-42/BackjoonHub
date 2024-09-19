#include <iostream>
#include <queue>
using namespace std;

const int MAX = 51;
const int INF = 1e9;
const int dy[4] = {-1, 0, 1, 0};
const int dx[4] = {0, 1, 0, -1};

int N, M, cnt = 0, MIN = INF;
char MAP[MAX][MAX];
int start_y, start_x, exit_y, exit_x;
int items_y[6], items_x[6];
bool visited[6];

int bfs(int sy, int sx, int ey, int ex) {
    int dist[MAX][MAX] = {0};
    queue<pair<int, int>> q;
    q.push({sy, sx});
    dist[sy][sx] = 1;

    while (!q.empty() && dist[ey][ex] == 0) {
        int y = q.front().first, x = q.front().second;
        q.pop();
        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d], nx = x + dx[d];
            if (ny < 0 || nx < 0 || ny >= M || nx >= N) continue;
            if (MAP[ny][nx] == '#' || dist[ny][nx] != 0) continue;
            dist[ny][nx] = dist[y][x] + 1;
            q.push({ny, nx});
        }
    }
    return dist[ey][ex] - 1;
}

void dfs(int y, int x, int level, int steps) {
    if (level == cnt) {
        steps += bfs(y, x, exit_y, exit_x);
        MIN = min(MIN, steps);
        return;
    }
    for (int i = 0; i < cnt; i++) {
        if (visited[i]) continue;
        visited[i] = true;
        int d = bfs(y, x, items_y[i], items_x[i]);
        dfs(items_y[i], items_x[i], level + 1, steps + d);
        visited[i] = false;
    }
}

int main() {
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> MAP[i][j];
            if (MAP[i][j] == 'X') {
                items_y[cnt] = i;
                items_x[cnt] = j;
                cnt++;
            } else if (MAP[i][j] == 'S') {
                start_y = i; start_x = j;
            } else if (MAP[i][j] == 'E') {
                exit_y = i; exit_x = j;
            }
        }
    }
    dfs(start_y, start_x, 0, 0);
    cout << MIN;
    return 0;
}