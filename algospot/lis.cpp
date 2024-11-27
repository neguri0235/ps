#include <iostream>
#include <cstring>

using namespace std;

int tc, n, cache[501],S[501];

int lis(const int start ) {
    int& ret = cache[start+1];
    if(ret != -1) return ret;

    ret = 1;
    for(int next = start +1; next <n; ++next) {
        if(start == -1 || S[start] < S[next])
            ret = max(ret, lis(next)+1);
    }
    return ret;
}

int main()
{
    cin>>tc;
    while(tc--) {
        cin>>n;
        memset(cache,-1,sizeof(cache));
        memset(S, -1, sizeof(S));
        for(int i = 0; i<n; i++) {
            cin>>S[i];
        }
        cout<<lis(-1)-1<<'\n';
    }
    return 0;
}