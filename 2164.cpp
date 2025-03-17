#include <iostream>
#include <deque>

using namespace std;

int main()
{
    deque<int> numset;
    int n;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        numset.push_back(i+1);
    }

    int cnt = 0;

    while(1){
        if (n == 1)
        {
            cout << numset[0] << endl; 
            break;
        }
        
        if (cnt == 0)
        {
            numset.pop_front();
            cnt = 1;
            n -= 1;
        }
        else
        {
            int tmp = numset.front();
            numset.pop_front();
            numset.push_back(tmp);
            cnt = 0;
        }
    }

    return 0;
}