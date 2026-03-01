import java.util.Scanner;

class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();//세로
		int M= sc.nextInt();//가로
		int [][]arr=new int [N][M];//바꿔야할 개수(기본값 0으로 초기화)
		String [] chess= new String[N];
		sc.nextLine();//Buffer
		for (int i=0;i<N;i++) {
			chess[i]=sc.nextLine();
		}
		for(int n=0;n<N;n++) {
			for(int m=0;m<M;m++) {
				if ((n+m)%2==0 && chess[n].substring(m,m+1).equals(chess[0].substring(0,1))) {
					arr[n][m]=0;
				}
				else if ((n+m)%2!=0 && !chess[n].substring(m,m+1).equals(chess[0].substring(0,1))) {
					arr[n][m]=0;
				}
				else arr[n][m]=1;
			}
		}
		int min=32;//다시 칠해야 하는 정사각형 개수의 최소값
		for(int a=0;a<N-7;a++) {
			for(int b=0;b<M-7;b++) {
				int count=0;//다시 칠해야하는 정사각형 개수
				for(int c=0;c<8;c++) {
					for(int d=0;d<8;d++) {
						count+=arr[a+c][b+d];
					}
				}
				if (count>32) count=64-count;
				if (min>count) min=count;
			}
		}
		System.out.println(min);
	}
}