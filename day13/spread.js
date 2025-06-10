const  obj ={
    name:"shiro",
    age:8
}
//console.log(obj["name"])
//console.log(obj.age)

const userDetails={
    ...obj, 
    isAdminUser:true
}
console.log(userDetails)