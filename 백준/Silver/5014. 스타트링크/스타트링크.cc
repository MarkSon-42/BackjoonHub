#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int F, S, G, U, D;

int bfs() {
	vector<int> visited(F + 1, -1);
	queue<int> q;

	q.push(S);
	visited[S] = 0;

	while (!q.empty()) {
		int curr = q.front();
		q.pop();

		if (curr == G) {
			return visited[curr];
		}

		if (curr + U <= F && visited[curr + U] == -1) {
			visited[curr + U] = visited[curr] + 1;
			q.push(curr + U);
		}

		if (curr - D >= 1 && visited[curr - D] == -1) {
			visited[curr - D] = visited[curr] + 1;
			q.push(curr - D);
		}
	}

	return -1;
}


int main() {
	cin >> F >> S >> G >> U >> D;
	int ans = bfs();
	if (ans == -1) cout << "use the stairs";
	else cout << ans;
	return 0;
}