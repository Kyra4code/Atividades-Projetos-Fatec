#include <stdio.h>
#include <stdlib.h>


//fazer uma soma de n numeros ate q o result seja menor q 4k
int atividade_01(){
	
	int n;
	
	printf("Qual tipo de soma vc gostaria? Exemplo: soma de 2 em 2 e etc\n");

	scanf("%d", &n);
	
	int count = 0;
	int anterior;

	if(n >= 4000){
		printf("Voce digitou: %d", n);
		return 0;
	}
	
	printf("Calculando...");
	
	count = n;
	
	while(count < 4000){
		anterior = count;
		count += anterior;
	}
	
	if(count >= 4000){
		printf("A soma que nao pode exceder 4000 deu: %d (Se somase ficaria: %d)", anterior, anterior + anterior);
		return 0;
	}
	
	printf("A soma deu: %d", count);
	
}

//fazer uma soma sequencial de 1 a 10. Exemplo: 1,2,3...
int atividade_02(){
	
	int soma;
	int i;
	int anterior;
	
	
	for(i = 0; i <= 10; i++){
		soma += i;
	}
	
	printf("A soma de 1 a dez deu: %d", soma);
}

int main(int argc, char *argv[]) {
	
	int response;
	
	printf("Digite 1 para soma de n numeros ate o resultado menor que 4000 ou 2 para soma de 10 numeros consecutivos\n");
	
	scanf("%d", &response);
	
	if(response == 1){
		atividade_01();
	}
	
	else if(response == 2){
		atividade_02();
	}
	else{
		return 0;
	}
	
	return 0;	
}
