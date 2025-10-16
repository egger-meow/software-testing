// Introduction to Software Testing
// Authors: Paul Ammann & Jeff Offutt
// Chapter 3; page ??
// See CalcTest.java, DataDrivenCalcTest.java for JUnit tests

public class Calc
{
   static public int add (int a, int b)
   {
      return a + b;
   }
   
   static public int subtract (int a, int b)
   {
      return a - b;
   }
   
   static public int multiply (int a, int b)
   {
      return a * b;
   }
   
   // Decision: divide returns double for precision
   static public double divide (int a, int b)
   {
      if (b == 0) {
         throw new IllegalArgumentException("Cannot divide by zero");
      }
      return (double) a / b;
   }
}
