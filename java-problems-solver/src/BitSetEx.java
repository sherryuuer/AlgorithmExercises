import java.util.BitSet;

public class BitSetEx {

    public static void main(String[] args) {
        // 创建一个BitSet，默认所有位都是false
        BitSet bitSet = new BitSet();

        // 设置位: 将索引 0 和索引 2 的位设置为 true
        bitSet.set(0);
        bitSet.set(2);

        // 输出BitSet的内容
        System.out.println("Initial BitSet: " + bitSet); // 输出: {0, 2}

        // 检查某个位的状态
        System.out.println("Is bit at index 2 set? " + bitSet.get(2)); // true
        System.out.println("Is bit at index 1 set? " + bitSet.get(1)); // false

        // 清除位: 将索引 2 的位清除（设为 false）
        bitSet.clear(2);
        System.out.println("After clearing index 2: " + bitSet); // 输出: {0}

        // 翻转位: 翻转索引 0 和 1
        bitSet.flip(0);
        bitSet.flip(1);
        System.out.println("After flipping index 0 and 1: " + bitSet); // 输出: {1}

        // 设置位范围: 将索引 5 到 7 之间的位设置为 true
        bitSet.set(5, 8); // 索引 5, 6, 7 会被设置为 true
        System.out.println("After setting range 5 to 8: " + bitSet); // 输出: {1, 5, 6, 7}

        // 获取集合中true位的数量
        System.out.println("Number of set bits: " + bitSet.cardinality()); // 输出: 4

        // 获取最大位的位置+1
        System.out.println("Length of BitSet: " + bitSet.length()); // 输出: 8

        // 创建另一个 BitSet 进行与运算 (AND)
        BitSet anotherBitSet = new BitSet();
        anotherBitSet.set(1);
        anotherBitSet.set(6);

        // 执行 AND 操作，保留两个BitSet都为 true 的位
        bitSet.and(anotherBitSet);
        System.out.println("After AND operation with anotherBitSet: " + bitSet); // 输出: {1, 6}

        // 执行 OR 操作，将两个 BitSet 中任一为 true 的位设为 true
        bitSet.or(anotherBitSet);
        System.out.println("After OR operation with anotherBitSet: " + bitSet); // 输出: {1, 6}

        // 执行 XOR 操作，将两个 BitSet 中只有一个为 true 的位设为 true
        bitSet.xor(anotherBitSet);
        System.out.println("After XOR operation with anotherBitSet: " + bitSet); // 输出: {}

        // 清除所有位
        bitSet.clear();
        System.out.println("After clearing all bits: " + bitSet); // 输出: {}
    }
}
