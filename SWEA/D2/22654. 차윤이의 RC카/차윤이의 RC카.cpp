#include <iostream>
#include <string>
using namespace std;

const int MAX_N = 50; // 최대 필드 크기
char field[MAX_N][MAX_N];
int N;

void moveForward(int& x, int& y, int dir) {
    int newX = x, newY = y;
    if (dir == 0) newX--;
    else if (dir == 1) newY++;
    else if (dir == 2) newX++;
    else if (dir == 3) newY--;
    
    if (newX >= 0 && newX < N && newY >= 0 && newY < N && field[newX][newY] != 'T') {
        x = newX;
        y = newY;
    }
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        int startX, startY, endX, endY;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cin >> field[i][j];
                if (field[i][j] == 'X') {
                    startX = i;
                    startY = j;
                } else if (field[i][j] == 'Y') {
                    endX = i;
                    endY = j;
                }
            }
        }
        int Q;
        cin >> Q;
        cout << "#" << t;
        for (int q = 0; q < Q; q++) {
            int C;
            string commands;
            cin >> C >> commands;
            int x = startX, y = startY;
            int dir = 0; // 0: UP, 1: RIGHT, 2: DOWN, 3: LEFT
            for (int i = 0; i < C; i++) {
                char command = commands[i];
                if (command == 'A') {
                    moveForward(x, y, dir);
                } else if (command == 'L') {
                    dir = (dir + 3) % 4;
                } else if (command == 'R') {
                    dir = (dir + 1) % 4;
                }
            }
            cout << " " << (x == endX && y == endY);
        }
        cout << endl;
    }
    return 0;
}