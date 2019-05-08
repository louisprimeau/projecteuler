#include<stdlib.h>
#include<stdio.h>
int toStr(int palindrome, char **store);
int isPalindrome(char *palindrome,int len);
int isPalindrome(char *palindrome, int len){
  int i;
  if((len-1)%2 == 0){
    for(i = 0;i<(len-1)/2;i++){
      if(palindrome[i] != palindrome[len-i]){
        return(0);
      }
    }
  }else{
    for(i=0;i<(int)((len-1)/2);i++){
      if(palindrome[i] != palindrome[len-i]){
        return(0);
      }
    }

  }
  return(1);
}
int toStr(int palindrome, char **store){
  int i = 0;
  int j = 0;
  float logpalindrome = palindrome;
  while(1){
    if(logpalindrome >= 1){
    logpalindrome = logpalindrome/10;
    j++;}else{break;}
  }
  *store = (char *)malloc((sizeof(char) + 1)*j);
  while(1){
    if(palindrome < 1){
      break;
    }
    (*store)[i] = (palindrome % 10) + '0';
    palindrome = (int)(palindrome / 10);
    i++;
  }
  return(j);
}
int main(void){
  int i;
  int len;
  int bigpalindrome = 101;
  char *abc = NULL;
  for(i=101;i<=999;i++){
    len = toStr(i*i,&abc);
    printf("%s\n",abc);
    if(isPalindrome(abc,len)){
      bigpalindrome = i;
    }
    free(abc);
    abc = NULL;
  }
  printf("%d",bigpalindrome);
  return(0);
}
