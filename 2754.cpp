#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;
int main()
{
	string str;
	cin >> str;

	float score = 0.0;

	if (str == "A+")
	{
		score = 4.3;
	}
	if (str == "A0")
	{
		score = 4.0;
	}
	if (str == "A-")
	{
		score = 3.7;
	}
	if (str == "B+")
	{
		score = 3.3;
	}
	if (str == "B0")
	{
		score = 3.0;
	}
	if (str == "B-")
	{
		score = 2.7;
	}
	if (str == "C+")
	{
		score = 2.3;
	}
	if (str == "C0")
	{
		score = 2.0;
	}
	if (str == "C-")
	{
		score = 1.7;
	}
	if (str == "D+")
	{
		score = 1.3;
	}
	if (str == "D0")
	{
		score = 1.0;
	}
	if (str == "D-")
	{
		score = 0.7;
	}
	if (str == "F")
	{
		score = 0.0;
	}

	printf("%.1f", score);
}