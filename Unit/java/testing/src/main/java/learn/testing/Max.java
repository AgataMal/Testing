package learn.testing;

public class Max {

    public static int max(int[] values) {
        int max = Integer.MIN_VALUE;
        for (int i : values) {
            if (i > max) {
                max = i;
            }
        }
        return max;
    }
}
