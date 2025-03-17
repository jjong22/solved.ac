#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
	int number;
	cin >> number;

	// 1부터 number 까지의 5의 배수의 개수

	int count_5, count_25, count_125;
	count_5 = number / 5;
	count_25 = number / 25;
	count_125 = number / 125;

	cout << count_5 + count_25 + count_125;
}