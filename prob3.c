/* Working Code */
#include <stdio.h>
#include <math.h>

int isprime(int pot){
  int i = 0;
  int isprime = 1;
  if(pot % 2 == 0){
    isprime = 0;
  }
  for(i = 3;i<(int)sqrt(pot);i=i+2){
    if(pot % i == 0){
      isprime = 0;
    }
  }
  return(isprime);
}
int main(){
  long number = 600851475143;
  long gd = 0;
  long i;
  printf("%ld\n",(long)sqrt(number));
  for(i = 1; i<775146;i++){
    if((number%i) == 0 && isprime(i)){
      gd = i;
    }
  }
  printf("%ld\n",gd);
  return(0);
}
