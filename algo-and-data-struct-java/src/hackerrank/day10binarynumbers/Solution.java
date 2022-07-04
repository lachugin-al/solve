package day10binarynumbers;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        System.out.println(consecutiveNumber(n));
        scanner.close();
    }

    public static int consecutiveNumber(int n) {
        int count = 0;
        int maxCount = 0;
        while (n > 0) {
            if (n % 2 == 1) {
                count++;
                if (maxCount < count) {
                    maxCount = count;
                }
            } else {
                count = 0;
            }
            n = n >> 1; // сдвиг вправо битов поля первого операнда на количество битов, определяемое вторым операндом (бит знака числа при этом не меняется)
        }
        return maxCount;
    }

}
