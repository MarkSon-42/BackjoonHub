#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class UnionFind {
public:
    UnionFind(int size) : parent(size), rank(size, 0), count(size) {
        for (int i = 0; i < size; ++i) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
            count--;
        }
    }

    int getCount() const {
        return count;
    }

private:
    vector<int> parent;
    vector<int> rank;
    int count;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        vector<vector<pair<int, int>>> edges(M);
        for (int i = 0; i < M; ++i) {
            int a, b;
            cin >> a >> b;
            edges[i].push_back({a, b});
        }

        int minAirplaneTypes = M; 
        for (const auto& airplaneEdges : edges) {
            UnionFind uf(N + 1); 

            for (const auto& edge : airplaneEdges) {
                int a = edge.first;
                int b = edge.second;
                uf.unionSets(a, b);
            }

            int components = 0;
            for (int i = 1; i <= N; ++i) {
                if (uf.find(i) == i) {
                    components++;
                }
            }

            minAirplaneTypes = min(minAirplaneTypes, components);
        }

        cout << minAirplaneTypes << '\n';
    }

    return 0;
}
