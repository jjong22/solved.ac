#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

int main()
{
	unsigned int arr[8][8];
	unsigned int arr2[8][8];

	char keyboard;

	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			cin >> arr[i][j];
		}
	}

	cin >> keyboard;

	if (keyboard == 'L')
	{
		for (int i = 0; i < 8; i++)
		{
			vector<unsigned int> save, not_0, result;
			unsigned int first;

			for (int j = 0; j < 8; j++)
			{
				save.push_back(arr[i][j]);
			}
			// i번째 줄의 열을 save[]에 저장함

			for (int k = 0; k < 8; k++)
			{
				if (save[k] != 0)
				{
					not_0.push_back(save[k]);
				}
			}
			// save에 저장한 값 중 0을 제외한 값을 not_0에 저장함.

			if (not_0.size() != 0)
			{
				first = not_0[0];

				for (int l = 0; l < not_0.size() - 1; l++)
				{
					unsigned int store = not_0[not_0.size() - 1];

					if (not_0[l] == not_0[l + 1])
					{
						result.push_back(2 * not_0[l]);
						l = l + 1;
					}
					else
					{
						result.push_back(not_0[l]);
					}

					if (l == not_0.size() - 2)
					{
						result.push_back(store);
					}


					// 같은 수가 있을 때 더하는 과정
				}

				if (not_0.size() == 1)
				{
					result.push_back(not_0[0]);
				}

				while (result.size() != 8)
				{
					if (result.size() == 8)
					{
						break;
					}
					result.push_back(0);
				}
			}
			else // 모두 0인 경우에는 사이즈 오류가 나므로 예외 처리 해줍니다.
			{
				for (int m = 0; m < 8; m++)
				{
					result.push_back(0);
				}
			}

			for (int n = 0; n < 8; n++)
			{
				arr2[i][n] = result[n];
			}

		}
	}

	if (keyboard == 'U')
	{
		for (int i = 0; i < 8; i++)
		{
			vector<unsigned int> save, not_0, result;
			unsigned int first;

			for (int j = 0; j < 8; j++)
			{
				save.push_back(arr[j][i]);
			}
			// i번째 줄의 열을 save[]에 저장함

			for (int k = 0; k < 8; k++)
			{
				if (save[k] != 0)
				{
					not_0.push_back(save[k]);
				}
			}
			// save에 저장한 값 중 0을 제외한 값을 not_0에 저장함.

			if (not_0.size() != 0)
			{
				first = not_0[0];

				for (int l = 0; l < not_0.size() - 1; l++)
				{
					unsigned int store = not_0[not_0.size() - 1];

					if (not_0[l] == not_0[l + 1])
					{
						result.push_back(2 * not_0[l]);
						l = l + 1;
					}
					else
					{
						result.push_back(not_0[l]);
					}

					if (l == not_0.size() - 2)
					{
						result.push_back(store);
					}


					// 같은 수가 있을 때 더하는 과정
				}

				if (not_0.size() == 1)
				{
					result.push_back(not_0[0]);
				}

				while (result.size() != 8)
				{
					if (result.size() == 8)
					{
						break;
					}
					result.push_back(0);
				}
			}
			else // 모두 0인 경우에는 사이즈 오류가 나므로 예외 처리 해줍니다.
			{
				for (int m = 0; m < 8; m++)
				{
					result.push_back(0);
				}
			}

			for (int n = 0; n < 8; n++)
			{
				arr2[n][i] = result[n];
			}

		}
	}

	if (keyboard == 'R')
	{
		for (int i = 0; i < 8; i++)
		{
			vector<unsigned int> save, not_0, result;
			unsigned int first;

			for (int j = 7; j >= 0; j--)
			{
				save.push_back(arr[i][j]);  // 오른쪽에 있는 값부터 배열에 저장함.
			}
			// i번째 줄의 열을 save[]에 저장함

			for (int k = 0; k < 8; k++)
			{
				if (save[k] != 0)
				{
					not_0.push_back(save[k]);
				}
			}
			// save에 저장한 값 중 0을 제외한 값을 not_0에 저장함.

			if (not_0.size() != 0)
			{
				first = not_0[0];

				for (int l = 0; l < not_0.size() - 1; l++)
				{
					unsigned int store = not_0[not_0.size() - 1];

					if (not_0[l] == not_0[l + 1])
					{
						result.push_back(2 * not_0[l]);
						l = l + 1;
					}
					else
					{
						result.push_back(not_0[l]);
					}

					if (l == not_0.size() - 2)
					{
						result.push_back(store);
					}


					// 같은 수가 있을 때 더하는 과정
				}

				if (not_0.size() == 1)
				{
					result.push_back(not_0[0]);
				}

				while (result.size() != 8)
				{
					if (result.size() == 8)
					{
						break;
					}
					result.push_back(0);
				}
			}
			else // 모두 0인 경우에는 사이즈 오류가 나므로 예외 처리 해줍니다.
			{
				for (int m = 0; m < 8; m++)
				{
					result.push_back(0);
				}
			}

			for (int n = 0; n < 8; n++)
			{
				arr2[i][n] = result[7-n];
			}

		}
	}

	if (keyboard == 'D')
	{
		for (int i = 0; i < 8; i++)
		{
			vector<unsigned int> save, not_0, result;
			unsigned int first;

			for (int j = 7; j >= 0; j--)
			{
				save.push_back(arr[j][i]);  // 오른쪽에 있는 값부터 배열에 저장함.
			}
			// i번째 줄의 열을 save[]에 저장함

			for (int k = 0; k < 8; k++)
			{
				if (save[k] != 0)
				{
					not_0.push_back(save[k]);
				}
			}
			// save에 저장한 값 중 0을 제외한 값을 not_0에 저장함.

			if (not_0.size() != 0)
			{
				first = not_0[0];

				for (int l = 0; l < not_0.size() - 1; l++)
				{
					unsigned int store = not_0[not_0.size() - 1];

					if (not_0[l] == not_0[l + 1])
					{
						result.push_back(2 * not_0[l]);
						l = l + 1;
					}
					else
					{
						result.push_back(not_0[l]);
					}

					if (l == not_0.size() - 2)
					{
						result.push_back(store);
					}


					// 같은 수가 있을 때 더하는 과정
				}

				if (not_0.size() == 1)
				{
					result.push_back(not_0[0]);
				}

				while (result.size() != 8)
				{
					if (result.size() == 8)
					{
						break;
					}
					result.push_back(0);
				}
			}
			else // 모두 0인 경우에는 사이즈 오류가 나므로 예외 처리 해줍니다.
			{
				for (int m = 0; m < 8; m++)
				{
					result.push_back(0);
				}
			}

			for (int n = 0; n < 8; n++)
			{
				arr2[n][i] = result[7 - n];
			}

		}
	}
	
	
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			cout << arr2[i][j] << " ";
		}
		cout << '\n';
	}

	
	// 이중 반복문을 통해 8 * 8 크기의 게임판을 입력 받음.
}