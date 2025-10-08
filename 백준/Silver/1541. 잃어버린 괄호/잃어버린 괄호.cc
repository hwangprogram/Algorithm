#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string expression, stack_tmp;
    cin >> expression;
    vector<pair<int, int>> exp_container;
    bool minus_flag = false;
    for (int i = 0; i < expression.size(); ++i) {
        if (expression[i] == '+') {
            if (!stack_tmp.empty()) {
                exp_container.emplace_back(stoi(stack_tmp), minus_flag? 1: 0);
                stack_tmp.clear();
            }
        }
        else if (expression[i] == '-') {
            if (!stack_tmp.empty()) {
                exp_container.emplace_back(stoi(stack_tmp), minus_flag? 1: 0);
                stack_tmp.clear();
            }
            minus_flag = true;
        }
        else stack_tmp.push_back(expression[i]);
    }
    if (!stack_tmp.empty()) {
        exp_container.emplace_back(stoi(stack_tmp), minus_flag? 1: 0);
        stack_tmp.clear();
    }
    int sum = 0;
    for (auto exp : exp_container) {
        if (exp.second == 0) sum += exp.first;
        else sum -= exp.first;
    }
    cout << sum << '\n';

    return 0;
}