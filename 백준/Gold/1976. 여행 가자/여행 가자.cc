#include <iostream>
#include <vector>

using namespace std;
static vector<int> parent;
int find(int a);
void unionfunc(int a, int b);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;   // 도시 N개, 방문할 도시 M개
    cin >> N;
    cin >> M;
    parent.resize(N+1);

    for (int i = 1; i <= N; ++i) {  // 대표 노드를 자기 자신으로 초기화
        parent[i] = i;
    }
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            int road;   // 길 여부
            cin >> road;

            if (road == 1) {    // 길이 있을 때만 union
                unionfunc(i, j);
            }
        }
    }

    bool ans = true;   // 정답여부
    int first_v, p;
    cin >> first_v;
    p = find(first_v);    // 첫 값의 부모로 다음값들과 부모가 같은지 체크
    for (int i = 1; i < M; ++i) {
        int temp;
        cin >> temp;
        if (find(temp) != p) {    // 입력받은 값의 부모가 처음 값의 부모와 다르면
            ans = false;    // NO 출력을 위한 flag
            break;
        }
    }
    if (ans) cout << "YES\n";
    else cout << "NO\n";

    return 0;
}

int find(int a) {
    if (a == parent[a]) return a;
    // 부모를 타고 올라가면서 최종 부모를 찾고, 자식들을 모두 최종 부모로 갱신
    else return parent[a] = find(parent[a]);
}

void unionfunc(int a, int b) {
    // 부모 찾기
    a = find(a);
    b = find(b);

    // 부모가 다른 경우 결합
    if (a != b) parent[b] = a;
}