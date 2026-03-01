import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String str=sc.nextLine();
		List<String> strs = new ArrayList<String>();
		for (int i=1;i<=str.length();i++) {
			for (int j=0;j<i;j++) {
				strs.add(str.substring(j,i));
			}
		}
		List<String> newList = strs.stream().distinct().collect(Collectors.toList());
		System.out.println(newList.size());
	}
}