#include <iostream>
#include <string>
#include <queue>
#include <functional>
using namespace std;
int main()
{
	int num = 0;
	char oper;
	int sum = 0;
	int minus_check = 0;
	while (scanf("%d %c", &num, &oper) != EOF)
	{
		if (minus_check) sum -= num;
		else if (!minus_check) sum += num;
		
		if (oper == '-')
			minus_check = true;

	}
	cout << sum << endl;
	return 0;
}