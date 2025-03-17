#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	char board[50][50];
	int chess[8][8];

	// white = 1, black = 0 이라고 생각하자.

	int n, m;
	int count = 0;
	int inner_count = 1;

	int value;
	vector<int> v1;

	cin >> n >> m;

	for (int i = 0; i < n; i++)
	{
		cin >> board[i];
	}

	for (int i = 0; i <= n - 8; i++)
	{
		for (int j = 0; j <= m - 8; j++)
		{
			// 8 * 8 체스판을 가져옵니다.
			for (int k = 0; k < 8; k++)
			{
				for (int l = 0; l < 8; l++)
				{
					if (board[i + k][j + l] == 'W')
					{
						chess[k][l] = 1;
					}
					else
					{
						chess[k][l] = 0;
					}
				}
			}

			if (chess[0][0] != 0)
			{
				chess[0][0] = 0;
				count++;
			}
			// 첫번째 줄 종축 판단
			for (int k = 0; k < 7; k++)
			{
				if (chess[k][0] == (chess[k+1][0]))
				{
					if (chess[k][0] == 1)
					{
						chess[k + 1][0] = 0;
					}
					else
					{
						chess[k + 1][0] = 1;
					}
					count++;
				}

			}
			
			// 횡축 판단
			for (int k = 0; k < 8; k++)
			{
				for (int l = 0; l < 7; l++)
				{
					if (chess[k][l] == (chess[k][l + 1]))
					{
						if (chess[k][l] == 1)
						{
							chess[k][l+1] = 0;
						}
						else
						{
							chess[k][l+1] = 1;
						}
						count++;
					}
				}
			}

			v1.push_back(count);
			count = 0;
		}
	}

	for (int i = 0; i <= n - 8; i++)
	{
		for (int j = 0; j <= m - 8; j++)
		{
			// 8 * 8 체스판을 가져옵니다.
			for (int k = 0; k < 8; k++)
			{
				for (int l = 0; l < 8; l++)
				{
					if (board[i + k][j + l] == 'W')
					{
						chess[k][l] = 1;
					}
					else
					{
						chess[k][l] = 0;
					}
				}
			}

			// 첫번째 줄 종축 판단
			if (chess[0][0] != 1)
			{
				chess[0][0] = 1;
				count++;
			}

			for (int k = 0; k < 7; k++)
			{
				if (chess[k][0] == (chess[k + 1][0]))
				{
					if (chess[k][0] == 1)
					{
						chess[k + 1][0] = 0;
					}
					else
					{
						chess[k + 1][0] = 1;
					}
					count++;
				}

			}

			// 횡축 판단
			for (int k = 0; k < 8; k++)
			{
				for (int l = 0; l < 7; l++)
				{
					if (chess[k][l] == (chess[k][l + 1]))
					{
						if (chess[k][l] == 1)
						{
							chess[k][l + 1] = 0;
						}
						else
						{
							chess[k][l + 1] = 1;
						}
						count++;
					}
				}
			}

			v1.push_back(count);
			count = 0;
		}
	}

	int min = *min_element(v1.begin(), v1.end());
	cout << min;
}