#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int building[1000005];
vector<int> visited(1000005, -1);

int f, s, g, u, d;

int bfs() {
	queue<int> q;
	q.push(s);
	visited[s] = 0;
	while (!q.empty()) {
		int curr = q.front();

		if (curr == g) {  
			cout << visited[curr];
			return 0;
		}

		if (curr + u <= f && visited[curr + u] == -1) {
			visited[curr + u] = visited[curr] + 1;  
			q.push(curr + u);
		}

		if (curr - d >= 1 && visited[curr - d] == -1) {
			visited[curr - d] = visited[curr] + 1;
			q.push(curr - d);
		}
		q.pop();
	}

	return -1;
}
int main() {

	cin >> f >> s >> g >> u >> d;
	if (bfs() == -1) {
		cout << "use the stairs";
	}
}