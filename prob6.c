/*working code*/
#include<stdio.h>
int main(void){
  int i;
  unsigned long long sum;
  unsigned long long sumsq;
  sum = (100 * 101 / 2)*(100*101/2);
  sumsq = (100 * 101 * 201)/6;
  printf("sum: %lld\n",sum);
  printf("sumsq: %lld\n",sumsq);
  printf("sum - sumsq: %lld\n",(sum - sumsq));
  return(0);
}
