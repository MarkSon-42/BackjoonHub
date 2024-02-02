#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int n;
    cin >> n;

    int total_marks = 0;
    bool has_satisfactory_marks = false;
    bool all_excellent_marks = true;

    for (int i = 0; i < n; i++) {
        int mark;
        cin >> mark;

        total_marks += mark;

        if (mark == 3) {
            has_satisfactory_marks = true;
            all_excellent_marks = false;
        }

        if (mark != 5) {
            all_excellent_marks = false;
        }
    }

    if (all_excellent_marks) {
        cout << "Named";
    } else if (!has_satisfactory_marks && total_marks / static_cast<double>(n) >= 4.5) {
        cout << "High";
    } else if (!has_satisfactory_marks) {
        cout << "Common";
    } else {
        cout << "None";
    }

    return 0;
}