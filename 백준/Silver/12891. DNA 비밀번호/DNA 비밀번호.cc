#include <iostream>
#include <string>

using namespace std;

// 체크할 문자 배열 checkArr, 내 배열 myArr
int checkArr[4], myArr[4];
// 정답 카운트 : 4가 되면 ans++, 정답 ans
int ansCount = 0;
// 내 함수에 유전자 추가, 제거하는 함수
void Add(char c);
void Remove(char c);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 문자열 길이 S, 부분문자열 길이 P
    int S, P;
    // 정답 수 ans
    int ans = 0;
    // 문자열 genes
    string genes;
    // 입력받기
    cin >> S >> P;
    cin >> genes;
    for (int i = 0; i < 4; i++) {
        cin >> checkArr[i];
        if (checkArr[i] == 0)
            ansCount++;
    }

    // 초기 윈도우 처리
    for (int i = 0; i < P; i++) {
        Add(genes[i]);
    }
    // 초기 윈도우에서 정답 있으면 플러스
    if (ansCount == 4)
        ans++;

    // 윈도우 이동 로직
    for (int i = P; i < S; i++) {
        int j = i - P;
        Add(genes[i]);
        Remove(genes[j]);
        if (ansCount == 4)
            ans++;
    }
    cout << ans;

    return 0;
}

void Add(char c) {  // 문자 확인용 배열 수 추가하는 함수
    switch (c) {
        case 'A':
            myArr[0]++;
            if (myArr[0] == checkArr[0])
                ansCount++;
            break;
        case 'C':
            myArr[1]++;
            if (myArr[1] == checkArr[1])
                ansCount++;
            break;
        case 'G':
            myArr[2]++;
            if (myArr[2] == checkArr[2])
                ansCount++;
            break;
        case 'T':
            myArr[3]++;
            if (myArr[3] == checkArr[3])
                ansCount++;
            break;
    }
}

void Remove(char c) {
    switch (c) {
        case 'A':
            if (myArr[0] == checkArr[0])
                ansCount--;
            myArr[0]--;
            break;
        case 'C':
            if (myArr[1] == checkArr[1])
                ansCount--;
            myArr[1]--;
            break;
        case 'G':
            if (myArr[2] == checkArr[2])
                ansCount--;
            myArr[2]--;
            break;
        case 'T':
            if (myArr[3] == checkArr[3])
                ansCount--;
            myArr[3]--;
            break;
    }
}