import java.io.*;
import java.util.*;
import java.util.ArrayList;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class domainName {

    public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String format = "(http|https)\\://(www.|ww2.|)([a-zA-Z0-9\\-\\.]+)(\\.[a-zA-Z]+)(/\\S*)?";
		Pattern pattern = Pattern.compile(format);
		ArrayList<String>links = new ArrayList<String>();
		int testcase = in.nextInt();
		String dec = in.nextLine();
		for(int i = 0;i<testcase;i++){
			String assessed = in.nextLine();
			Matcher match = pattern.matcher(assessed);
			while(match.find()){
					match.groupCount();
					if(links.contains(match.group(3)+match.group(4)) == false){
						links.add(match.group(3)+match.group(4));
					}
			}
		}
		Collections.sort(links);
		for(int j = 0;j<links.size();j++){
			if(j == links.size()-1){
				System.out.println(links.get(j));
			}
			else{
				System.out.print(links.get(j)+";");
			}
		}
    }
}