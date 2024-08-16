// 백준 2075번 N번째 큰 수

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class MinHeap {
private:
    vector<int> heap;

    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[index] < heap[parent]) {
                swap(heap[index], heap[parent]);
                index = parent;
            } else {
                break;
            }
        }
    }

    void heapifyDown(int index) {
        int size = heap.size();
        while (index < size) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int smallest = index;

            if (left < size && heap[left] < heap[smallest]) {
                smallest = left;
            }
            if (right < size && heap[right] < heap[smallest]) {
                smallest = right;
            }
            if (smallest != index) {
                swap(heap[index], heap[smallest]);
                index = smallest;
            } else {
                break;
            }
        }
    }

public:
    void push(int value) {
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }

    void pop() {
        if (heap.empty()) return;
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);
    }

    int top() {
        if (heap.empty()) throw out_of_range("Heap is empty");
        return heap[0];
    }

    int size() {
        return heap.size();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    MinHeap minHeap;

    for (int i = 0; i < n * n; i++) {
        int num;
        cin >> num;
        minHeap.push(num);

        if (minHeap.size() > n) {
            minHeap.pop();
        }
    }

    cout << minHeap.top() << "\n";

    return 0;
}