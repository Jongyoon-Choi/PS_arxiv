#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
	int answer = 0;
	while (section.size()!=0) {
		int start = section[0];
		for (int i = start; i < start+ m; i++) {
			if (section.size() != 0 && section[0] == i)
				section.erase(section.begin());
		}
		answer++;
	}
	return answer;
}