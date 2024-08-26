#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int F, S, G, U, D;


int main() {
	cin >> F >> S >> G >> U >> D;
	
	vector<int> visited(F + 1, -1);  // 방문 여부와 버튼 누른 횟수를 저장하는 배열 선언 및 초기화
	queue<int> q;  // 큐 선언하고,

	q.push(S);  // 시작점을 큐에 삽입

	visited[S] = 0;
	
	while (!q.empty()) {
		int current = q.front();
		q.pop();

		if (current == G) {
			cout << visited[current] << endl;
			return 0;
		}

		// 위로 올라갈 수 있고, 올라갈 곳이 방문하지 않는 곳인지 체크
		if (current + U <= F && visited[current + U] == -1) {
			visited[current + U] = visited[current] + 1;  // 방문과 동시에 버튼 횟수 증가 반영
			q.push(current + U);  // 위로 이동한 층을 큐에 삽입
		}

		if (current - D >= 1 && visited[current - D] == -1) {  // 내려갈 수 있으며, 방문하지 않았는지 체크
			visited[current - D] = visited[current] + 1;
			q.push(current - D);
		}
		  
	}
	cout << "use the stairs" << endl;
	return 0;
}


// 스타트링크는 총 F층으로 이루어진 고층 건물

// S(지금 있는층)층에서 G층(스타트링크)으로 이동하려 한다


// 엘베엔 2개 버튼 U, D ( 위로 U층, 아래로 D층 )

// G층에 도착하려면 버튼을 적어도 몇 번 눌러야 하는지.

// F S G U D 가 주어진다.

// 예제 1

// 10 1 10 2 1

// 총 10층이고, 현재 위치 1층
// 10층으로 가야함 UP은 2, DOWN은 1

// 1 + 2 + 2 + 2 + 2 + 2 - 1

// 버튼 6번..!

//이건 1차원 방향배열?

// 엘레베이터로 이동 불가시에는 "use the stairs" 출력.