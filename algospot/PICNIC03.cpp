#include <iostream>
#include <vector>
#include <cstring>
#include <cstdlib>

using namespace std;

int tc, n, m;


int pairs(vector<vector<int>>& f, vector<int>& p) {
    int first = -1;
    for (int i=0; i<n; ++i) {
        if (p[i] == 0) {
            first = i;
            break;
        }
    }
    if(first == -1) return 1;

    int ret = 0;

    for(int i = first+1; i<n; ++i) {
        if( f[first][i] == 1 && p[i] == 0) {
            p[first] = p[i] = 1;
            ret += pairs(f,p);
            p[first] = p[i] = 0;
        }
    }
    return ret;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin>>tc;
    while(tc--) {
        cin>>n>>m;
        vector<vector<int>>friends(n, vector<int>(n,0));
        for(int i = 0; i<m; ++i) {
            int fr, to;
            cin>>fr;
            cin>>to;
            friends[fr][to] = friends[to][fr] = 1;
        }
        vector<int> pair(n,0);
        cout<<pairs(friends, pair)<<'\n';
    }
    return 0;
}