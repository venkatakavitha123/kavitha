const add = (x,y)=> x+y;
const sum = (a,b,fun)=>
{
    return fun(a,b);
}
console.log(sum(4,6,add))
