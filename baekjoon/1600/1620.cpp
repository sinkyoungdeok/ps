#include <iostream>
#include <string>
#include <queue>
#include <functional>
#include <cstdlib>
#include <map>
using namespace std;
int main()
{
	int a, b;
	scanf("%d %d", &a, &b);
	string *mon = new string[a];
	map<string, int> mon2;
	char tmp[100];
	for (int i = 0; i < a; i++)
	{
		scanf("%s", tmp);
		mon[i] = tmp;
		mon2[mon[i]] = i;
	}

	string search;
	for (int i = 0; i < b; i++)
	{
		scanf("%s", tmp);
		search = tmp;
		if ('0' <= search[0] && search[0] <= '9')
			cout << mon[stoi(search) - 1] << "\n";
		else
			cout << mon2[search] + 1 << "\n";

	}


	return 0;
}