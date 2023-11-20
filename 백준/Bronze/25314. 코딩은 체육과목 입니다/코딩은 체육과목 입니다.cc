# include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;

    int loop = n/4;

    for (int i = 0; i < loop; i++) {
        cout << "long" << " ";
    }
    cout << "int";
    return 0;
}