#include <stdio.h>
#include <stdlib.h>


long fatorial(int n){
	
	double count;
	
	count = n;
	
	if(n == 0){
		return 1;
	}
	
	return n * fatorial(n-1);
}

int fibbonachi(int n){

	if(n == 0){
		return 0;
	}

	if(n == 1){
		return 1;
	}

	return fibbonachi(n-1) + fibbonachi(n-2);

}



public int main(int argc, char *argv[]) {

	//Dps organizar----------------
	
	// int selected;
	
	// printf("Digite o valor para calcular o fatorial:\n");
	
	// scanf("%d", &selected);
	
	// int result = fatorial(selected);
	
	// if(selected == 0 || !selected){
		
	// 	printf("Voce so pode colocar um valor acima de zero e nao nulo");
	// }
	
	// printf("o valor do fatorial sera: %d", result);

	int selected;
	
	printf("Digite a posicao de fibbonachi desejada:\n");
	
	scanf("%d", &selected);
	
	printf("Calculando...\n\n");

	int result = fibbonachi(selected);

	printf(" o valor deu:%d", result);

}

