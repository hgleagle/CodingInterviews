public class Test10Fibonacci {
    public static int Fibonacci1(int n) {
        if (n <= 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        return Fibonacci1(n - 1) + Fibonacci1(n - 2);
    }

    //recommended: Dynamic planning
    public static int Fibonacci2(int n) {
        int prev1 = 1, prev2 = 0, result = 0;

        if (n <= 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }

        for (int i = 2; i <= n; i++) {
            result = prev1 + prev2;
            prev2 = prev1;
            prev1 = result;
            //equals to: prev1 += prev2; prev2 = prev1 - prev2;
        }

        return result;
    }

    public static int Fibonacci3(int n) {
        int[] cache = new int[n + 1];

        if (n <= 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }

        cache[0] = 0;
        cache[1] = 1;
        for (int i = 2; i <= n; i++) {
            cache[i] = cache[i - 1] + cache[i - 2];
        }

        return cache[n];
    }

    public static void main (String[] args) {

        for (int i = 0; i < 10; i++) {
            System.out.println(Fibonacci1(i));
            System.out.println(Fibonacci2(i));
            System.out.println(Fibonacci3(i));
        }
    }
}
