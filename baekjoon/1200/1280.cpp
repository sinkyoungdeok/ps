#include <iostream>
using namespace std;
long long tree1[810000];
long long tree2[810000];
long long update(long long *tree,long long index, long long target, long long value, long long start, long long end)
{
    if( target < start || end < target) return tree[index];
    if(start == end ) return tree[index] += value;
    long long mid = (start+end)/2;
    return tree[index] = update(tree,index*2,target,value,start,mid) + update(tree,index*2+1,target,value,mid+1,end);
}
long long query(long long *tree, long long index, long long left, long long right, long long start, long long end)
{
    if( right < start || end < left) return 0;
    if( left <= start && end <= right) return tree[index];
    long long mid = (start+end)/2;
    return query(tree,index*2,left,right,start,mid) + query(tree,index*2+1,left,right,mid+1,end);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    int n;
    cin >> n;
    update(tree1,1,n,n,0,200000);
    update(tree2,1,n,1,0,200000);
    long long res = 1;
    for(int i=1; i< N; i++)
    {
        cin >> n;

        //cout << query(tree1,1,1,n-1,1,200000) << ' ' << query(tree1,1,n+1,200000,1,200000) <<'\n';

        //cout << (n*query(tree2,1,1,n-1,1,200000))-query(tree1,1,1,n-1,1,200000) << '\n';
        //cout << query(tree1,1,n+1,200000,1,200000) - (n*query(tree2,1,n+1,200000,1,200000)) << '\n';
		
		res *= (((n*query(tree2,1,0,n-1,0,200000))-query(tree1,1,0,n-1,0,200000)) + (query(tree1,1,n+1,200000,0,200000) - (n*query(tree2,1,n+1,200000,0,200000)))) % 1000000007;
        res %= 1000000007;
        update(tree1,1,n,n,0,200000);
        update(tree2,1,n,1,0,200000);
    }
	cout << res << '\n';


    return 0;
}