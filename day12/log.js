playing = true;
learning = true;

if(playing && learning)
{
    console.log("happy to learning and playing")
}
if(playing || learning)
{
    console.log("any one choose")
}
if(!learning)
{
    console.log("another choose playing")
}


let x=10,y=20,z=50;
console.log(x,y,z);
if(x<y && x<z)
{
    console.log("x is smaller")
}
else if(y<x || y<z)
{
    console.log("y is smaller")

}
else if(!z>y)
{
    console.log("not equal")
}
else
{
    console.log("x equal y")
}