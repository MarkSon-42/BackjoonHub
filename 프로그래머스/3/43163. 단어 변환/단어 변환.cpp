#include <string>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

bool canTransform(const string& word1, const string& word2) {
    int diff = 0;
    for (int i = 0; i < word1.length(); i++) {
        if (word1[i] != word2[i]) diff++;
    }
    return diff == 1;
}

int solution(string begin, string target, vector<string> words) {
    unordered_set<string> wordSet(words.begin(), words.end());
    
    // target이 words에 없는 경우 0 반환
    if (wordSet.find(target) == wordSet.end()) return 0;
    
    queue<pair<string, int>> q;
    q.push({begin, 0});
    
    unordered_set<string> visited;
    
    while (!q.empty()) {
        auto [current, steps] = q.front();
        q.pop();
        
        if (current == target) return steps;
        
        for (const string& word : words) {
            if (visited.find(word) == visited.end() && canTransform(current, word)) {
                visited.insert(word);
                q.push({word, steps + 1});
            }
        }
    }
    
    return 0;  // 변환할 수 없는 경우
}