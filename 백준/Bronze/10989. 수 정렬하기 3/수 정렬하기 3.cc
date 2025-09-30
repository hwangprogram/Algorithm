#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int value_arr[10001] = {0};
    cin >> N;
    int value = 0;

    for (int i = 1; i <= N; i++) {
        cin >> value;
        value_arr[value]++;
    }

    for (int i = 0; i <= 10000; i++) {
        if (value_arr[i] != 0) {
            for (int j = 0; j < value_arr[i]; j++) {
                cout << i <<'\n';
            }
        }

    }

    return 0;
}