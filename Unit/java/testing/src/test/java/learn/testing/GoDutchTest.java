package learn.testing;


import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class GoDutchTest {

    @Test
    public void testBillWithCorrectData() {
        GoDutch testing = new GoDutch();
        assertEquals(2200, testing.calculateTip(10000, 5));
        assertEquals(5500, testing.calculateTip(5000, 1));
        assertEquals(1, testing.calculateTip(200, 220));
        assertEquals(1, testing.calculateTip(1, 1));
    }

    @Test
    public void testInvalidNumbers() {
        GoDutch testing = new GoDutch();
        assertEquals(-1, testing.calculateTip(100, -2));
        assertEquals(-1, testing.calculateTip(-2, 2));
        assertEquals(-1, testing.calculateTip(-1, 1));

    }
}
