#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

const int MAX = 16;
int l, c;
vector<char> v;
vector<char> tmp;

bool check(vector<char> v) { //문제조건 체크
    int vowel = 0;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] == 'a' || 
            v[i] == 'e' || 
            v[i] == 'i' || 
            v[i] == 'o' || 
            v[i] == 'u') {
            vowel++;
        }
    }
    if (vowel >= 1 && l - vowel >= 2) //모음 1개 이상, 자음 2개 이상 필수 
        return true;
    return false;
}
 
void dfs(int idx) {
    if ((int)tmp.size() == l) {
        if (check(tmp)) {
            for (int i = 0; i < tmp.size(); i++) {
                cout << tmp[i];
            }
            cout << "\n";
        }
        return;
    }
    for (int i = idx; i < c; i++) {
        tmp.push_back(v[i]);
        dfs(i + 1);
        tmp.pop_back();
    }
}

int main() {
    cin >> l >> c;
    for (int i = 0; i < c; i++) {
        char alp;
        cin >> alp;
        v.push_back(alp);
    }
    sort(v.begin(), v.end());
    dfs(0);
}