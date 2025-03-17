#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;
int main()
{
	long long int n, m;
	cin >> n >> m;

	long long int k = fabs(n - m);

	cout << k;
}