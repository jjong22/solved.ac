#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
	int people[50] = {};
	int say = 0;
	int n,number;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> number;
		people[i] = number;
	}

	int size = sizeof(people) / sizeof(*people);

	while (*max_element(people, people + size) != people[0])
	{
		people[max_element(people, people + size) - people] -= 1;
		people[0] += 1;
		say += 1;
	}

	if (count(people, people + size, people[0]) != 1)
	{
		say += 1; // people[0]가 최댓값이지만, 1번의 작업이 더 필요할 때를 제외합니다
	}

	

	cout << say;
}