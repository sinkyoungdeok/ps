#include <iostream>
#include <string>
#include <queue>
#include <set>
using namespace std;
int main()
{
	string input;
	string desti = "123456780";
	
	for (int i = 0; i < 9; i++)
	{
		int num;
		cin >> num;
		input += num + '0';
	}

	queue<string> OPEN;
	set<string> CLOSE;

	OPEN.push(input);
	int cnt = 0;
	int di[4] = { -1,1,0,0 };
	int dj[4] = { 0,0,-1,1 };
	CLOSE.insert(input);
	while (!OPEN.empty())
	{
		int OPEN_size = OPEN.size();
		for (int i = 0; i < OPEN_size; i++)
		{
			string cur = OPEN.front(); OPEN.pop();
			if (cur == desti)
			{
				cout << cnt << endl;
				return 0;
			}
			int current_index;
			for (int j = 0; j < cur.length(); j++)
			{
				if (cur[j] == '0')
				{
					current_index = j;
					break;
				}
			}
			int ci = current_index / 3;
			int cj = current_index % 3;
			for (int d = 0; d < 4; d++)
			{
				int ni = ci + di[d];
				int nj = cj + dj[d];

				if (ni < 0 || ni >= 3 || nj < 0 || nj >= 3)
					continue;

				int next_index = (ni * 3) + nj;

				string next = cur;

				char temp = next[current_index];
				next[current_index] = next[next_index];
				next[next_index] = temp;

				if (CLOSE.find(next) == CLOSE.end())
				{
					OPEN.push(next);
					CLOSE.insert(next);
				}


			}



		}
		cnt++;

	}
	cout << -1 << endl;
	

	return 0;
}