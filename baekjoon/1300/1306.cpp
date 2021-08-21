#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#include <cstring>
using namespace std;
const int MAX = 1000000;
long long tree[MAX * 4];
typedef long long ll;
long long update(long long index, long long target, long long value, long long start, long long end)
{
    if( target< start || target > end) return tree[index];
    if( start == end) return tree[index] = value;
    long long mid = (start+end)/2;
    return tree[index] = max(update(index*2,target,value,start,mid) , update(index*2+1,target,value,mid+1,end) );
}

long long query(long long index, long long left, long long right, long long start, long long end)
{
    if(right < start || end < left) return -1;
    if(left <= start && end <= right) return tree[index];
    long long mid = (start+end)/2;
    return max(query(index*2,left,right,start,mid) , query(index*2+1,left,right,mid+1,end) );
}

int main()
{
	ios_base :: sync_with_stdio(false); 
	cin.tie(NULL); 
	cout.tie(NULL);
    int N,M;
    cin >> N >>M;
    
    memset(tree,INT_MIN,sizeof(tree));

    for(int i=1; i<= N; i++)
    {
        int input;
        cin >> input;
        
        update(1,i,input,1,N);
    }
    
    for(int i=M; i<= N-M+1 ; i++)
    {
        cout << query(1,i-(M-1),i+(M-1),1,N) << ' ';
    }
    cout << '\n';


    return 0;
}