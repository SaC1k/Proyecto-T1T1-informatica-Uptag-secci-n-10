#include<iostream>

int main(){
    double temp; char op;

    std::cout << "****** convertidor de temperatuara *****\n";

    std::cout<< "F = farenheit \n";
    std::cout<< "C = Celcius \n";

    std::cout<< "que unidad quieres convertir ";

    std::cin >> op;

        if (op =='F' || op =='f'){
            std::cout<< "ingrese el valor en Celsius ";

            std::cin>>temp;
            std::cout<<temp <<"C en farenheit es igual a: "<<(1.8 * temp + 32)<<"F \n";
            }
        else if( op == 'C' || op == 'c'){
            std::cout<< "ingrese el valor en farenheit ";

            std::cin>>temp;

            std::cout<<temp <<"F en celcius es igual a: "<<((temp - 32)/ 1.8)<<"C\n";
        }
        else{
            std::cout<<op<<" no es un caracter valido.\n por favor ingrese un caracter valido \nF = farenheit \nC = Celcius\n";
        }

    std::cout << "****************************************";





    return 0;
}