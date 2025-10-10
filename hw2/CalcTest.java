// Introduction to Software Testing
// Authors: Paul Ammann & Jeff Offutt
// Chapter 3; page ??
// JUnit for Calc.java

import org.junit.*;
import static org.junit.Assert.*;

public class CalcTest
{
   @Test public void testAdd()
   {
      assertTrue ("Calc sum incorrect", 5 == Calc.add (2, 3));
   }
   
   // TDD Step 1: Test for subtract (FAILING TEST)
   @Test public void testSubtract()
   {
      assertTrue ("Calc subtract incorrect", 2 == Calc.subtract (5, 3));
   }
   
   // TDD Step 2: Test for multiply (FAILING TEST)
   @Test public void testMultiply()
   {
      assertTrue ("Calc multiply incorrect", 12 == Calc.multiply (4, 3));
   }
   
   // TDD Step 3: Test for divide (FAILING TEST)
   // Decision: divide returns double for precision
   @Test public void testDivide()
   {
      assertEquals ("Calc divide incorrect", 5.0, Calc.divide (10, 2), 0.001);
   }
   
   // TDD Step 4: Test for divide by zero (edge case)
   @Test(expected = IllegalArgumentException.class)
   public void testDivideByZero()
   {
      Calc.divide (10, 0);
   }
}
