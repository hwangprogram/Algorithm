#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    float age_min = 2010+(12/12)+(31/31) , age_max=1990+(1/12)+(1/31);
    string oldest, youngest;

    for (int i = 0; i < N; i++) {
        string name;
        float day, month, year;
        cin >> name >> day >> month >> year;
        float sum_age = (day/31) + (month/12) + year;

        if (sum_age < age_min) {
            age_min = sum_age;
            oldest = name;
        }
        if (sum_age > age_max) {
            age_max = sum_age;
            youngest = name;
        }
    }
    cout << youngest << '\n';
    cout << oldest << '\n';

    return 0;
}