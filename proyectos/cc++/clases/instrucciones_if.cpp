#include <iostream>
#include <stdio.h>

int main(){
    int edad;

    std::cin >> edad;

    if(edad >= 18){

        std::cout<<"eres un adulto";

    }
    else if(edad <=0){
        std::cout<<"no has nacido";

    }
    else{
        std::cout<<"no eres bienvenido";
    }





    return 0;
}