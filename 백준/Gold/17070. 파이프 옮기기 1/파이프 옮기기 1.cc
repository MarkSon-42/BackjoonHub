#include <iostream>

using namespace std;

const int MAXSIZE = 16;

int n;
int ans = 0;
int room[MAXSIZE + 1][MAXSIZE + 1];

void input() {
    cin >> n;

    int temp;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            cin >> temp;
            room[r][c] = temp;
        }
    }
}

void output() {
    cout << ans << endl;
}

void movePipe(int state, int r, int c) {
    if (r == n - 1 && c == n - 1) {
        ans++;
        return;
    }

    bool canMoveH = c + 1 < n && room[r][c + 1] == 0;
    bool canMoveV = r + 1 < n && room[r + 1][c] == 0;

    if (canMoveH && state != 1) {
        movePipe(0, r, c + 1);
    }
    if (canMoveV && state != 0) {
        movePipe(1, r + 1, c);
    }

    if (canMoveH && canMoveV && room[r + 1][c + 1] == 0) {
        movePipe(2, r + 1, c + 1);
    }
}

int main() {
    input();
    movePipe(0, 0, 1);
    output();
}