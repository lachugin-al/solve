package problemset;

import java.util.HashSet;
import java.util.Set;

public class CountDoubleChar {
    public static void main(String[] args) {
        countDoubleCharAtString("iwjd  wekskkww");
    }

    public static void countDoubleCharAtString(String str) {
        Set<Character> setChar = new HashSet<>();
        for (int i = 0; i < str.length(); i++) {
            char temp = str.charAt(i);
            for (int y = i + 1; y < str.length(); y++) {
                if (temp == str.charAt(y)) {
                    setChar.add(temp);
                }
            }
        }
        System.out.println(setChar.size());
    }
}
