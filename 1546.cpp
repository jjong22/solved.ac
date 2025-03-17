#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	int n;
	int save;

	float f_save = 0 ;
	float f_sum = 0;

	float equal;

	vector<float> v1, v2;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> save;
		v1.push_back(save);
	}

	sort(v1.begin(), v1.end());

	for (int i = 0; i < n; i++)
	{
		f_save = v1[i] / v1[n-1] * 100;
		v2.push_back(f_save);

		f_sum += f_save;
	}

	equal = f_sum / n;
	
	cout << equal;
}