#include<iostream>
using namespace std;
 
int main(){
    int n;
    cin>>n;
    cin.ignore();
    char nums[n][80];
    for (int i=0;i<n;i++){
        cin.getline(nums[i], 81);
        int sum=0;
        for(int j=0;nums[i][j]=='O'||nums[i][j]=='X';j++){
            if(nums[i][j]=='O'){
                sum++;
                for(char* x=&nums[i][j-1];*x=='O';x--){
                    sum++;
                }
            }
        }
        cout<<sum<<endl;
    }
    //cout<<x<<endl;
    return 0;
}