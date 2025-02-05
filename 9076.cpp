#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        vector<int> num = {0, 0, 0, 0, 0};

        for (int j = 0; j < 5; j++) {
            int temp;
            cin >> temp;
            num[j] += temp;
        }

        sort(num.begin(), num.end());
        int sum = num[1] + num[2] + num[3];
        int diff_min_max = num[3] - num[1];
        if (diff_min_max >= 4) {
            cout << "KIN" << endl;
        } else {
            cout << sum << endl;
        }
    }
}