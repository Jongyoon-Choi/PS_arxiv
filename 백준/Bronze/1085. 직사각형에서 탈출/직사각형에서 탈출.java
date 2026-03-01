import java.util.Arrays;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		int x, y, wide, high, shortlength;//x, y는 현재 위치
		Scanner sc = new Scanner(System.in);
		x=sc.nextInt();
		y=sc.nextInt();
		wide=sc.nextInt();
		high=sc.nextInt();
		int array[]= {x, y, wide-x, high-y};
		Arrays.sort(array);
		shortlength=array[0];
		System.out.println(shortlength);
		}
}
