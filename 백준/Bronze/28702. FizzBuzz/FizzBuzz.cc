#include <iostream>
#include <string>
using namespace std;

bool isNumber(const string& str) {
    for (char const &c : str) {
        if (isdigit(c) == 0) return false;
    }
    return true;
}

int main() {
    string s1, s2, s3;
    getline(cin, s1);
    getline(cin, s2);
    getline(cin, s3);
    int result = 0;

    if (isNumber(s1)) { // 첫번째 단어가 숫자라면
        result = stoi(s1) + 3;
    } else {
        if (isNumber(s2)) { // 두번째 단어가 숫자라면
            result = stoi(s2) + 2;
        } else {
            if (isNumber(s3)) { // 세번째 단어가 숫자라면
                result = stoi(s3) + 1;
            }
        }
    }

    string output;
    if (result % 3 == 0) { // 정답이 3의 배수라면
        output += "Fizz";
    }

    if (result % 5 == 0) { // 정답이 5의 배수라면
        output += "Buzz";
    }

    if (output.empty()) { // 정답이 3과 5의 배수가 아니라면
        output = to_string(result);
    }

    cout << output << endl;

    return 0;
}