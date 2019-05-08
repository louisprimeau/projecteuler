/*working code*/
#include<stdio.h>
int isPrime(int n);
int isPrime(int n){
  int i;
  if(n <= 1){return(0);}
  for(i=2;i<n;i++){
    if(n%i == 0){
      return(0);
    }
  }
  return(1);
}
int main(void){
  int i=1;
  int numprime = 0;
  while(1){
    if(isPrime(i)){
      numprime++;
    }
    if(numprime >= 10001){
      printf("%d",i);
      break;
    }
    i = i + 1;
  }
}
