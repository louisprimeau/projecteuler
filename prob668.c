#include <stdio.h>
#include <math.h>


int lpf(long long n){
  int largestPrimeFactor;
  if(n % 2 == 0) {
    largestPrimeFactor = 2;
    while(n % 2 == 0){n = n / 2;}
  }
  if(n % 3 == 0) {
    largestPrimeFactor = 3;
    while(n % 3 == 0){n = n / 3;}
  }
  int multOfSix = 6;
  while(multOfSix - 1 <= n) {
    if(n % (multOfSix - 1) == 0) {
        largestPrimeFactor = multOfSix - 1;
	while(n % largestPrimeFactor == 0){n = n / largestPrimeFactor;}
    }
    if(n % (multOfSix + 1) == 0) {
        largestPrimeFactor = multOfSix + 1;
	while(n % largestPrimeFactor == 0){n = n / largestPrimeFactor;}
    }
    multOfSix += 6;
  }
  return(largestPrimeFactor);
}

int main(void){
  long long i = 0;
  long long counter = 0;

  printf("%lld\n",i);
 
  for(i = 4; i <= 1000000; i++){
    if(i%1000 == 0){
      printf("%lld\n",i/1000);
    }
    if(lpf(i) < sqrt(i)){
      counter++;
    }
  }
  printf("%lld\n",counter + 1);
}
