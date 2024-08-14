#include <iostream>
#include <queue>

using namespace std;

const int MAX_SIZE = 1005;
int arr[MAX_SIZE][MAX_SIZE];
bool visited[MAX_SIZE][MAX_SIZE];
int r, c, startX, startY, new_color;

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

void bfs(int startX, int startY, int new_color) {
    queue<pair<int, int>> q;
    int origin_color = arr[startX][startY];

    if (origin_color == new_color) return; 

    q.push({startX, startY});
    visited[startX][startY] = true;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        arr[x][y] = new_color;

        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < r && ny >= 0 && ny < c && !visited[nx][ny] && arr[nx][ny] == origin_color) {
                visited[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
}

int main() {
    cin >> r >> c;

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            char ch;
            cin >> ch;
            arr[i][j] = ch - '0';
        }
    }

    cin >> startX >> startY >> new_color;

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            visited[i][j] = false;
        }
    }

    bfs(startX, startY, new_color);

    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cout << arr[i][j];
        }
        cout << endl;
    }

    return 0;
}
