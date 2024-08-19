#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 16진수 문자열을 10진수로 변환하는 함수
long long hexToDecimal(const string& hex) {
    return stoll(hex, nullptr, 16);
}

// 중복 제거 함수
void removeDuplicates(vector<string>& v) {
    vector<string> result;
    for (const auto& item : v) {
        if (find(result.begin(), result.end(), item) == result.end()) {
            result.push_back(item);
        }
    }
    v = result;
}

int main() {
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int N, K;
        cin >> N >> K;
        string s;
        cin >> s;
        s += s;  // 문자열을 두 배로 늘려 순환을 쉽게 처리

        vector<string> hexNumbers;

        for (int i = 0; i < N; i++) {
            string hexNum = s.substr(i, N / 4);
            hexNumbers.push_back(hexNum);
        }

        sort(hexNumbers.begin(), hexNumbers.end());

        removeDuplicates(hexNumbers);

        sort(hexNumbers.begin(), hexNumbers.end(), greater<string>());

        string kthLargestHex = hexNumbers[K - 1];

        long long answer = hexToDecimal(kthLargestHex);

        cout << "#" << tc << " " << answer << endl;
    }

    return 0;
}