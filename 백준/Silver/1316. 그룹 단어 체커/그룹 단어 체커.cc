#include<iostream>
#include<string>
using namespace std;
 
int main(){
    int n;
    cin>>n;
    cin.ignore();
    
    int count=0;
    for (int i=0;i<n;i++){
        string s;
        getline(cin,s);
        bool alphabet[26] = { false, };
        alphabet[(int)s[0] - 97] = true;
        for (int j=1;j<s.length();j++){
            if (s[j]==s[j-1]){
                continue;
            }
            else if (alphabet[(int)s[j]-97]==true){
                count++;//그룹단어 아님
                break;
            }
            else{//등장한 적 없다면
                alphabet[(int)s[j]-97]=true;
            }
        }
    }
    cout<<n-count<<endl;
    return 0;
}