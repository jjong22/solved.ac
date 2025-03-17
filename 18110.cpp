#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <numeric>

using namespace std;
int main()
{
	int number, put;
	float sum = 0;
	float equ;
	vector<int> v1;
	cin >> number;

	for (int i = 0; i < number; i++)
	{
		cin >> put;
		v1.push_back(put);
	}

	equ = float(number) * 15 / 100;
	equ = floor(equ + 0.5); // 내림함수에 0.5를 더해 반올림 함수를 구현

	sort(v1.begin(), v1.end());

	float aver = accumulate(v1.begin()+equ, v1.end()-equ, 0.0) / (v1.size() - 2 * equ);

	equ = floor(aver + 0.5);

	if (number == 0)
	{
		equ = 0;
	}

	cout << int(equ);
}