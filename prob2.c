/* Working Code */

#include <stdio.h>
#include <stdlib.h>

int main(){
  int fib1=1;
  int fib2=1;
  int hold;
  int sum = 0;
  while(fib2 < 4000000){
    hold = fib1;
    fib1 = fib1 + fib2;
    if(fib1 % 2 == 0){
      sum = sum + fib1;
    }
    fib2 = hold;
  }
  printf("%d",sum);
  return(0);
}
