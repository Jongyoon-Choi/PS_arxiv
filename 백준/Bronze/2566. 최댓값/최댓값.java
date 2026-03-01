import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int max=-1;
		int maxi=0;
		int maxj=0;
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++) {
				int num= sc.nextInt();
				if (num>max) {
					max=num;
					maxi=i+1;
					maxj=j+1;
				}
			}
		}
		System.out.println(max);
		System.out.print(maxi+" "+maxj);
	}
}