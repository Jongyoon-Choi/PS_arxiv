import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int H,M;//H는 시간, M은 분
		Scanner sc = new Scanner(System.in);
		H=sc.nextInt();
		M=sc.nextInt();
		M-=45;
		if (M<0) {
			H-=1;
			M+=60;
			if (H<0){
				H+=24;
			}
		}
		System.out.println(H+" "+M);
	}
}

