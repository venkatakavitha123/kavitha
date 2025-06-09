let arr=[1,2,3,4,5,6]
console.log(arr);
console.log(arr.length-1);
console.log(arr.length);

arr.push(8);
arr.push(9);
console.log("after push:",arr)

arr.pop();
console.log("after pop",arr)

arr.shift()
console.log("after shift:",arr)
arr.unshift(7)
console.log("after unshift:",arr)

console.log(arr.includes(2));
console.log(arr.indexOf(2));

console.log(arr.slice(3));
console.log(arr.splice(0,3))



