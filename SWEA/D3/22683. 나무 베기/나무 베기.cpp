#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;

const int MAX_N = 10;
const int dx[] = {-1, 0, 1, 0};  // 상, 우, 하, 좌
const int dy[] = {0, 1, 0, -1};

int N, K;
char field[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N][4][6];  // x, y, 방향, 벤 나무 수

struct State {
    int x, y, dir, trees, moves;
    State(int x, int y, int dir, int trees, int moves) : x(x), y(y), dir(dir), trees(trees), moves(moves) {}
};

int bfs(int startX, int startY, int endX, int endY) {
    queue<State> q;
    q.push(State(startX, startY, 0, 0, 0));  // 초기 상태: 위쪽 바라봄
    visited[startX][startY][0][0] = true;

    while (!q.empty()) {
        State current = q.front();
        q.pop();

        if (current.x == endX && current.y == endY) {
            return current.moves;
        }

        // 전진
        int nx = current.x + dx[current.dir];
        int ny = current.y + dy[current.dir];
        if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
            if (field[nx][ny] != 'T' && !visited[nx][ny][current.dir][current.trees]) {
                q.push(State(nx, ny, current.dir, current.trees, current.moves + 1));
                visited[nx][ny][current.dir][current.trees] = true;
            } else if (field[nx][ny] == 'T' && current.trees < K && !visited[nx][ny][current.dir][current.trees + 1]) {
                q.push(State(nx, ny, current.dir, current.trees + 1, current.moves + 1));
                visited[nx][ny][current.dir][current.trees + 1] = true;
            }
        }

        // 좌회전
        int newDir = (current.dir + 3) % 4;
        if (!visited[current.x][current.y][newDir][current.trees]) {
            q.push(State(current.x, current.y, newDir, current.trees, current.moves + 1));
            visited[current.x][current.y][newDir][current.trees] = true;
        }

        // 우회전
        newDir = (current.dir + 1) % 4;
        if (!visited[current.x][current.y][newDir][current.trees]) {
            q.push(State(current.x, current.y, newDir, current.trees, current.moves + 1));
            visited[current.x][current.y][newDir][current.trees] = true;
        }
    }

    return -1;  // 목적지에 도달할 수 없음
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N >> K;
        int startX, startY, endX, endY;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cin >> field[i][j];
                if (field[i][j] == 'X') {
                    startX = i;
                    startY = j;
                    field[i][j] = 'G';  // 시작 위치를 'G'로 변경
                } else if (field[i][j] == 'Y') {
                    endX = i;
                    endY = j;
                    field[i][j] = 'G';  // 도착 위치를 'G'로 변경
                }
            }
        }

        memset(visited, false, sizeof(visited));
        int result = bfs(startX, startY, endX, endY);
        cout << "#" << t << " " << result << endl;
    }
    return 0;
}