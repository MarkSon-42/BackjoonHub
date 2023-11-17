#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int tc = 10;

    for (int t = 1; t < tc + 1; t++) {
        int n;
        cin >> n;

        vector<int> building(n);
        for (int i = 0; i < n; i++) {
            cin >> building[i];
        }

        int answer = 0;

        for (int i = 2; i < n - 2; ++i) {
            if ((building[i - 2] < building[i] && building[i - 1] < building[i]) &&
                (building[i + 1] < building[i] && building[i + 2] < building[i])) {
                answer += building[i] - max({building[i - 2], building[i - 1], building[i + 1], building[i + 2]});
            }
        }
        
        cout << "#" << t << " " << answer << endl;
    }
    
    return 0;
}