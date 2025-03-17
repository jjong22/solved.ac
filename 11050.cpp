#include <iostream>
#include <cstdlib>

int factorial(int n);

using namespace std;
int main()
{
	int n, k;
	int sum;

	cin >> n >> k;

	sum = factorial(n) / (factorial(k) * factorial(n-k));
	cout << sum;

}

int factorial(int n)
{
	int result = 1;

	for (int i = 1; i<=n; i++)
	{
		result = result * i;
	}
	return result;
}