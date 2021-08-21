#include <iostream>
#include <string>
#include <queue>
#include <functional>
using namespace std;
priority_queue<string, vector<string>, greater<string>> pq;
int main()
{
	int n;
	cin >> n;
	string *book = new string[n];
	int *book_cnt = new int[n];
	int book_i = 0;
	for (int i = 0; i < n; i++)
	{
		string book_name;
		cin >> book_name;
		book_cnt[i] = 0;
		int check = 0;
		for (int j = 0; j < book_i; j++)
			if (book[j] == book_name)
			{
				book_cnt[j]++;
				check = 1;
				break;
			}

		if (check == 0)
		{
			book_cnt[book_i]++;
			book[book_i++] = book_name;
		}
	}
	int mxcnt = 0;
	for (int i = 0; i < book_i; i++)
		if (mxcnt < book_cnt[i])
			mxcnt = book_cnt[i];

	for (int i = 0; i < book_i; i++)
		if (mxcnt == book_cnt[i])
			pq.push(book[i]);

		cout << pq.top() << endl;



	return 0;
}