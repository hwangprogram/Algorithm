#include <iostream>
#include <vector>
#include <stack>
#include <cmath>

using namespace std;
long long real_num(long long v);
long long gcd(long long a, long long b);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long A, B;
    cin >> A >> B;
    long long result = gcd(A, B);
    for (long long i = 0; i < result; ++i) {
        cout << 1;
    }
    cout << '\n';

    return 0;
}

long long gcd(long long a, long long b) {
    long long big, small;
    if (a > b) {
        big = a;
        small = b;
    }
    else {
        big = b;
        small = a;
    }

    while (big % small > 0) {
        long long temp = small;
        small = big % small;
        big = temp;
    }
    return small;
}