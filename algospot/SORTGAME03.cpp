#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

map<vector<int>,int> toSort;

int solve(const vector<int>& perm) {
    int n = perm.size();
    vector<int> fixed(n);
    for(int i = 0; i<n; ++i){
        int smaller = 0; 
        for(int j = 0; j<n; ++j){
            if(perm[i] > perm[j]) smaller += 1;
        }
        fixed[i] = smaller;
    }
    return toSort[fixed];
}


void precalc(const int n) {
    vector<int> perm(n,0);
    for(int i = 0; i<n; i++) perm[i] = i;

    queue<vector<int>> q;
    q.push(perm);
    toSort[perm] = 0;

    while (!q.empty())
    {
        vector<int> here = q.front(); q.pop();
        int cost = toSort[here];
        for (int i = 0; i < n; ++i)
        {
            for (int j = i + 2; j <= n; ++j)
            {
                reverse(here.begin()+i, here.begin()+j);
                if (toSort.count(here) == 0)
                {
                    toSort[here] = cost + 1;
                    q.push(here);
                }
                reverse(here.begin()+i, here.begin()+j);
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    int tc, n;
    cin>>tc;

    for(int i = 1; i<=8; i++) precalc(i);
    while(tc--) {
        cin>>n;
        vector<int> perm(n);
        for(int i = 0; i<n; ++i) cin>>perm[i];

        cout<<solve(perm)<<'\n';
    }
    return 0;
}