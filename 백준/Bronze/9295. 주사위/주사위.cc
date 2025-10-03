#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    for (int i = 1; i <= T; i++) {
        int n1, n2;
        cin >> n1 >> n2;
        cout << "Case " << i << ": " << n1+n2 << '\n';
    }

    return 0;
}