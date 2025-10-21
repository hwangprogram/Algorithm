#include <iostream>
#include <string>
#include <vector>

using namespace std;
vector<int> split(const string& str, char delimiter);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string current_time_tmp, start_time_tmp, ans_time;
    cin >> current_time_tmp;
    cin >> start_time_tmp;
    vector<int> current_times = split(current_time_tmp, ':');
    vector<int> start_times = split(start_time_tmp, ':');
    int ans_h = 0, ans_m = 0, ans_s = 0;
    string hour, minute, second;

    if (current_times[2] > start_times[2]) {
        start_times[2] += 60;
        start_times[1]--;
    }
    ans_s += start_times[2] - current_times[2];
    if (ans_s / 10 == 0) second = '0' + to_string(ans_s);
    else second = to_string(ans_s);

    if (current_times[1] > start_times[1]) {
        start_times[1] += 60;
        start_times[0]--;
    }
    ans_m += start_times[1] - current_times[1];
    if (ans_m / 10 == 0) minute = '0' + to_string(ans_m);
    else minute = to_string(ans_m);

    if (current_times[0] > start_times[0]) start_times[0] += 24;
    ans_h += start_times[0] - current_times[0];
    if (ans_h / 10 == 0) hour = '0' + to_string(ans_h);
    else hour = to_string(ans_h);
    cout << hour << ':' << minute << ':' << second << '\n';

    return 0;
}

vector<int> split(const string& str, char delimiter) {
    vector<int> tokens;
    size_t start = 0;
    size_t end = str.find(delimiter);

    while (end != string::npos) {
        string token = str.substr(start, end - start);
        if (!token.empty()) tokens.push_back(stoi(token));
        start = end + 1;
        end = str.find(delimiter, start);
    }
    string last = str.substr(start);
    if (!last.empty()) tokens.push_back(stoi(last));

    return tokens;
}