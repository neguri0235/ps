#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int n, fr, to, tc;
int dp[2002][2002];

int go(int i, int j, vector<int>&v)
{

    if(i == j) return dp[i][j] = 1;
    if((i+1) == j) return dp[i][j] = (v[i] == v[j]);
    if(dp[i][j] >= 0) return dp[i][j];

    if(v[i] != v[j]) return dp[i][j] = 0;
    else{
        return dp[i][j] = go(i+1,j-1, v);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin>>n;
    vector<int>vec(n);
    for(int i = 0; i<n; ++i) {
        cin>>vec[i];
    }

    memset(dp,-1,sizeof(dp));

    for(int i = 0; i<n; ++i) {
        for(int j = i; j<n; ++j) {
            go(i,j,vec);
        }
    }

    cin>>tc;
    for(int i = 0; i<tc; ++i){
        cin>>fr>>to;
        cout<<dp[fr-1][to-1]<<'\n';
    }

    return 0;
}