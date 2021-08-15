#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class segTree
{
public:
	vector<long long> tree;
	long long base;
	segTree(long long a)
	{
		base = 1;
		while(base < a) base <<= 1;
		tree.resize(base*2 + 2,0);
		base --;
	}
	void update(long long idx, long long val)
	{
		idx += base;
		tree[idx] = val;
		idx >>= 1;
		while(idx != 0)
		{
			tree[idx] = tree[idx*2] + tree[idx*2+1];
			idx >>= 1;
		}
	}
	long long query(long long st, long long fn, long long ns=1, long long nf=-1,long long num=1)
	{
		if(nf == -1) nf = base+1;
		
		if(st > nf || ns > fn ) return 0;
		
		if(st <= ns && nf <= fn) return tree[num];
		
		long long mid = (ns+nf) >> 1;
		
		return query(st,fn,ns,mid,num*2) + query(st,fn,mid+1,nf,num*2+1);
	}
	
};


int main(int argc, char* argv[]) 
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	long long N, M;
	cin >> N >> M;
	segTree segtree(N);
	for(long long i=0; i< N;i++)
	{
		long long num;
		cin >> num;
		segtree.update(i+1,num);
	}
	for(long long i=0; i< M; i++)
	{
		long long a,b,c,d;
        cin >> a>>b>>c>>d;
        if(a > b)
            swap(a,b);
        cout << segtree.query(a,b) << '\n';
		segtree.update(c,d);

	}
	
	
	return 0;
}