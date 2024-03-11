#include <iostream>
using namespace std;

int main(){
    int n, k;
    int answer = 0;
    int coin[10];

    cin >> n >> k;

    for (int i=0; i<n; i++) {
        cin >> coin[i];
    }

    for (int i=0; i<n; i++) {
        
        if (k >= coin[n-i-1]) {

            // 몫
            answer = answer + k / coin[n-i-1];

            // 나머지
            k = k % coin[n-i-1];
        }
    }

    cout << answer << endl;
}
