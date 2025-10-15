#include <iostream>
#include <vector>
#include <tuple>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int max = 0;
    for (int i = 0; i < 2; ++i) {
        int a, b, c, d, sum = 0;
        cin >> a >> b >> c >> d;
        if (a + b + c + d > max) {
            max = a + b + c + d;
        }
    }
    cout << max << '\n';

    return 0;
}