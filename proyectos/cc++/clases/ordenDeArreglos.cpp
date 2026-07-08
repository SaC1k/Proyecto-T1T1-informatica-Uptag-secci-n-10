#include<iostream>

void ordenarArreglo(int arreglo[],int tam);

int main(){
    int cnum;
    std::cout<<"ingrese un numero";
    std::cin>>cnum;
    int num[cnum];
    for(int i=0;i<cnum;i++){
        std::cin>>num[i];           

    }
    std::cout<<"\n\n";
    int tam=sizeof(num)/sizeof(int);
    ordenarArreglo(num,tam);
    for(int elemento:num){
        std::cout<<elemento<<" ";

    }


}



void ordenarArreglo(int arreglo[],int tam){
    int temp;
    for(int i=0;i< tam-1;i++){
        for(int j=0;j<tam-i-1;j++){
            if(arreglo[j]>arreglo[j+1]){
                temp=arreglo[j];
                arreglo[j]=arreglo[j+1];
                arreglo[j+1]=temp;
            }
        }
    }
}
