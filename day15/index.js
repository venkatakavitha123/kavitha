const todo = JSON.parse(localStorage.getItem("todo"));
if(todo == null)
    todo = []
console.log(todo);

const displayTodo = ()=>{

    const todoContainer = document.getElementById("todo-container");
    todoContainer.innerHTML = "";
    todo.forEach((element, index)=>{
        const todoItem = document.createElement("div");
        todoItem.classList.add("item");
        todoItem.classList.add("pending");
        todoItem.innerText = `${index + 1}. ${element}`;
        
        todoItem.innerHTML = `
        <p>${index + 1}. ${element}</p>
        <select>
            <option>Pending</option>
            <option>Done</option>
        </select>
        `
        todoContainer.append(todoItem);
    })
}