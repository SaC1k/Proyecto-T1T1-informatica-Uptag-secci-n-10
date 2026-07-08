#include <stdio.h>
#include <iostream>
#include <cmath>

int main(){
    //funciones de matematicas
    //mayor numero y menor numero
    double x = 3.14;
    double y = 3;
    double z;
    double w;
    z = std::max(x,y);
    w = std::min(x,y);
    std::cout << "el numero mayo entre " << x << " y " << y << " es " << z << " y el menor "<< w;

    //cmath
    //elevado, base, exponente
    z = std::pow(2,4);
    std::cout<<"\n\n"<<z;

    //squareroot
    z = std::sqrt(5);
    std::cout<<"\n\n"<<z;
    
    //valor absoluto
    z=std::abs(-3);
    std::cout<<"\n\n"<<z;

    //round redondeado, para bajo si es menor a 5, si es mayor o igual a 5 sube
    z = std::round(x);
    std::cout<<"\n\n"<<z;

    //ceil redondea siempre hacia arriba
    z = std::ceil(x);
    std::cout<<"\n\n"<<z;

    //floor redondea hacia abajo
    z = std::floor(x);
    std::cout<<"\n\n"<<z;

    //funciones de matematicas cmath cplusplus.com/reference/cmath





    return 0;
}