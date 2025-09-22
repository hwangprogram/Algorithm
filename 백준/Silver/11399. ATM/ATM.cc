#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;  // 수열 수
    cin >> N;
    vector<int> A(N, 0);    // 수열

    for (int i = 0; i < N; i++) {
        cin >> A[i];    // 수열 입력
    }

    for (int i = 1; i < N; i++) {
        int insert_point = i;
        int insert_value = A[i];
        for (int j = i-1; j > -1; j--) {
            if (A[i] > A[j]) {
                insert_point = j + 1;   // 삽입 지점
                break;
            }
            if (j == 0)
                insert_point = 0;
        }

        for (int j = i; j > insert_point; j--) {  // i부터 삽입지점 i+1까지의 데이터 한칸씩 밀기
            A[j] = A[j-1];
        }
        A[insert_point] = insert_value;
    }

    // 합배열 만들기
    vector<int> S(N, 0);
    S[0] = A[0];
    for (int i = 1; i < N; i++) {
        S[i] = S[i-1] + A[i];
    }

    // 결과 출력
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += S[i];
    }
    cout << sum << '\n';

    return 0;
}