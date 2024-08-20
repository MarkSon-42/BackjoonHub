#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

vector<int> dijkstra(int start, int n, const vector<vector<pair<int, int>>>& graph, int k) {
    vector<vector<int>> distances(n + 1);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    pq.push({0, start});
    
    while (!pq.empty()) {
        int currentDist = pq.top().first;
        int current = pq.top().second;
        pq.pop();
        
        if (distances[current].size() == k) continue;
        
        distances[current].push_back(currentDist);
        
        for (const auto& edge : graph[current]) {
            int next = edge.first;
            int nextDist = currentDist + edge.second;
            
            if (distances[next].size() < k) {
                pq.push({nextDist, next});
            }
        }
    }
    
    vector<int> result(n + 1, -1);
    for (int i = 1; i <= n; i++) {
        if (distances[i].size() == k) {
            result[i] = distances[i].back();
        }
    }
    
    return result;
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    
    vector<vector<pair<int, int>>> graph(n + 1);
    
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
    }
    
    vector<int> result = dijkstra(1, n, graph, k);
    
    for (int i = 1; i <= n; i++) {
        cout << result[i] << '\n';
    }
    
    return 0;
}