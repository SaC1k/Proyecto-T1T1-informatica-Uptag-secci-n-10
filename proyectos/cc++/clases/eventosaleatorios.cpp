#include <iostream>
#include <ctime>

int main(){

    srand(time(0));

    int randNum = (rand() % 5) + 1;  
    
    switch (randNum){

    case 1:
        std::cout<<"ganaste UNA POLLA\n";
        break;
    case 2:
        std::cout<<"ganaste";
        break;
    case 3:
        std::cout<<"ganaste";
        break;
    case 4:
        std::cout<<"ganaste";
        break;
    case 5:
        std::cout<<"ganaste";
        break;
    }
    return 0;
}