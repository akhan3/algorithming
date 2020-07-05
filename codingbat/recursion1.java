public class recursion1 {


  public int factorial(int n) {
    return (n == 1) ? 1 : n * factorial(n-1);
  }



  public int bunnyEars(int bunnies) {
    return 2*bunnies;
  }



  public int fibonacci(int n) {
    if (n <= 1)
      return n;
    else
      return fibonacci(n-1) + fibonacci(n-2);
  }


  public int bunnyEars2(int bunnies) {
    if (bunnies == 0)
      return 0;
    else if ((bunnies % 2) == 0)
      return 3 + bunnyEars2(bunnies-1);
    else
      return 2 + bunnyEars2(bunnies-1);
  }



  public int triangle(int rows) {
    if (rows == 0)
      return 0;
    else
      return rows + triangle(rows-1);
  }



  public int sumDigits(int n) {
    if (n == 0)
      return n;
    else
      return n % 10 + sumDigits(n/10);
  }



  public int count7(int n) {
    if (n == 0)
      return 0;
    int a = ((n % 10) == 7) ? 1 : 0;
    return a + count7(n / 10);

  }

}
