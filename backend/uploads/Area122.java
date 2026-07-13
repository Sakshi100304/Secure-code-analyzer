class Area {
// Method to calculate area, to be overridden in subclasses
public void calculateArea()
{
}
}
class AreaCalculator extends Area
{
public void calculateRectangleArea(double length, double width) {
double area = length * width;
System.out.println("Area of the Rectangle: " + area);
}
public void calculateTriangleArea(double base, double height) {
double area = 0.5 * base * height;
System.out.println("Area of the Triangle: " + area);
}
}
public class Area122 {
public static void main(String[] args)
{
AreaCalculator calculator = new AreaCalculator();
calculator.calculateRectangleArea(10, 10);
calculator.calculateTriangleArea(20,15);
}
}