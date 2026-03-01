#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
	vector<int> answer;
	vector<int> point;
	for (int i = 0; i < park.size(); i++) {
		for (int j = 0; j < park[i].size(); j++) {
			if (park[i][j] == 'S') {
				answer = point = { i,j };
			}
		}
	}
	for (int i = 0; i < routes.size(); i++) {
		int len = routes[i][2] - '0';
		bool pass = true;
		for (int j = 0; j < len; j++) {
			switch (routes[i][0])
			{
			case 'S':
				point[0]++;
				if (point[0] >= park.size() || park[point[0]][point[1]] == 'X') 
					pass = false;
				break;
			case 'N':
				point[0]--;
				if (point[0] < 0 || park[point[0]][point[1]] == 'X')
					pass = false;
				break;
			case 'E':
				point[1]++;
				if (point[1] >= park[0].size() || park[point[0]][point[1]] == 'X') 
					pass = false;
				break;
			case 'W':
				point[1]--;
				if (point[1] < 0 || park[point[0]][point[1]] == 'X') 
					pass = false;
				break;
			default:
				break;
			}
			if (!pass){
				point = answer;
				break;
			}
		}
		if (pass) {
			answer = point;
		}
	}
	return answer;
}