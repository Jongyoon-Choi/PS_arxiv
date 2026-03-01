import java.util.Scanner;
import java.math.BigInteger;

class Main {
	public static void main(String[] args) {
		BigInteger n,m;//n은 가진돈, m은 돈 받으러 온 생명체 수
		Scanner sc = new Scanner(System.in);
		n=sc.nextBigInteger();
		m=sc.nextBigInteger();
		System.out.println(n.divide(m)+"\n"+n.remainder(m));
	}
}
