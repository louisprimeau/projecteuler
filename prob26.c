
int storedecimal(double decimal, int** expansion){
  *expansion = (int*)malloc(sizeof(int)*20);
  
}
int repeatcounter(int* expansion, int length){

}
int main(void){
  int i;
  double decimal;
  int** expansion;

  for(i=0;i<1000;i++){
    decimal = 1.0 / ((double)i);
    storedecimal(decimal, expansion);
  }

  return(0);
}
