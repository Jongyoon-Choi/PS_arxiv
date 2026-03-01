import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int x=sc.nextInt();
		int count=0;
		while(x>0) {
			count++;
			x-=count;
		}
		if (count%2==0) {
			System.out.println((count+x)+"/"+(1-x));
		}
		else {
			System.out.println((1-x)+"/"+(count+x));
		}
	}
}