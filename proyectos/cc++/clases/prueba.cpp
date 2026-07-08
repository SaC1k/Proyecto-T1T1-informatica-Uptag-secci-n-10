#include <iostream>
#include <stdio.h>

 //typedef std::string text_t;
    using text_t = std::string;

    //espacios de nombres, namespace, para tener varia entidades del mismo nombre pero con distintos valores
namespace primero{
  int x = 1;
  int y = 9;
}

namespace segundo{
        int x = 2;
        int y = 7;
}

int main (){

    std::cout<<"hola"<<std::endl;//
    std::cout<<"hola"<<'\n';//
    std::cout<<"hola"<<'\n'<<'\n'<<'\n';//

    /*int x;//declracion
    x = 5;//asignacion
    int entero
    double o flotantes dcecimales
    */

    int d = 67;//ambos
    int yh = 76;
    int suma = d + yh;
    long double pene = 12.3453;

    std::cout<<pene<<'\n'<<'\n'<<'\n';//

    //char characteres
    char hola = 'S';
    std::cout<<hola;//

    //booleanos bool
    bool rata = true;// o false: 1 true 0 false
    std::cout<<'\n'<<rata;

    //string secuencias de textos
    std::string nombre = "isaac";

    std::cout<<'\n'<<'\n'<<"hola"<<nombre;


    //constante solo lectura
    const double PI = 3.14159;
    double radio = 10; 
    const double circunferencia = 2 * PI * radio;

    std::cout<<'\n'<<'\n'<<circunferencia<<" centimetros";

    const int velocidad_yupi = 1237;

    //espacios de nombres, namespace
    using namespace primero;

    int x = 3;
    /* //using namespace std;
    cout<<'\n'<<'\n'<<"x :"<<primero::x<<segundo::x<<x<<'\n'<<"y: "<<segundo::y<<y;
    */

   using std::cout;
    using std::string;
   cout<<'\n'<<"hola";
    string penelan = "penelandia";


    //typedef o usign para ponerle un apodo a un dato

    text_t wan = "pablo";

    //suma + resta - mult * divi/ modulo %
    int estudiantes = 20;
    //estudiantes = estudiantes + 1; todos
    //estudiantes += 1;todos
    estudiantes++;//suma o resta


    //conversion de datos esxpliucita-implicitaa

    /*double xe = (int)8.09;
    std::cout<<xe;*/
    char xe = 100;
    std::cout<<xe;



    return 0;

}
//comentario de una linea+

/*varias lineas waos


waos*/