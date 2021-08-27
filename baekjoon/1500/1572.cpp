#include <iostream>
using namespace std;

const int MAX_N =250001;
const int MAX =65535;

long long tree[MAX_N*4], n[MAX_N];

long long update(int index, int target, int value, int start, int end)
{
    if(start >target || target > end )
        return tree[index];
    if(start == end)
        return tree[index] += value;
    long long mid = (start+end)/2;
    return tree[index] = update(index*2, target, value, start, mid) + update(index*2+1,target,value,mid+1,end);
}

long long query(int index, int value, int start, int end)
{
    if( start == end) return start;
    long long mid = (start+ end) / 2;

    if(tree[index*2] >= value ) return query(index*2,value,start, mid);

    return query(index*2+1,value-tree[index*2],mid+1,end);
}

int main()
{  
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int N,K;
    cin >> N >> K;

    for(int i=0; i< N ;i++)
        cin >> n[i];
    
    for(int i=0; i< K-1;i++)
        update(1, n[i],1, 0, MAX);

    long long res = 0;
    for(int i= K-1; i< N;i++)
    {
        update(1, n[i], 1, 0, MAX);
        res += query(1,(K+1)/2,0,MAX);
        update(1,n[i-K+1],-1,0,MAX);
    }
    
    

    cout << res << '\n';





    return 0;
}