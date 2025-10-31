#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, sum = 0;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        int students, apples;
        cin >> students >> apples;
        sum += apples % students;
    }
    cout << sum << '\n';

    return 0;
}