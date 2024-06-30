#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        int N;
        scanf("%d", &N);

        int triangle[10][10] = {0};

        triangle[0][0] = 1;

        for (int i = 1; i < N; i++) {
            triangle[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
            }
        }

        printf("#%d\n", t);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= i; j++) {
                if (j > 0) printf(" ");
                printf("%d", triangle[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
