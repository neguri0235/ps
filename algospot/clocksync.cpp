#include <iostream>
#include <vector>

using namespace std;

const int INF = 9999, SWITCHS = 10, CLOCKS = 16;
const char linked[SWITCHS][CLOCKS+1] = {
    "xxx.............",
    "...x...x.x.x....",
    "....x.....x...xx",
    "x...xxxx........",
    "......xxx.x.x...", 
    "x.x...........xx",
    "...x..........xx",
    "....xx.x......xx",
    ".xxxxx..........",
    "...xxx...x...x.."
};

bool areAligned(const vector<int>& clocks);
void push(vector<int>& clocks, int swtch);
int solve(vector<int>& clocks, int swtch);


int main()
{
    int tc;
    cin>>tc;
    while(tc--) {
        vector<int>clocks(16, 0);
        for(int i = 0; i<16; ++i) {
            cin>>clocks[i];
        }
        int ans = solve(clocks,0);
        if(ans == INF) {
            cout<<-1<<'\n';
        }else{
            cout<<ans<<'\n';
        }
    }
    return 0;
}
bool areAligned(const vector<int>& clocks){
    for(int i = 0; i<clocks.size(); ++i){
        if (clocks[i] != 12) return false;
    }
    return true;
}

void push(vector<int>& clocks, int swtch){
    for(int clock = 0; clock <CLOCKS; ++clock) {
        if(linked[swtch][clock] == 'x'){
            clocks[clock] += 3;
            if(clocks[clock] == 15) clocks[clock] = 3;
        }
    }
}

int solve(vector<int>& clocks, int swtch) {
    if(swtch == SWITCHS) return areAligned(clocks) ? 0 : INF;

    int ret = INF;
    for(int cnt = 0; cnt < 4; ++cnt) {
        ret = min(ret, cnt + solve(clocks, swtch+1));
        push(clocks,swtch);
    }
    return ret;
}