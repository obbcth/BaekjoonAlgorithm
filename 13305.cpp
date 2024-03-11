#include <iostream>
using namespace std;

int main(){
    int n;
    int city[100000];
    int road[100000];

    cin >> n;

    for (int i=0; i<n-1; i++) {
        cin >> road[i];
    }

    for (int i=0; i<n; i++) {
        cin >> city[i];
    }

    long long min = 1234567890;
    long long answer = 0;

    for (int i=0; i<n-1; i++) {

        if (city[i] < min) {
            min = city[i];
        }

        answer = answer + min * road[i];
    }

    cout << answer << endl;
}
