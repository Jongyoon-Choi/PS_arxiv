import java.util.Arrays;
import java.util.Scanner;
import java.math.BigDecimal;

class Main {
	public static void main(String[] args) {
		int subjectnum;
		BigDecimal mean;
		Scanner sc=new Scanner(System.in);
		subjectnum= sc.nextInt();
		BigDecimal []subject= new BigDecimal[subjectnum];
		for (int i=0;i<subjectnum;i++){
			subject[i]=sc.nextBigDecimal();
		}
		Arrays.sort(subject);
		BigDecimal sum=new BigDecimal("0");
		for(BigDecimal n:subject) {
			BigDecimal k=n.divide(subject[subject.length-1],4,BigDecimal.ROUND_HALF_UP);
			k=k.multiply(new BigDecimal("100"));
			sum=sum.add(k);
		}
		mean=sum.divide(new BigDecimal(subject.length),4,BigDecimal.ROUND_DOWN);
		System.out.println(mean);
    }
}