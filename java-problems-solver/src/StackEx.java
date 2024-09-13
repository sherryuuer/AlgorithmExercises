import java.util.Stack;

public class StackEx {

    public static void main(String[] args) {
        // 创建一个 Stack 对象
        Stack<Integer> stack = new Stack<>();

        // 向栈中推入元素
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // 输出栈的内容
        System.out.println("Stack elements: " + stack); // 输出: [10, 20, 30]

        // 查看栈顶元素
        int topElement = stack.peek();
        System.out.println("Top element: " + topElement); // 输出: 30

        // 从栈中弹出元素
        int poppedElement = stack.pop();
        System.out.println("Popped element: " + poppedElement); // 输出: 30
        System.out.println("Stack after pop: " + stack); // 输出: [10, 20]

        // 检查栈是否为空
        boolean isEmpty = stack.empty();
        System.out.println("Is stack empty? " + isEmpty); // 输出: false

        // 查找元素的位置
        int position = stack.search(10); // 位置从1开始计数!!!这好变态
        System.out.println("Position of element 10: " + position); // 输出: 2

        // 继续弹出元素
        stack.pop();
        stack.pop();

        // 检查栈是否为空
        System.out.println("Is stack empty after popping all elements? " + stack.empty()); // 输出: true
    }
}

// Stack 是 Java 中提供的一种 后进先出（LIFO） 的数据结构。它继承了 Vector 类，意味着它也是同步的。
// Stack 类提供了一些用于堆栈操作的基本方法，比如 push()、pop()、peek() 等，常用于实现递归或跟踪执行路径。
