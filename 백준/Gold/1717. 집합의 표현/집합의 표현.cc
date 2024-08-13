#include <iostream>
#include <vector>

using namespace std;

int n, m;
int parent[1000001];


int getParent(int x) {
	if (parent[x] == x) return x;
	return parent[x] = getParent(parent[x]);
	// 노드 x의 대표 부모 노드를 찾는 함수
}

void unionParent(int a, int b) {
	a = getParent(a);
	b = getParent(b);

	// 두 노드의 부모를 비교하여 더 작은 값을 부모로 설정
   // 이렇게 하면 트리의 높이가 낮아져 성능이 향상됨
	if (a > b) parent[a] = b;
	else parent[b] = a;
	// 두 노드 a와 b의 집합을 합치는 함수

}

void findParent(int a, int b) {
	// 두 노드 a와 b가 같은 집합에 속하는지 확인하는 함수

	// 각각의 부모 노드를 찾는다
	a = getParent(a);
	b = getParent(b);

	// 부모 노드가 같다면, 두 노드는 같은 집합에 속하므로 "YES"
	if (a == b) cout << "YES\n";
	else cout << "NO\n";

}

int main() {
	ios::sync_with_stdio(false); // c++의 입출력 속도를 향상
	cin.tie(0); // cin과 cout의 동기화를 해제하여 성능 향상
	cout.tie(0); // cin과 cout의 동기화를 해제하여 성능 향상

	cin >> n >> m;

	// 각 노드는 처음에 자기 자신을 부모로 설정 (..왜?)

	for (int i = 1; i <= n; i++) {
		parent[i] = i;
	}

	for (int i = 0; i < m; i++) {
		int opr, a, b;
		cin >> opr >> a >> b;

		if (!opr) {
			unionParent(a, b);
		} 
		else {
			findParent(a, b);
		}
	}

	return 0;
}
