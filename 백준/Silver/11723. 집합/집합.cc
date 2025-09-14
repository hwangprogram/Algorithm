#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int S;
    int bitset = 0;
    cin >> S;

    for (int i = 0; i < S; i++) {
        string order;
        int number;

        cin >> order;
        if (order == "add") {
            cin >> number;
            bitset |= (1 << number);
        } else if (order == "remove") {
            cin >> number;
            bitset &= ~(1 << number);
        } else if (order == "check") {
            cin >> number;
            cout << ((bitset & (1 << number)) ? 1 : 0) << '\n';
        } else if (order == "toggle") {
            cin >> number;
            bitset ^= (1 << number);
        } else if (order == "all") {
            bitset = (1 << 21) - 2; // 1~20까지 비트 ON
        } else if (order == "empty") {
            bitset = 0;
        }
    }
    return 0;
}