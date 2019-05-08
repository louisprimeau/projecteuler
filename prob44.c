#include<stdio.h>
#include<stdlib.h>
int pent(int n){
  return(n * (3 * n - 1) / 2);
}
int main(void){
  int i = 0;
  int pentag[1000];
  for(i = 1; i < 1000; i++){
    pentag[i] = pent(i);
  }

  
}
