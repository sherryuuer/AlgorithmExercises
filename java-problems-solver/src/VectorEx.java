import java.util.Vector;

public class VectorEx {

    public static void main(String[] args) {
        // 创建一个Vector
        Vector<String> vector = new Vector<>();

        // 添加元素
        vector.add("Apple");
        vector.add("Banana");
        vector.add("Cherry");

        // 输出Vector的内容
        System.out.println("Vector elements: " + vector);

        // 获取元素
        String firstElement = vector.get(0);
        System.out.println("First element: " + firstElement); // 输出: Apple

        // 移除元素
        vector.remove(1); // 移除索引为1的元素
        System.out.println("After removal: " + vector); // 输出: [Apple, Cherry]

        // 查找元素是否存在
        boolean containsBanana = vector.contains("Banana");
        System.out.println("Contains Banana? " + containsBanana); // 输出: false

        // 遍历Vector
        for (String fruit : vector) {
            System.out.println(fruit);
        }

        // 获取Vector的大小
        int size = vector.size();
        System.out.println("Vector size: " + size); // 输出: 2

        // 访问第一个和最后一个元素
        System.out.println("First element: " + vector.firstElement()); // 输出: Apple
        System.out.println("Last element: " + vector.lastElement()); // 输出: Cherry

        // 清空Vector
        vector.clear();
        System.out.println("Is vector empty? " + vector.isEmpty()); // 输出: true
    }
}

// 线程安全，动态扩展，允许重复，类似于ArrayList的数组
