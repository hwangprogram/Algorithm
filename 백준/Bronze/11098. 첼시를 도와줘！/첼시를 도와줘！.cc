#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int P, max = 0;
        string best_player;
        cin >> P;
        for (int j = 0; j < P; j++) {
            int cost;
            string player;
            cin >> cost >> player;
            if (cost > max) {
                max = cost;
                best_player = player;
            }
        }
        cout << best_player << '\n';
    }

    return 0;
}