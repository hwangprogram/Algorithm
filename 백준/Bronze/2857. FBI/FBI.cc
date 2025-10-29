#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int agent_cnt = 0;

    for (int i = 1; i <= 5; ++i) {
        string agent;
        cin >> agent;
        if (agent.find("FBI") != -1) {
            agent_cnt++;
            cout << i << ' ';
        }
    }
    if (agent_cnt == 0) cout << "HE GOT AWAY!" << '\n';

    return 0;
}