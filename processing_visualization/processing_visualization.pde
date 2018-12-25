// my plans:
// take as input a text file which is outputted by my approximation alg, create vector of values for distance.
// use a loop to draw each circle at certaind distance from each other.
// both circles equidistant from center.


float x;
float y;
 
int value = 1;
int n = 100;

float r = 100;
//Double R = 100;
float d = 50;
//https://stackoverflow.com/questions/4247889/area-of-intersection-between-two-circles
//if(R < r){
    // swap
 //   r = radius2;
 //   R = radius1;
//}
//Double part1 = r*r*Math.acos((d*d + r*r - R*R)/(2*d*r));
//Double part2 = R*R*Math.acos((d*d + R*R - r*r)/(2*d*R));
//Double part3 = 0.5*Math.sqrt((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R));

//Double intersectionArea = part1 + part2 - part3;

double intersectionArea = 2*r*r*Math.acos((d*d)/(2*d*r)) - 0.5*Math.sqrt((-d+2*r)*(d)*(d)*(d+2*r));
// i need to turn this above equation around... take the d's out of it.... fun.

double justnumber = 1;
float m = 0;

void setup (){
  size(1200,800);
  frameRate(10);
  background(100);
  colorMode(HSB);
}
  
void draw(){  
  justnumber++;
    
    rectMode(CENTER);
    fill(0,0,0,0);
    clear();
    
    for( int i = 1; i<100;i++){
      float hue = i*2.55 + m;
      while(hue > 255){hue = hue-255;}
   
      strokeWeight(3);
      stroke(hue,255,255);
//ellipse(mouseX, mouseY, 2.5*i, 2.5*i);
//ellipse(200, 300, 2.5*i, 2.5*i);
//ellipse(mouseX - 5*sin(m), mouseY + m, 3*i, 3*i);
//ellipse(mouseX, mouseY, 6*i, 6*i);
ellipse(600, 400, 6*i, 6*i);
ellipse(600 -40*sin(m/10), 400 + 40*cos(m/10), 6*i, 6*i);
    }
    
    if(m <= 255){m++;}
    else{m = 0;}
 

}

