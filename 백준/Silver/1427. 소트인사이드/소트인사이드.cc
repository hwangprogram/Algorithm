#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string numbers;
    cin >> numbers;
    vector<int> A(numbers.size(), 0);

    // 문자열 > 숫자 배열로 전환
    for (int i = 0; i < numbers.size(); i++) {
        A[i] = stoi(numbers.substr(i, 1));
    }

    // 정렬 (선택정렬)
    for (int i = 0; i < numbers.size(); i++) {
        int max_index = i;
        for (int j = i+1; j < numbers.size(); j++) {
            if (A[j] > A[max_index])
                max_index = j;
        }
        if (max_index != i) {
            int temp = A[i];
            A[i] = A[max_index];
            A[max_index] = temp;
        }
        cout << A[i];
    }

    return 0;
}