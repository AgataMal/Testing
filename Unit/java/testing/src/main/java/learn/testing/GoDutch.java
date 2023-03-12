package learn.testing;

public class GoDutch {

    public int calculateTip(int totalBill, int friendsCount) {

        if (totalBill < 0) {
            System.out.println("Bill total amount cannot be negative");
            return -1;
        }

        if (totalBill == 0) {
            System.out.println("0");
            return -1;
        }

        if (friendsCount > 0) {
            int toPay = totalBill / friendsCount;
            int result = (int) (toPay + 0.1 * toPay);
            return result == 0 ? 1 : result;
        } else {
            System.out.println("Number of friends cannot be negative or zero");
        }
        return -1;
    }
}
