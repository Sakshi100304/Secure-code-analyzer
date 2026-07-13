import java.util.ArrayList;
 class ArrayList1 {
    public static void main(String args[]){
        ArrayList<String> friend = new ArrayList<String>();
        //add element
        friend.add("Sakshi");
        friend.add("Unesha");
        friend.add("Gayatri");
        System.out.println(friend);
   
        for(int i=0;i<=friend.size();i++){
            System.out.println(friend.get(i));
        }

    }
    
}
