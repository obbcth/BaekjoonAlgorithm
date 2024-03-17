#include <iostream>
using namespace std;

int h[1000001] = {0,};

int main(){
    int n;
    cin >> n;

    int balloon;
    int count = 0;

    for (int i=0; i<n; i++) {
        cin >> balloon;

        if (h[balloon] == 0) {
            h[balloon - 1] += 1;
            count += 1;
        }
        else {
            h[balloon] -= 1;
            h[balloon-1] += 1;
        }
        
    }

    cout << count << endl;
}
