#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;   // 저장된 사이트 주소의 수 N, 비밀번호를 찾으려는 사이트 주소의 수 M
    cin >> N >> M;

    map<string, string> link_and_password;
    for (int i = 0; i < N; i++) {
        string site, pw;
        cin >> site >> pw;
        link_and_password.insert({site, pw});
    }

    // value값 찾아 출력
    for (int i = 0; i < M; i++) {
        string serching_site;
        cin >> serching_site;
        if (link_and_password.find(serching_site) != link_and_password.end()) {
            cout << link_and_password[serching_site] << '\n';
        }
    }

    return 0;
}