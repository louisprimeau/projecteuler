#include <stdio.h>
int main(void){
  int i1,i2,i3,i4,i5,i6,i7;
int total = 0;
for(i1 = 0; i1 < 3; i1++){
  for(i2 = 0; i2 < 5; i2++){
    for(i3 = 0; i3 < 11; i3++){
      for(i4 = 0; i4 < 21; i4++){
	for(i5 = 0; i5 < 41; i5++){
	  for(i6 = 0; i6 < 101; i6++){
	    for(i7 = 0; i7 < 201; i7++){
	      if(i1 * 100 + i2 * 50 + i3 * 20 + i4 * 10 + i5 * 5 + i6 * 2 + i7  *1 == 200){
		total += 1; }}}}}}}}

printf("%d",total + 1);

}
