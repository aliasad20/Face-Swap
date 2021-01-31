#include <stdio.h>
int b;
/*void big(int *a){
	int j;
	b = *a;
	printf("%u",*a);
	for(j =1;j<10;j++){
		if(b <= *(++a)){
			b = *a;
		}
	}
}*/

int main(){
	char arr[4];
	printf("Enter 3 letters:");
	for(int i = 0; i<4; i++){
		scanf("%c\n",arr[i]);
		
	}
	for(int i = 0;i<4;i++){
		printf("%u\n", *arr);
		
	}
	return 0;
}
