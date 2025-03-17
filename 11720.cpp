#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>


using namespace std;
int main()
{
	int num;
	string total;
	int sum = 0;

	int save;

	cin >> num;
	cin >> total;

	vector<int> v1;

	for (int i = 0; i < num; i++)
	{
		v1.push_back(total[i]);
	}

	for (int i = 0; i < num; i++)
	{
		sum = sum + v1[i] - 48;  // 아스키 코드에 해당하므로 48을 빼줍니다.
	}
	
	cout << sum;
}