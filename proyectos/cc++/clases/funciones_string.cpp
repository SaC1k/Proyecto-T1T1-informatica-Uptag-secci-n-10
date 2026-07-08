#include<iostream>

int main(){

    std::string nombre;
    nombre = "isaac";
    char pos; char pos1; int ultnum;

    //length longitud total de la cadena de texto
    std::cout << "\n\n"<< nombre<< " longitud de texto es "<< nombre.length();

    //empty valor bool para saber si una cadena esta vacia, 1 en buleano es verdadero, 0 es falso

    std::cout<< "\n\n"<< nombre<< " si esta vacio es 1 si no es 0: "<<nombre.empty();

    //clear  vaciar el cotenido de una variable

    nombre.clear();

    std::cout<<"\n\n"<<nombre<<"oye ve se nos olvido tu nombre wey";

    //append agregar contenido a la variable

    nombre.append("isaac");
    std::cout<<"\n\n"<<nombre<<" oye ya lo encontramos";

    nombre.append("@gmail.com");
    std::cout<<"\n\n"<<nombre<<" mira";    
    
    //at localiza que se encuentra en tal numero de casilla disponible

    nombre= "Isaac";
    
    pos = nombre.at(0);
    pos1= nombre.at(nombre.length() - 1);

    std::cout<<"\n\n"<<nombre<<" oye tu nombre empieza por "<<pos<< " y termina por "<<pos1; 

    //insertar cadena o caracter en una posicion espescifica en la cadena original

    nombre= "isaa";
    std::cout<<"\n\n"<<nombre.insert(4,"c");

    nombre="isaac";

    std::cout<<"\n\n"<<nombre.insert(5," soto");
    //find buscar la primera poscision de la cadena quequeramos buscar

    nombre= "isaac soto";

    std::cout<<"\n\n"<<nombre.find("soto");
    
    //erase borra lo que quieras seleccionar, -1 hasta el ultimo caracter

    std::cout<<"\n\n"<<nombre.erase(5,9);

    std::cout<<"\n\n"<<nombre.erase(5,-1);

    //existen muchos más

    return 0;
}