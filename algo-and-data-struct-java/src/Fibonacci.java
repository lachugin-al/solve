public class Fibonacci {
    public static void main(String[] args) {
        System.out.println(fibEffective(3));
    }

    public static long fibNaive(int n) {
        // 0 = 0, 1 = 1
        if (n <= 1) {
            return n;
        }

        // рекурсивный вызов по формуле нахождения числа
        return fibNaive(n - 1) + fibNaive(n - 2);
    }

    public static long fibEffective(int n) {
        // создаем массив длинной n + 1;
        long[] arr = new long[n + 1];
        arr[0] = 0;
        arr[1] = 1;

        for (int i = 2; i <= n; i++) {
            arr[i] = arr[i - 1] + arr[i - 2];
        }

        // int n = 3
        // arr[2] = arr[2-1] + arr[2-2] = 1;
        // arr[3] = arr[3-1] + arr[3-2] = 2;

        return arr[n];
    }
}
