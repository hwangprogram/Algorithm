#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int total_val;
    cin >> total_val;
    for (int i = 0; i < 9; i++) {
        int book_val;
        cin >> book_val;
        total_val -= book_val;
    }
    cout << total_val << '\n';

    return 0;
}