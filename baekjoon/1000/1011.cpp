#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int x, y, result = 1;
		unsigned int diff;
		unsigned int pos = 1;
		cin >> x >> y;
		diff = y - x;
		for (int i = 2; pos < diff ; i++)
		{
			pos += i / 2;
			result++;
		}
		if (pos > diff)
			result--;
		cout << result << endl;


	}

	return 0;
}