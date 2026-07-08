#include <iostream>

int main(){

    /*for(int i = 1; i <= 3; i++){
        
        std::cout<<"\n";
        
        for(int j=1; j<=10;j++){
            std::cout<<j<<" ";
        }

    }*/
   //rectangulo
   int fila; int columnas; char simbolo;

   std::cout<<"fila: ";
   std::cin>>fila;

   std::cout<<"columnas: ";
   std::cin>>columnas;

   std::cout<<"simbolo: ";
   std::cin>>simbolo;

   for(int i = 1; i <= fila; i++){

        for(int i = 1; i <= columnas; i++){
            std::cout<<simbolo<<" ";
        }
        std::cout<<"\n";
   }

    return 0;
}