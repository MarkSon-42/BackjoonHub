#include <iostream>
#include <queue>
#include <vector>
#define MAX 101
using namespace std;

int n, m;
int map[MAX][MAX];
int val[MAX][MAX];
bool visited[MAX][MAX];
vector<pair<int, int>> melted_cheese;

bool inRange(int x, int y) {
    return (0 <= x && x < n && 0 <= y && y < m);
}

int bfs() {
    queue<pair<int, int>> q;
    int dx[] = { -1, 1, 0, 0 };
    int dy[] = { 0, 0, -1, 1 };
    int curHour = 0;
    
    q.push(make_pair(0, 0));
    visited[0][0] = true;
    
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (!inRange(nx, ny))
                continue;
            
            // 공기인 경우 (새로운)
            if (map[nx][ny] == 0 && !visited[nx][ny]) {
                visited[nx][ny] = true;
                q.push(make_pair(nx, ny));
            }
            // 치즈인 경우
            else if (map[nx][ny] == 1) {
                // 외부 공기와 두 군데 이상 접촉된 경우
                if (++val[nx][ny] >= 2 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    melted_cheese.push_back(make_pair(nx, ny));
                }
            }
        }
        
        //큐가 비었고, 지금 턴에 녹은 치즈가 있는 경우
        if (q.empty() && !melted_cheese.empty()) {
            curHour++;
            for (size_t i = 0; i < melted_cheese.size(); i++) {    
                //녹은 치즈는 공기가 되었다.
                q.push(melted_cheese[i]);
                map[melted_cheese[i].first][melted_cheese[i].second] = 0;
            }
            melted_cheese.clear();
        }
    }
    return curHour;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];
        }
    }
    
    cout << bfs();
    return 0;
}