#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int n;
vector<int> scv(3);
int dp[61][61][61];
int INF = 987654321;

int go(int i, int j, int k)
{
    if(i<0) return go(0, j, k);
    if(j<0) return go(i, 0, k);
    if(k<0) return go(i, j, 0);

    if(i == 0 && j == 0 && k == 0) return 0;

    int& ret = dp[i][j][k];

    if(ret != -1) return ret;

    ret = INF;

    ret = min(ret, go(i-9, j-3, k-1) + 1);
    ret = min(ret, go(i-9, j-1, k-3) + 1);

    ret = min(ret, go(i-3, j-9, k-1) + 1);
    ret = min(ret, go(i-3, j-1, k-9) + 1);

    ret = min(ret, go(i-1, j-9, k-3) + 1);
    ret = min(ret, go(i-1, j-3, k-9) + 1);

    return ret;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin>>n;

    for(int i = 0; i<n; ++i) {
        cin>>scv[i];
    }

    memset(dp, -1, sizeof(dp));

    int ans = go(scv[0], scv[1], scv[2]);
    cout<<ans<<'\n';
    return 0;
}