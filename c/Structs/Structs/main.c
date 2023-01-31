#include <stdio.h>
#include <stdlib.h>
struct geofix{
        float latitude;
    float longitude;
};

struct location{
    char* description;
    struct geofix pos;

}home_location ={"Home",400.00,500.55},
cur_location = {"Shop",400.4343,245.324};


void foo (struct location myloc){
if((myloc.description != NULL )&& !strcmp(myloc.description,"Newcastle")){
    printf("Home\n");
    myloc.pos.latitude =0.0;
    myloc.pos.longitude=0.0;
}
}

struct location fooo (char* req){
    struct location locc;
    if(!strcmp(req,"home")){
        locc = home_location;
    }else{
    locc = cur_location;
    }
    return locc;

}


int main()
{
    struct location my_college = {{"Newcastle"},{4.3,6.5}};
    struct location my_loc;
    my_loc = fooo("current");

    printf("Come visit %s at geo: %f,%f \n",
           my_loc.description,
           my_loc.pos.latitude,
           my_loc.pos.longitude);
}
