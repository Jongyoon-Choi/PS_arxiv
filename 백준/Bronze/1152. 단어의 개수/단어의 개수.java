import java.util.Scanner;
import java.util.StringTokenizer;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String Sentense= sc.nextLine();
		StringTokenizer Words = new StringTokenizer(Sentense," ");
		System.out.println(Words.countTokens());
	}
}