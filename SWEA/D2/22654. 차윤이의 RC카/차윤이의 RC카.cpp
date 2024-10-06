#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Position {
    int x, y;
};

enum Direction { UP, RIGHT, DOWN, LEFT };

Position moveForward(Position pos, Direction dir, int N, vector<string>& field) {
    Position newPos = pos;
    switch (dir) {
        case UP: newPos.x--; break;
        case RIGHT: newPos.y++; break;
        case DOWN: newPos.x++; break;
        case LEFT: newPos.y--; break;
    }
    if (newPos.x >= 0 && newPos.x < N && newPos.y >= 0 && newPos.y < N && field[newPos.x][newPos.y] != 'T') {
        return newPos;
    }
    return pos;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        vector<string> field(N);
        Position start, end;
        for (int i = 0; i < N; i++) {
            cin >> field[i];
            for (int j = 0; j < N; j++) {
                if (field[i][j] == 'X') {
                    start = {i, j};
                } else if (field[i][j] == 'Y') {
                    end = {i, j};
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
            Position pos = start;
            Direction dir = UP;
            for (char command : commands) {
                if (command == 'A') {
                    pos = moveForward(pos, dir, N, field);
                } else if (command == 'L') {
                    dir = static_cast<Direction>((dir + 3) % 4);
                } else if (command == 'R') {
                    dir = static_cast<Direction>((dir + 1) % 4);
                }
            }
            if (pos.x == end.x && pos.y == end.y) {
                cout << " 1";
            } else {
                cout << " 0";
            }
        }
        cout << endl;
    }
    return 0;
}