#include <iostream>
#include <algorithm>
using namespace std;
bool compare(int a, int b) { return a > b; }
int main()
{
	char *num = new char[11];
	cin >> num;
	int size = 0;
	for (int i = 0; num[i] != NULL; i++)
		size++;
	int *rnum = new int[size];
	for (int i = 0; i<size; i++)
		rnum[i] = num[i] - '0';

	sort(rnum, rnum + size,compare);
	
	for (int i = 0; i < size; i++)
		cout << rnum[i];
	return 0;
}