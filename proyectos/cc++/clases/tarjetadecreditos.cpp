#include <iostream>

int main(){
    // 4507 9900 0000 4905
    std::string numero= "4507 9900 0000 4905";
    
    std::cout<<numero<<"\n";


    std::cout<<numero<<"\n";

    for(int i = numero.size()-2; i>=0; i-=2){
        std::cout<<(int)(numero[i]-'0')<<"\n";
    }


    
}