#include <string>

using namespace std;

string solution(string s, string skip, int index) {
	string answer = "";
	string alpha= "abcdefghijklmnopqrstuvwxyz";
	for (int i = 0; i < skip.size(); i++) {
		alpha.erase(alpha.find(skip[i]), 1);
	}
	for (int i = 0; i < s.size(); i++) {
		answer.push_back(alpha[(alpha.find(s[i]) + index)%alpha.size()]);
	}
	return answer;
}