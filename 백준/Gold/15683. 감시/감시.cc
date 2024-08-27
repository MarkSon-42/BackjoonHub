#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int N, M;
vector<vector<int>> office;
vector<pair<int, int>> cctvs;
int min_blind_spots = INT_MAX;

// CCTV 감시 방향 정의
const vector<vector<vector<int>>> cctv_directions = {
    {},
    {{0}, {1}, {2}, {3}},
    {{0, 2}, {1, 3}},
    {{0, 1}, {1, 2}, {2, 3}, {3, 0}},
    {{0, 1, 2}, {1, 2, 3}, {2, 3, 0}, {3, 0, 1}},
    {{0, 1, 2, 3}}
};

// 방향 정의 (상, 우, 하, 좌)
const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

void watch(int x, int y, int direction, vector<vector<int>>& tmp) {
    int nx = x, ny = y;
    while (true) {
        nx += dx[direction];
        ny += dy[direction];
        if (nx < 0 || nx >= N || ny < 0 || ny >= M || tmp[nx][ny] == 6) break;
        if (tmp[nx][ny] == 0) tmp[nx][ny] = -1;
    }
}

void dfs(int depth, vector<vector<int>> office) {
    if (depth == cctvs.size()) {
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (office[i][j] == 0) count++;
            }
        }
        min_blind_spots = min(min_blind_spots, count);
        return;
    }

    int x = cctvs[depth].first;
    int y = cctvs[depth].second;
    int cctv_type = office[x][y];

    for (const auto& dirs : cctv_directions[cctv_type]) {
        vector<vector<int>> tmp = office;
        for (int dir : dirs) {
            watch(x, y, dir, tmp);
        }
        dfs(depth + 1, tmp);
    }
}

int main() {
    cin >> N >> M;
    office.resize(N, vector<int>(M));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> office[i][j];
            if (office[i][j] >= 1 && office[i][j] <= 5) {
                cctvs.push_back({i, j});
            }
        }
    }

    dfs(0, office);

    cout << min_blind_spots << endl;

    return 0;
}