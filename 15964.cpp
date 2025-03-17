#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
	long long int a, b;
	cin >> a >> b;

	long long int result = (a + b) * (a - b);

	cout << result;
}