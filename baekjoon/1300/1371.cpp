#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int check[150];
int main()
{//97~122
	char c;
	int max = 0;
	while (~scanf("%c", &c) ) {
		check[(int)c]++;
	}
	for (int i = 97; i <= 122; i++)
		if (max < check[i])
		{
			max = check[i];
		}
	for (int i = 97; i <= 122; i++)
		if (max == check[i])
		{
			cout << (char)i;
		}
	return 0;
}