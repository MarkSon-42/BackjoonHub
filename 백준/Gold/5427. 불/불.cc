#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int t, w, h;
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
char maze[1001][1001];
int dist[1001][1001];

int bfs() {
	// bfs적용 객체가 2개니까..큐도 2개
	queue<pair<int, int>> q; 
	queue<pair<int, int>> fire;

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			if (maze[i][j] == '@') {
				q.push({ i, j });
				dist[i][j] = 0;
			}
			else if (maze[i][j] == '*') {
				fire.push({ i, j });
			}
			if (maze[i][j] != '#') dist[i][j] = -1;
		}
	}

	while (!q.empty()) {
		int f_size = fire.size();  // 불 큐 크기 만큼..?
		while (f_size--) {
			int x = fire.front().first;
			int y = fire.front().second;
			fire.pop();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
				if (maze[nx][ny] == '.' || maze[nx][ny] == '@') {
					maze[nx][ny] = '*';
					fire.push({ nx, ny });
				}
			}
		}

		int q_size = q.size();

		while (q_size--) {
			int x = q.front().first;
			int y = q.front().second;
			q.pop();

			if (x == 0 || x == h - 1 || y == 0 || y == w - 1) {
				return dist[x][y] + 2;  // 탈출 ( 탈출 거리가 아니고 탈출했을때 초를 구하는거라 +2 해줌.
			}
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
				if (maze[nx][ny] == '.' && dist[nx][ny] == -1) {
					dist[nx][ny] = dist[x][y] + 1;
					q.push({ nx, ny });
				}
			}
		}
	}
	// 큐도 비었는데 여기까지 왔다면.. 탈출 불가능이오.
	return -1;
}

int main() {
	cin >> t;
	while (t--) {
		cin >> w >> h;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				cin >> maze[i][j];
				dist[i][j] = -1;
			}
		}

		int ans = bfs();
		if (ans == -1) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			cout << ans << endl;
		}
	}
	return 0;
}