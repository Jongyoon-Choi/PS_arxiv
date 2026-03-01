#include <iostream> 
using namespace std;
int main(){		
	bool prime[246912];
	int n;
	while (true) {
		cin >> n;
		if (n == 0)
			break;
		for (int i = 2; i <= 2 * n; i++)
			prime[i] = true;
		for (int i = 2; i <= 2 * n; i++) {
			if (prime[i]) {
				prime[i] = true;
			}
			for (int j = i + i; j <= 2 * n; j += i) {
				if (prime[j])
					prime[j] = false;
			}
		}
		int count = 0;
		for (int i = n + 1; i <= 2 * n; i++) {
			if (prime[i])
				count++;
		}
		cout << count<<endl;
	}
	return 0;
}