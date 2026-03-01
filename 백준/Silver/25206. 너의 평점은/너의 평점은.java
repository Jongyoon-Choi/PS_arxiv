import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		double credit;//학점
		double gradeSum=0.0;//합계
		String grade;//등급
		double creditSum=0;//학점의 합
		for (int i=0; i<20; i++) {
			String subject=sc.next();//과목명
			credit = sc.nextDouble();
			grade=sc.next();
			if (grade.equals("A+")) {
				gradeSum+=credit*4.5;
			}
			else if(grade.equals("A0")) {
				gradeSum+=credit*4.0;
			}
			else if(grade.equals("B+")) {
				gradeSum+=credit*3.5;
			}
			else if(grade.equals("B0")) {
				gradeSum+=credit*3.0;
			}
			else if(grade.equals("C+")) {
				gradeSum+=credit*2.5;
			}
			else if(grade.equals("C0")) {
				gradeSum+=credit*2.0;
			}
			else if(grade.equals("D+")) {
				gradeSum+=credit*1.5;
			}
			else if(grade.equals("D0")) {
				gradeSum+=credit*1.0;
			}
			else if(grade.equals("F")) {
			}
			else {
				continue;//grade==P
			}
			creditSum+=credit;
		}
		System.out.println(gradeSum/creditSum);
    }
}