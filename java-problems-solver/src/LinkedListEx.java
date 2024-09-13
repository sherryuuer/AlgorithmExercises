import java.util.LinkedList;

public class LinkedListEx {

    public static void main(String[] args) {
        // 创建一个 LinkedList 对象
        LinkedList<String> list = new LinkedList<>();

        // 作为队列使用 (FIFO)
        list.add("A"); // 添加到尾部
        list.add("B");
        list.add("C");

        // 输出队列的内容
        System.out.println("LinkedList as Queue (FIFO): " + list); // 输出: [A, B, C]

        // 移除头部元素
        String firstElement = list.remove(); // 移除并返回头部元素
        System.out.println("Removed first element: " + firstElement); // 输出: A
        System.out.println("LinkedList after remove(): " + list); // 输出: [B, C]

        // 作为栈使用 (LIFO)
        list.push("X"); // 插入到头部
        list.push("Y");
        list.push("Z");

        // 输出栈的内容
        System.out.println("LinkedList as Stack (LIFO): " + list); // 输出: [Z, Y, X, B, C]

        // 弹出栈顶元素
        String poppedElement = list.pop(); // 移除并返回栈顶元素
        System.out.println("Popped element: " + poppedElement); // 输出: Z
        System.out.println("LinkedList after pop(): " + list); // 输出: [Y, X, B, C]

        // 双端队列操作
        list.addFirst("First"); // 插入到头部
        list.addLast("Last"); // 插入到尾部

        // 输出双端队列的内容
        System.out.println("LinkedList as Deque: " + list); // 输出: [First, Y, X, B, C, Last]

        // 移除头部和尾部元素
        String removedFirst = list.removeFirst(); // 移除头部
        String removedLast = list.removeLast(); // 移除尾部
        System.out.println("Removed first element: " + removedFirst); // 输出: First
        System.out.println("Removed last element: " + removedLast); // 输出: Last
        System.out.println("LinkedList after removeFirst() and removeLast(): " + list); // 输出: [Y, X, B, C]
    }
}
