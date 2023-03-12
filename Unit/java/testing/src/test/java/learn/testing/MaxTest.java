package learn.testing;



import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MaxTest {

    @Test
    void testReturnArraysSingleValue() {
        int[] values = new int[]{10};
        int result = Max.max(values);
        assertEquals(values[0], result);
    }

    @Test
    void testReturnMaxForNegativeValues() {
        int[] values = new int[]{-4, -3, -3, -10, -2, -145};
        int result = Max.max(values);
        assertEquals(-2, result);
    }

    @Test
    void testReturnIntegerMaxIfArrayContainsIt() {
        int[] values = new int[]{-10, 3, 255528, 0, Integer.MAX_VALUE, 100, 0};
        int result = Max.max(values);
        assertEquals(Integer.MAX_VALUE, result);
    }

    @Test
    void testReturnsValueNearToIntegerMaxIfArrayContainsIt() {
        int diff = 27;
        int toFind = Integer.MAX_VALUE - diff;
        int[] values = new int[]{8332, 0, -123, 44, 23, 924823, toFind};
        int result = Max.max(values);
        assertEquals(toFind, result);
    }

    @Test
    void testReturnMaxValueForSampleArray() {
        int[] values = new int[]{-574, -484, 444, -217, 978, -370, 269, -9, 189};
        int result = Max.max(values);
        assertEquals(978, result);
    }

    @Test
    void testReturnMaxValueForSampleArray2() {
        int[] values = new int[]{-794, -206, -500, -410, -850, -249, -968, -536, -61, -65, -866};
        int result = Max.max(values);
        assertEquals(-61, result);
    }

    @Test
    void testReturnMaxValueForSampleArray3() {
        int[] values = new int[]{806, 19, 140, 392, 36, 528, 351, 29, 786, 646, 656, 542, 890, 424};
        int result = Max.max(values);
        assertEquals(890, result);
    }
}
