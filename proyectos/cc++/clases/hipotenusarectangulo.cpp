#include <cmath>
#include <iostream>

int main(){
    double a; double b; double c;
    std::cout <<"calcular la hipotenusa de los lados: \nlado a: ";

    std::cin >> a ;

    std::cout << "lado b: ";

    std::cin >> b;
    c = std::hypot(a,b);

    std::cout<< "\n\n la hipotenusa es igual a " << c;

    a = std::pow(a,2);
    b = std::pow(b,2);

    c= std::sqrt(a + b);
    std::cout<< "\n\n la hipotenusa es igual a " << c;

    a = std::sqrt(a);
    b = std::sqrt(b);

    c= std::sqrt(pow(a,2) + pow(b,2));
    std::cout<< "\n\n la hipotenusa es igual a " << c;

    return 0;
}