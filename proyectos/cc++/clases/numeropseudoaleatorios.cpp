#include <iostream>
#include <ctime>

int main(){
    int us; int num; int usc;char rep = 's';int i=1;
    srand(time(0));
    while(rep = 's'){
        num = rand() % 20 +1;
        std::cout<<"adivina el numero \n";
        do{
            std::cout<<"ingrese el numero: \n";
            std::cin>> us;
            }while(us<= 0||us > 20);
        do{
        
            while(num > us){

                usc=us;

                std::cout<<"el numero es mayor a "<<usc<<"\n";

                std::cin>>us;
                
                (us<= 0||us > 20) ? us = usc : usc = us;
                i++;
                }
            while(num < us){
                usc=us;
                std::cout<<"el numero es menor a "<<usc<<"\n";
                std::cin>>us;
                (us<= 0||us > 20) ? us = usc: usc = us;
                i++;
            }   
        
        }while(num!=us);

        std::cout<<"adivinaste el numero \n"<<"intentos "<<i<<"\n";

        do{
            std::cout<<"quieres volverlo a repetir? \n";
            std::cin>>rep;
        }while(rep !='s' && rep !='n' && rep !='S' && rep !='N');
    }
        return 0;
}