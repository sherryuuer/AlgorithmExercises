import java.util.ArrayList;

public class ArrayListEx {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();

        list.add(10);
        list.add(20);
        list.add(30);
        list.add(40);

        System.out.println(list);

        // get value at index 2
        int value = list.get(2);
        System.out.println("Value at index 2 is " + value);

        // modify value at index 2
        list.set(2, 100);
        System.out.println("Modified index 2 value to 100: " + list);

        // remove value at index 1
        list.remove(1);
        System.out.println("Remove index 1 value: " + list);

        // get the size
        System.out.println("The size of the list is " + list.size());

        // print out all the element
        System.out.println("Print out all the elements: ");
        for (int i : list) {
            System.out.println(i);
        }
    }
}
