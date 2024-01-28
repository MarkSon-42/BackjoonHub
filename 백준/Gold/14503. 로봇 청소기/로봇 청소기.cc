#include <iostream>
#include <queue>
using namespace std;

int N, M;
int r, c, d;
int room[50][50];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int turn_left(int d) {
    if (d == 0) {
        return 3;
    } else {
        return d - 1;
    }
}

int main() {
    cin >> N >> M;
    cin >> r >> c >> d;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> room[i][j];
        }
    }

    int count = 1;
    room[r][c] = 2;
    while (true) {
        bool check = false;
        for (int i = 0; i < 4; i++) {
            d = turn_left(d);
            int nx = r + dx[d];
            int ny = c + dy[d];
            if (room[nx][ny] == 0) {
                count++;
                room[nx][ny] = 2;
                r = nx;
                c = ny;
                check = true;
                break;
            }
        }
        if (!check) {
            if (room[r - dx[d]][c - dy[d]] == 1) {
                break;
            } else {
                r -= dx[d];
                c -= dy[d];
            }
        }
    }

    cout << count;

    return 0;
}