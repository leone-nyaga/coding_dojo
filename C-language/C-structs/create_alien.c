#include "main.h"

alien create_alien(char *name, int strength, char *planet)
{
    alien a;
    a.name = name;
    a.strength = strength;
    a.planet = planet;
    
    return a;
}
int main() {
    
    alien superman = create_alien("Clark kent", 9000, "Krypton");
    printf("%s %d %s\n", superman.name, superman.strength, superman.planet);


    return 0;
}
