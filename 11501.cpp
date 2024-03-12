#include <iostream>
using namespace std;

int price[1000000];

int main() {
    int t, n;
    cin >> t;

    long long answer = 0;
    int max_stock = 0;

    for(int i = 0; i < t ; i++){

        answer = 0;
        max_stock = 0;
        cin >> n;

        for(int day=0; day < n; ++day) {
            cin >> price[day];
        }

        for(int day = n-1 ; day >= 0 ; --day){

            if (price[day] < max_stock) {
                answer += (max_stock - price[day]);
            }
            else {
                max_stock = price[day];
            }

        }

        cout << answer << endl;
    }

    return 0;
}