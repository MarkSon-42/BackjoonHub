#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    for (int t = 1; t <= 10; t++) {

        int cnt;
        vector<int> boxes;

        cin >> cnt;
        for (int i = 0; i < 100; i++) {
            int box;
            cin >> box;
            boxes.push_back(box);
        }

        sort(boxes.begin(), boxes.end());

        for (int i = 0; i < cnt; i++) {

            //가장 많은 박스에서 가장 적은 박스로 하나 넘기기
            boxes.back()--;
            boxes.front()++;

            sort(boxes.begin(), boxes.end());

            //차이가 1이하인 경우 -> 평탄화 종료
            if (boxes.back() - boxes.front() <= 1) {
                break;
            }
        }
        cout << "#" << t << " " << boxes.back() - boxes.front() << "\n";
    }

    return 0;
}