#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

// 1. 파티 정보에 대해 저장하기
// 2. 같은 파티에 참여한 사람들을 같은 집합으로 묶기
// 3. union 계산이 끝난 파티 배열을 다시 순환하며 진실을 아는 사람이 없는 파티의 수 계산
int parents[51];   // 부모 배열
int find(int a);
void unionfunc(int a, int b);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, knower_num;   // 사람 N명, M개의 파티, 진실을 아는 사람들 수
    int ans = 0;    // 거짓말 가능한 파티의 수
    cin >> N >> M;
    vector<vector<int>> parties(M);    // 파티 배열
    vector<int> knowers;    // 진실을 아는 사람들
    // parents 배열 초기화
    for (int i = 1; i <= 50; ++i) {
        parents[i] = i;
    }
    // 진실을 아는 사람 저장
    cin >> knower_num;
    for (int i = 0; i < knower_num; ++i) {
        int people;
        cin >> people;
        knowers.push_back(people);
    }

    // 파티 저장
    for (int i = 0; i < M; ++i) {
        int party_people;   // 파티에 오는 사람 수
        cin >> party_people;

        for (int j = 0; j < party_people; ++j) {
            int people;
            cin >> people;
            parties[i].push_back(people);
        }

        // 같은 파티에 있는 사람들은 같은 집합에 묶음
        for (int j = 0; j < party_people; ++j) {
            unionfunc(parties[i][0], parties[i][j]);
        }
    }

    // union 계산이 끝난 파티를 순회하기
    for (int i = 0; i < M; ++i) {
        bool can_fool = true;
        // 진실을 아는 자와 파티에 참석한 사람의 부모가 같다면 -> 거짓말 불가
        for (int person : parties[i]) {
            for (int knower : knowers) {
                if (find(person) == find(knower)) {
                    can_fool = false;
                    break;
                }
            }
            if (!can_fool) break;
        }
        if (can_fool) ans++;
    }
    cout << ans << '\n';

    return 0;
}

int find(int a) {
    if (parents[a] == a)
        return a;
    return parents[a] = find(parents[a]);
}

void unionfunc(int a, int b) {
    a = find(a);
    b = find(b);

    if (a != b)
        parents[b] = a;
}