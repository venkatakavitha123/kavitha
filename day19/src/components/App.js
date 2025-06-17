import logo from './logo.svg';
import React from 'react';
import Forms from './Forms';
import List from './Components/List';

const App = () =>{


//const[players,setPlayer]=useState([]);
   const players=([{name:"virat",age:32,iplteam:"RCB"},
    {name:"MSD",age:38,iplteam:"CSK"},
    {name:"Rohit",age:35,iplteam:"MI"}]);

    <list list={players}/>
    const handlechange=(newplayers)=>{
        players.push(newplayers)
    }

return(
<>
    <div>
        {
            players.map((element,index)=>{
                console.log(element)
            return <div key={index}>
             <h1>{element.name}</h1>
             <p>{element.age}</p>
             <p>{element.iplteam}</p>
            </div>
        
            
            
            })
             
        }
    </div>
    </>
)
}
export default App;