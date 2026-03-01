#include<iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    cout << "int a;"<<endl;
    for (int i = 1; i <= N; i++) {
        cout << "int "; 
        for (int j = 0; j < i; j++)
            cout << "*";
        cout << "ptr";
        if (i > 1)
            cout << i;
        if (i == 1)
            cout << " = &a";
        else if(i==2)
            cout << " = &ptr";
        else
            cout << " = &ptr"<<i-1;
        cout << ";"<<endl;
    }
    return 0;
}