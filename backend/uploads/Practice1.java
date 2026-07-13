import java.util.Scanner;
import java.util.ArrayList;
class Practice1{
    public static void main(String args[]){
        ArrayList<Integer> list1 = new ArrayList<Integer>();
        list1.add(0);
        list1.add(2);
        list1.add(4);
        list1.add(6);
        list1.add(8);
        list1.add(10);
         System.out.println(list1);
         list1.set(2,12);
         System.out.println(list1);
    }
}