#include<iostream>

using namespace std;
int fibonacci(int n) {
    int* fib = new int[n + 1];
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib[n];
}
int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int n;
        cin >> n;
        int count0 = 1;//0 호출 횟수
        int count1 = 0;//1 호출 횟수
        if (n >= 1) {
            count0 = fibonacci(n - 1); 
            count1 = fibonacci(n); 
        }
        cout << count0 << " " << count1 << endl;
    }
    return 0;
}