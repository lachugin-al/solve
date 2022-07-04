package problemset;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class CountAndPrintDoubleChar {
    public static void main(String[] args) {
        countAndPrintDoubleCharAndNum("aabbwwe387udhiwjif");
        countChar("baaaqqw");
    }

    public static void countAndPrintDoubleCharAndNum(String str) {
        HashMap<Character, Integer> myHashMap = new HashMap<>();
        char[] temp = str.toCharArray();
        Arrays.sort(temp);
        char tempChar;
        int next = 1;
        int counter = 1;
        if (temp.length > 1) {
            tempChar = temp[0];
            for (int i = next; i < temp.length; i++) {
                if (tempChar == temp[next]) {
                    counter++;
                    myHashMap.put(tempChar, counter);
                    next++;
                } else {
                    myHashMap.put(tempChar, counter);
                    tempChar = temp[next];
                    counter = 1;
                    next++;
                }
            }
        } else {
            System.out.println("");
        }

        printArray(temp);
        for (Map.Entry<Character, Integer> entry : myHashMap.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    private static void countChar(String str) {
        HashMap<Character, Integer> myHashMap2 = new HashMap<>();
        int count = 1;
        for (int i = 0; i < str.length(); i++) {
            if (myHashMap2.containsKey(str.charAt(i))) {
                myHashMap2.put(str.charAt(i), myHashMap2.get(str.charAt(i)) + 1);
            } else {
                myHashMap2.put(str.charAt(i), count);
            }
        }
        for (Map.Entry<Character, Integer> entry : myHashMap2.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    private static void printArray(char[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) {
                System.out.print(", ");
            }
            System.out.print(arr[i]);
        }
        System.out.print("]\n");
    }
}
