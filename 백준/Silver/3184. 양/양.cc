// 백준 3184 flood fill 양과 늑대 문제

#include <iostream>
#include <queue>

using namespace std;

const int MAX_SIZE = 250;
char arr[MAX_SIZE][MAX_SIZE];
bool visited[MAX_SIZE][MAX_SIZE];
int sheep, wolf, r, c;

int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };

void bfs(int i, int j) {
    queue<pair<int, int>> q;
    q.push({ i, j });
    visited[i][j] = true;
    int s = 0;
    int w = 0;
    if (arr[i][j] == 'o') s++;
    if (arr[i][j] == 'v') w++;
    
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= r || ny < 0 || ny >= c) continue;
            if (visited[nx][ny] || arr[nx][ny] == '#') continue;
            visited[nx][ny] = 1;
            if (arr[nx][ny] == 'o') s++;
            if (arr[nx][ny] == 'v') w++;
            q.push({ nx, ny });
        }
    }

    // 양이 늑대보다 많다? 오호호,, 해당 울타리 늑대 모두 아웃!
    if (s > w) wolf -= w;
    if (s <= w) sheep -= s;
}

// 글자 '.' (점)은 빈 필드를 의미하며,
// 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미


// 늑대일 경우 bfs호출.. 그리고 늑대를 카운트 하자


int main()
{
    cin >> r >> c;

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (arr[i][j] == 'o') sheep++;
            if (arr[i][j] == 'v') wolf++;
        }
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (arr[i][j] != '#' && !visited[i][j]) {
                bfs(i, j);
            }
        }
    }

    cout << sheep << " " << wolf;
}