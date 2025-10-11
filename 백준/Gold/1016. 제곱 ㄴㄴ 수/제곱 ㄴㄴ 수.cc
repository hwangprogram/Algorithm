#include <iostream>
#include <vector>
#include <stack>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long min, max;
    cin >> min >> max;
    vector<bool> check(max - min + 1);

    for (long i = 2; i * i <= max; ++i) {
        long pow = i * i;
        long start_index = min / pow;

        if (min % pow != 0) {   // 나머지가 0이 아닐때 한자리 올리기
            start_index++;
        }
        for (long j = start_index; pow * j <= max; j++) {
            check[(int)((pow*j)-min)] = true;
        }
    }
    int count = 0;
    for (int i = 0; i <= max - min; ++i) {
        if (!check[i]) count++;
    }
    cout << count << '\n';

    return 0;
}