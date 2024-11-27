#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int tc, n, m;
bool friends[10][10];
bool taken[10];


int countPairings_(bool taken[10]) {

    bool finished = true;
    for(int i = 0; i<n; ++i) if(!taken[i]) finished = false;
    if(finished) return 1;

    int ret = 0;

    for(int i = 0; i<n; ++i) {
        for(int j = 0; j<n; ++j) {
            if(!taken[i] && !taken[j] && friends[i][j]) {
                taken[i] = taken[j] = true;
                ret += countPairings_(taken);
                taken[i] = taken[j] = false;
            }
        }
    }
    return ret;
}

int countPairings(bool tabken[10]){
    int firstFree = -1;

    for(int i = 0; i<n; ++i) {
        if(!taken[i]) {
            firstFree = i;
            break;
        }
    }

    if(firstFree == -1) return 1;
    int ret = 0;

    for(int pairWith = firstFree+1; pairWith <n; ++pairWith) {
        if(!taken[pairWith] && friends[firstFree][pairWith]) {
            taken[firstFree] = taken[pairWith] = true;
            ret += countPairings(taken);
            taken[firstFree] = taken[pairWith] = false;
        }
    }
    return ret;
}

int main()
{
    cin>>tc;
    while(tc--){
        cin>>n>>m;
        for(int i = 0; i<10; ++i) taken[i] = false;
        for(int i = 0; i<10; ++i)for(int j = 0; j<10; ++j) friends[i][j] = false;
        for(int i = 0; i<m; ++i) {
           int f, t;
           cin>>f>>t;
           friends[f][t] = true;
           friends[t][f] = true; 
        }


        cout<<countPairings(taken)<<'\n';
    }
    
    return 0;
}