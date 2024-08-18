#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N, M;
vector<vector<int>> lab;
vector<pair<int, int>> virus;
int maxSafeArea = 0;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

void bfs() {
    vector<vector<int>> temp = lab;
    queue<pair<int, int>> q;
    
    for (int i = 0; i < virus.size(); i++) {
        q.push(virus[i]);
    }
    
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if (temp[nx][ny] == 0) {
                    temp[nx][ny] = 2;
                    q.push({nx, ny});
                }
            }
        }
    }
    
    int safeArea = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (temp[i][j] == 0) safeArea++;
        }
    }
    
    maxSafeArea = max(maxSafeArea, safeArea);
}

void dfs(int count) {
    if (count == 3) {
        bfs();
        return;
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (lab[i][j] == 0) {
                lab[i][j] = 1;
                dfs(count + 1);
                lab[i][j] = 0;
            }
        }
    }
}

int main() {
    cin >> N >> M;
    lab.resize(N, vector<int>(M));
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> lab[i][j];
            if (lab[i][j] == 2) {
                virus.push_back({i, j});
            }
        }
    }
    
    dfs(0);
    
    cout << maxSafeArea << endl;
    
    return 0;
}