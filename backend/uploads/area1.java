public class area1{
 void rect1(){
System.out.println("Enter the area of Rectangle");
}
 void tri1(){
System.out.println("Enter the area of triangle");
}
}
public class Rectangle extends area1{
//public void rect(int a,int b){
//int sum = a*b;
//System.out.println(sum);
//}
}
public class triangle extends area1{
//public void tri(double a,int b,int h){
//int sum = a*b*h;
//System.out.println(sum);

public static void main(String args[]){
Rectangle r = new Rectangle();
triangle t = new triangle();
r.rect1();
//r.rect(2,4);
t.tri1();
//t.tri(0.5,3,4);

}
}
