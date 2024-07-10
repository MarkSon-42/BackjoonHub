#include <stdio.h>
#include <string.h>

int dx[] = {0, 0, 1, -1, 1, -1, 1, -1};
int dy[] = {1, -1, 0, 0, 1, 1, -1, -1};

int N;
char grid[101][101];

int search(int x, int y, int dir) {
    char target[] = "MOBIS";
    for(int i = 0; i < strlen(target); i++) {
        int nx = x + dx[dir] * i;
        int ny = y + dy[dir] * i;
        if (nx < 0 || ny < 0 || nx >= N || ny >= N || grid[nx][ny] != target[i])
            return 0;
    }
    return 1;
}

int main() {
    scanf("%d", &N);
    for(int i = 0; i < N; i++) {
        scanf("%s", grid[i]);
    }

    int cnt = 0;
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            for(int dir = 0; dir < 8; dir++) {
                cnt += search(i, j, dir);
            }
        }
    }

    printf("%d\n", cnt);
    return 0;
}