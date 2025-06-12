console.log("hai from the js file")
const nameList = [
    "shiro","janu","likky","ramya","shanvi","medha"
]






console.log("hello java script")
console.log("div")

const doc = document.getElementsByTagName("div")
let div = doc[0];
div.textContent = "BVC Testing Python Batch"


const headings=document.getElementsByTagName("h2")
for(i=0;i<headings.length;i++)
headings[i].style.fontStyle="italic"
console.log(headings)

const heading=document.getElementsByTagName("h1");
heading[0].style.fontStyle="Italic"
console.log(heading)


const bye = document.createElement("h2")
bye.textContent = "Bye! Bye!"
document.body.appendChild(bye)


 const adddiv = ()=>{
 const ram = document.createElement("div");
 tx.classList.add("boring");

 const parent = document.getElementById("container");
 tx.textContent = `Test div ${(parent.children.length + 1)}`;
parent.appendChild(ram);
}


 const clicked = ()=>{  
 nameList.push("New Name");
  console.log(nameList)
 }




 const button = document.querySelector("#button1")

button.addEventListener("mouseover" , ()=>{
    button.style.backgroundColor = "pink"
    button.style.scale = 1.2
})

button.addEventListener("mouseout" , ()=>{
    button.style.backgroundColor = "yellowgreen"
    button.style.scale = 0.9
})


button.addEventListener("dblclick" , ()=>{
    console.log("double clicked bro")
})

button.addEventListener("click" , ()=>{
    const newh2 = document.createElement("h2")
    console.log()
    newh2.textContent = document.getElementById("input").value
    document.getElementById("container").appendChild(newh2)
})