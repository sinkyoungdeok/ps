#include <iostream>
#include <string>
#include <queue>
using namespace std;
class comp {
public:
	bool operator()(string a, string b)
	{
		int asum = 0;
		int bsum = 0;
		for (int i = 0; i < a.length(); i++)
		{
			if ('1' <= a[i] && a[i] <= '9')
				asum += a[i] - '0';
		}
		for (int i = 0; i < b.length(); i++)
		{
			if ('1' <= b[i] && b[i] <= '9')
				bsum += b[i] - '0';
		}
		if (a.length() > b.length())
		{
			return true;
		}
		else if (a.length() == b.length())
		{
			if (asum > bsum)
				return true;
			else if (asum == bsum)
			{
				if (a > b)
					return true;
				else
					return false;

			}
			else
				return false;
		}
		else
			return false;
	}
};
int main()
{
	priority_queue <string,vector<string>,comp>pq;
	int num = 0;
	cin >> num;
	for (int i = 0; i < num; i++)
	{
		string a;
		cin >> a;
		pq.push(a);
	}

	for (int i = 0; i < num; i++)
	{
		cout << pq.top() << endl;
		pq.pop();
	}

	return 0;
}