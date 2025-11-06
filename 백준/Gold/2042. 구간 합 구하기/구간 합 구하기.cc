#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

static vector<long> tree;
long getSum(int s, int e);
void changeVal(int index, long val);
void setTree(int i);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K;     // 수의 개수, 변경이 일어나는 횟수, 구간 합을 구하는 횟수
    int treeHeight = 0;
    int Length = N;

    while (Length != 0) {   // 트리의 높이 구하기
        Length /= 2;
        treeHeight++;
    }

    int treeSize = int(pow(2, treeHeight + 1));
    int leftNodeStartIndex = treeSize / 2 - 1;
    tree.resize(treeSize + 1);

    // 데이터를 리프 노트에 입력받기
    for (int i = leftNodeStartIndex + 1; i <= leftNodeStartIndex + N; ++i) {
        cin >> tree[i];
    }
    setTree(treeSize - 1);  // tree 만들기

    for (int i = 0; i < M + K; ++i) {
        long a, s, e;
        cin >> a >> s >> e;

        if (a == 1) {       // 변경
            changeVal(leftNodeStartIndex + s, e);
        }
        else if (a == 2) {  // 구간 합
            s += leftNodeStartIndex;
            e += leftNodeStartIndex;
            cout << getSum(s, e) << '\n';
        }
    }

    return 0;
}

long getSum(int s, int e) {     // 구간 합 연산 함수
    long partSum = 0;

    while (s <= e) {
        if (s % 2 == 1) {
            partSum += tree[s];
            s++;
        }
        if (e % 2 == 0) {
            partSum += tree[e];
            e--;
        }
        s /= 2;
        e /= 2;
    }
    return partSum;
}

void changeVal(int index, long val) {   // 트리값 변경 함수
    long diff = val - tree[index];

    while (index > 0) {
        tree[index] += diff;
        index /= 2;
    }
}

void setTree(int i) {   // 초기 트리 생성 함수
    while (i != 1) {
        tree[i / 2] += tree[i];
        i--;
    }
}