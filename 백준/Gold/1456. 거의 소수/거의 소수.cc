#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long A, B;
    cin >> A >> B;
    // 아리스토텔레스의 체 구현
    vector<long> aristo(10000001);
    for (int i = 2; i < 10000001; ++i) {
        aristo[i] = i;
    }
    for (int i = 2; i <= sqrt(10000001); ++i) {    // 제곱근까지만 수행
        if (aristo[i] == 0)
            continue;
        for (int j = i + i; j <= 10000001; j += i) {
            aristo[j] = 0;
        }
    }
    int count = 0;
    for (int i = 2; i < 10000001; ++i) {
        if (aristo[i] != 0) {
            long long x = aristo[i];
            while ((double)aristo[i] <= (double)B / (double)x) {
                if ((double)aristo[i] >= (double)A / (double)x)
                    count++;
                x *= aristo[i];
            }
        }
    }
    cout << count << '\n';

    return 0;
}