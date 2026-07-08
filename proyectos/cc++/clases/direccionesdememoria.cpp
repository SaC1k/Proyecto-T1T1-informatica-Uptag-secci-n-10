#include <iostream>

//envio por referencia(memoria)
void cambio(std::string &x, std::string &y);

int main(){
    /*un lugar de la memoria
    std::string nombre ="pepe"; int edad=24; bool gay=true;

    std:: cout << &nombre << "\n";
    std:: cout << &edad << "\n";
    std:: cout << &gay << "\n";

    std:: cout << sizeof(nombre) << "\n";
    std:: cout << sizeof(edad) << "\n";
    std:: cout << sizeof(gay) << "\n";

    */

    std::string x="p";  std::string y="c";

    cambio(x, y);

    std::cout << x<<y;
}


void cambio(std::string &x, std::string &y){

    std::string temp;

    temp= x;    
    x=y;    
    y=temp;
}