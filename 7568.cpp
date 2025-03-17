#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	int n;
	cin >> n;

	int a, b;
	int compare[50] = { 0, };
	vector<int> hight, weight, hight_sq, weight_sq, hight_value, weight_value;

	for (int i = 0; i < n; i++)
	{
		cin >> a >> b;
		weight.push_back(a);
		hight.push_back(b);
	}

	int count = 0;

	for (int i = 0; i < n; i++)
	{
		int index = max_element(hight.begin(), hight.end()) - hight.begin();
		int max = *max_element(hight.begin(), hight.end());

		replace(hight.begin(), hight.begin() + index + 1, max, 0);
		hight_sq.push_back(index);
		hight_value.push_back(max);
	}

	compare[hight_sq[0]] = 1;

	// 키가 가장 큰 사람을 1위로 정함.

	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (weight[hight_sq[i]] < weight[hight_sq[j]])
			{
				if (hight_value[i] < hight_value[j])
				{
					count += 1;
				}
			}
		}

		compare[hight_sq[i]] = count + 1;

		count = 0;
	}


	for (int i = 0; i < n; i++)
	{
		cout << compare[i] << " ";
	}
}