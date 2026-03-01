import java.util.Scanner;
import java.lang.Math;

class Main {
	public static boolean primenum(int x) {
		for(int i=2;i<=Math.sqrt(x);i++) {
			if (x%i==0) {
				return false;
			}
		}
		return true;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int attempt=sc.nextInt();
		int[] num=new int[attempt];
		for (int i=0;i<attempt;i++) {
			num[i]=sc.nextInt();
		}
		for (int i=0;i<attempt;i++) {
			for (int j=num[i]/2;j>1;j--) {
				if (primenum(j)&primenum(num[i]-j)) {
					System.out.println(j+" "+(num[i]-j));
					break;
				}
			}
		}
	}
}