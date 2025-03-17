# include <iostream>

using namespace std;

int main()
{
    int num, money;

    int coin25, coin10, coin5, coin1;

    cin >> num;
    for (int i = 0 ; i < num ; i++)
    {
        cin >> money;

        coin25 = money / 25;
        money = money % 25;
        coin10 = money / 10;
        money = money % 10;
        coin5 = money / 5;
        money = money % 5;
        coin1 = money;

        cout << coin25 << " " << coin10 << " " << coin5 << " " << coin1 << '\n';
    }



    return 0;
}