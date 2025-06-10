const add = (x,y)=> x+y;
const sum = (a,b,callback) =>
{
    x = a+b;
    callback();
    return x;
 
}
console.log(sum(4,5,()=>console.log("calculating.....")));

