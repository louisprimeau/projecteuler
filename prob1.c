/* Working Code */

#include <stdio.h>
#include <stdlib.h>


int main(){
  int i;
  int sum = 0;
  for(i=2;i<1000;i++){
    if((i%3==0) || (i%5==0)){
      sum = sum + i;
    }
  }
  printf("%d",sum);
  return(0);
}