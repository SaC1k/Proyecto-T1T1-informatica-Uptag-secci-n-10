#include <stdio.h>
#include <iostream>

int main(){
    char x = 100;

    std::cout<<x;
    int pc = 7;
    int t = 10;
    double puntaje = pc / (double)t * 100;
    std::cout << "\n\n" << puntaje << "%";

    //aceptar entradas
    //operador de insercion cout<< y operador de extracion cin >>
    std::string nombre;
    
    int edad;
    std::cout<< "\n\n" << "how old are you? ";
    
    std::cin >> edad;
    std::cout<< "\n\n" << "cual es tu nombre? ";

    std::getline(std::cin>> std::ws, nombre);

    std::cout << "\n\n" << "bienvenido sea "<<nombre;
    std::cout << "\n\n" << "your age is "<<edad;

    return 0;
}