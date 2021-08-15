#include <iostream>
using namespace std;
int D[1001][1001];
int main()
{
	int N,M,X;
	cin >> N>>M>>X;
	
	
	for(int i=1;i<=N;i++)
	{
		for(int j=1; j<=N;j++)
		{
			if(i!=j)
				D[i][j] = 1000000000;
		}
	}
	
	for(int i=0; i< M;i++)
	{
		int a,b,c;
		cin >> a>>b>>c;
		
		D[a][b] = c;	
	}
	
	for(int k=1; k<=N;k++)
	{
		for(int i=1;i<=N;i++)
		{
			for(int j=1;j<=N;j++)
			{
				D[i][j] = min(D[i][j],D[i][k]+D[k][j]);
			}
		}
	}
	
	int mx= 0;
	for(int i=1; i<=N;i++)
	{
		if(mx < D[i][X] + D[X][i])
			mx = D[i][X] + D[X][i];
	}
	cout << mx << endl;
	
	return 0;
}