#include <iostream>

int main() {
    int N, F;
    std::cin >> N >> F;

    N = (N / 100) * 100;
    int remainder = N % F;

    if (remainder != 0) {
        N += F - remainder;
    }

    int lastTwoDigits = N % 100;

    printf("%02d\n", lastTwoDigits);

    return 0;
}