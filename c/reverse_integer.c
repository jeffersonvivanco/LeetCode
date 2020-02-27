#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

int reverse(int);

int main() {
  printf("12 reversed is %d\n", reverse(12));
  printf("51 reversed is %d\n", reverse(51));
  printf("23 reversed is %d\n", reverse(23));
  printf("132 reversed is %d\n", reverse(132));
  printf("123 reversed is %d\n", reverse(123));
  printf("10 reversed is %d\n", reverse(10));
  printf("20 reversed is %d\n", reverse(20));
  printf("120 reversed is %d\n", reverse(120));
  printf("-123 reversed is %d\n", reverse(-123));
  printf("2 reversed is %d\n", reverse(2));
  printf("123456 reversed is %d\n", reverse(123456));
  printf("1534236469 reversed is %d\n", reverse(1534236469));
  printf("-2147483648 reversed is %d\n", reverse(-2147483648));
}

// given a 32-bit signed integer, reverse digits of an integer.
int reverse(int x){
  int neg = 0;
  int temp;
  if (x < 0) {
    neg = 1;
    // check if its lower or equal to, if so, return 0 cause positive is 1 less than abs(INTEGER_MIN)
    if (x <= INT_MIN) return 0;
    temp = abs(x);
  } else temp = x;
  double b = floor(log10(temp));
  int b_int = (int) b;
  int res = 0;
  while (b_int > 0 && temp > 10) {
    int r = temp % 10;
    int d = temp / 10;
    if (r > 0) {
      res += r * pow(10, b_int);
      temp -= r;
      temp /= 10;
      b_int -= 1;
    } else {
      temp = d;
      b_int -= 1;
    }
  }
  // when number was reversed it was greater than INT_MAX, therefore return 0
  if (res < 0) return 0;
  if (res >= INT_MAX && neg) return 0;
  res += (temp % 10) + (temp / 10);
  return neg ? -res : res;
}
/*
20
*/