import java.util.ArrayList;
import java.util.Collections;
class ArrayLists{
    //ArrayList humesha object ki hoti hai
    public static void main(String args[]){
     ArrayList<Integer> list = new ArrayList<Integer>();
   
       //add elements
       list.add(0);
       list.add(2);
       list.add(3);

       System.out.println(list);
       //get element mein index pass karna padta hai
       int element =  list.get(1);
  
       System.out.println(element);

       //add element in between
       list.add(1,1);
       System.out.println(list);

       //set element
       list.set(0,4);
       System.out.println(list);
       
       //delete element
       list.remove(3);
       System.out.println(list);

       //size
       int size = list.size();
       System.out.println(size);
       
       //loops
       for(int i=0;i<list.size();i++){
        System.out.println(list.get(i));
       }

       //sorting
       Collections.sort(list);
      System.out.println(list);                                                                                                                                                                                                                                                               A``                                           ``                        ``                                                                                                                                                          QAZQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ    Q1                    );


    }

}
