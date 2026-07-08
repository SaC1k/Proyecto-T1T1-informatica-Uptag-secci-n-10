#include <cmath>
#include <iostream>

int main(){
    char op; double num1; double num2; double resultado;
    std::cout<<"calculadora\n\n";
    
    std::cout<<"ingrese (+ - * /): "; std::cin>>op;
    
    std::cout<<"\ningrese numero 1: "; std::cin>>num1;
    
    std::cout<<"\ningrese numero 2: "; std::cin>>num2;

    switch (op)
    {
    case '+':
        std::cout<<"\nel resultado es: "<<(num1 + num2);
        break;
    case '-':
        std::cout<<"\nel resultado es: "<<(num1 - num2);
        break;
    case '*':
        std::cout<<"\nel resultado es: "<<(num1 * num2);
        break;
    case '/':
        if(num2 == 0){
            std::cout<<"no se puede dividir entre cero";
        }
        else{
           std::cout<<"\nel resultado es: "<<(num1 / num2);
        }
        break;
    default:
        std::cout<<"\npor favor, ingrese un dato valido (+ - * /)";
        break;
    }
    return 0;
}