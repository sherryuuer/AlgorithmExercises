public class ReverseBits {
    public static int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 8; i++) { // 处理8位
            result <<= 1; // 左移给下一位腾出空间
            result |= (n & 1); // 将n的最低位放入result
            n >>= 1; // 右移n以处理下一位
        }
        return result;
    }

    public static void main(String[] args) {
        int num = 0b11001010; // 8-bit number (202 in decimal)
        int reversed = reverseBits(num);
        System.out.printf("Original: %8s\n", Integer.toBinaryString(num));
        System.out.printf("Reversed: %8s\n", Integer.toBinaryString(reversed));
    }
}

// 反转二进制问题
// reverseBits 方法接收一个8位整数作为输入。
// 循环8次，依次从输入数的最低位开始，通过位操作将其放入结果中。
// 每次处理一位后，将输入数右移，结果数左移。
