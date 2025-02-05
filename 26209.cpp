#include <iostream>

using namespace std;
int main() {
    int bits[8] = {0,};

    for (int i = 0; i < 8; i++) {
        cin >> bits[i];
    }

    for (int i = 0; i < 8; i++) {
        if (bits[i] == 9) {
            cout << 'F';
            return 0;
        }
    }
    cout << 'S';
    return 0;
}