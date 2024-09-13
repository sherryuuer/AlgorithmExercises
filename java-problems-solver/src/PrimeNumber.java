import java.util.ArrayList;

public class PrimeNumber {
    public static void main(String[] args) {
        ArrayList<Integer> arr = findPrimeNumber(100);
        System.out.println(arr);
    }

    static ArrayList<Integer> findPrimeNumber(int n) {
        ArrayList<Integer> pnList = new ArrayList<>();

        for (int i = 2; i <= n; i++) {
            boolean divedeFlag = true;
            for (int j = 2; j <= Math.sqrt(i); j++) {
                if (i % j == 0) {
                    divedeFlag = false;
                    break;
                }

            }
            if (divedeFlag == true) {
                pnList.add(i);
            }
        }
        return pnList;
    }
}
