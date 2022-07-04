package day6letsreview;

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        for (int i = 0; i < T; i++) {
            String inputString = scan.next();      // input string
            if (inputString.length() > 1) {
                printResult(inputString);
            }
        }
        scan.close();
    }

    public static void printResult(final String inputString){   // create StringBuilder for even and odd
        StringBuilder even = new StringBuilder(); // array for even
        StringBuilder odd = new StringBuilder();  // array for odd
        for (int i =0; i < inputString.length(); i++) {
            char inputStringChar = inputString.charAt(i);   // create char for each inputString index
            if (i % 2 == 0) {
                even.append(inputStringChar);   // add to even array
            } else {
                odd.append(inputStringChar);    // add to odd array
            }
        }
        System.out.printf("%s %s", even, odd);
    }

}
