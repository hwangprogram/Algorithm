#include <iostream>
#include <vector>
#include <stack>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int A, B, big, small;
        cin >> A >> B;
        if (A > B) {
            big = A;
            small = B;
        }
        else {
            big = B;
            small = A;
        }
        while (big % small != 0) {
            const int temp = small;
            small = big % small;
            big = temp;
        }
        int ans = (A * B) / small;
        cout << ans << '\n';
    }

    return 0;
}