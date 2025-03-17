#include <iostream>
#include <cstdlib>
#include <queue>

using namespace std;

int main()
{
	int n, won;
	int sum = 0;
	int coin = 0;
	deque<int> de;
	
	cin >> n >> won;

	for (int i = 0; i < n; i++)
	{
		int number;
		cin >> number;
		de.push_front(number);
	}
	
	int won_copy = won;

	while (sum != won)
	{
		if (de.front() > won_copy)
		{
			de.pop_front();
		}
		else
		{
			int mok = won_copy / de.front();
			coin += mok; // 몫을 return
			sum += mok * de.front();
			won_copy = won_copy % de.front();

			if (sum == won)
			{
				break;
			}
			de.pop_front();
		}
	}

	cout << coin;
}