import java.io.*;

class Main {
   public static void main(String[] args) throws IOException{
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      int N = Integer.parseInt(br.readLine());
      int [][] arr;//0=공백 1=*인 배열
      arr= new int [N][N];//NxN배열 생성, 0으로 초기화
      star(arr,0,0,N);
      
      for (int i=0;i<N;i++) {//출력
         for (int j=0;j<N;j++) {
            if (arr[i][j]==1) bw.write('*');
            else bw.write(' ');
         }
         bw.write('\n');
      }
      bw.flush();
      bw.close();
   }
   static void star(int[][]arr, int x, int y, int N){
    if(N>3) {
       for (int i=0;i<3;i++) {
          for (int j=0;j<3;j++) {
             if(i!=1||j!=1) star(arr,3*x+i,3*y+j,N/3);//가운데 빼고 작은 8구역에 별 찍기
          }
       }
    }
    else{//N=3
       for (int i=0;i<3;i++) {
          for (int j=0;j<3;j++) {
             if(i!=1||j!=1) arr[x*3+i][y*3+j]=1;//가운데 빼고 별 찍
          }
       }
       return;
    }
 }
}