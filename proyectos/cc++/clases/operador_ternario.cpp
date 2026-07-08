#include <cmath>
#include <iostream>

int main(){

//pérador ternario ?: es una declaracion if_else
// codicion ? expresion 1 (verdadero): expresion2 (falso)

    int calificacion = 5;
    calificacion >= 60 ? std::cout<<"pasas!" : std::cout<<"no pasas";


//ejemplo2

    int numero = 18;

    numero %2 == 0 ? std::cout<<"\n par" : std::cout<<"\n impar";

//ejemplo 2

    bool luz = true;

    luz == false? std::cout<<"\nno hay luz" : std::cout<<"\n hay luz";



    return 0;
}