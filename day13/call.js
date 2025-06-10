const great=(name,callback)=>{
    console.log(name)
    callback()
}
great("shiro",()=>console.log("hello"))
