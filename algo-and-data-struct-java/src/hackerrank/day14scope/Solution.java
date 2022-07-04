package day14scope;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Difference {
    private int[] elements;
    public int maximumDifference;

    // Add your code here
    public Difference(final int[] elements) {
        this.elements = elements;
    }

    // находит отличия в введенных из командной строки данных
    public void computeDifference() {
        int max = Arrays.stream(elements).max().getAsInt(); // получаем максимальное значение в массиве
        int min = Arrays.stream(elements).min().getAsInt(); // получаем минимальное значение в массиве
        maximumDifference = max - min ;
    }

    /* Math.abs - модуль числа (абсолютное значение аргумента)
    public void computeDifference(){
        Arrays.sort(elements);
        this.maximumDifference = Math.abs(elements[elements.length - 1] - elements[0]);
    }*/

} // End of Difference class

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.close();

        Difference difference = new Difference(a);

        difference.computeDifference();

        System.out.print(difference.maximumDifference);
    }
}
