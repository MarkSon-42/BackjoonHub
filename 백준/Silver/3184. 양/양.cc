#include <iostream>
#include <queue>

using namespace std;

const int MAX_SIZE = 250;
char arr[MAX_SIZE][MAX_SIZE];
bool visited[MAX_SIZE][MAX_SIZE];

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

void bfs(int x, int y, int& sheepCount, int& wolfCount) {
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = true;
    
    int localSheep = 0;
    int localWolves = 0;

    // Count the initial position
    if (arr[x][y] == 'o') localSheep++;
    if (arr[x][y] == 'v') localWolves++;

    while (!q.empty()) {
        auto [curX, curY] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = curX + dx[i];
            int ny = curY + dy[i];
            if (nx >= 0 && ny >= 0 && nx < MAX_SIZE && ny < MAX_SIZE && !visited[nx][ny] && arr[nx][ny] != '#') {
                visited[nx][ny] = true;
                if (arr[nx][ny] == 'o') localSheep++;
                if (arr[nx][ny] == 'v') localWolves++;
                q.push({nx, ny});
            }
        }
    }

    if (localSheep > localWolves) {
        sheepCount += localSheep;
    } else {
        wolfCount += localWolves;
    }
}

int main() {
    int r, c;
    cin >> r >> c;

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> arr[i][j];
        }
    }

    int totalSheep = 0;
    int totalWolves = 0;

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (arr[i][j] != '#' && !visited[i][j]) {
                int sheepCount = 0;
                int wolfCount = 0;
                bfs(i, j, sheepCount, wolfCount);
                if (sheepCount > wolfCount) {
                    totalSheep += sheepCount;
                } else {
                    totalWolves += wolfCount;
                }
            }
        }
    }

    cout << totalSheep << ' ' << totalWolves << endl;

    return 0;
}