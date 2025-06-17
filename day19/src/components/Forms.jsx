const Forms=(props)=>{

    const handlesubmit=(event)=>{

        event.preventDefault();
        const formobj ={
            name:event.target[0].value,
            age : event.target[1].value,
            iplteam :event.target[2].value
        }
        console.log(formobj);
        props.handlechange(formobj);

        console.log("form submitted");
        console.log(event.target);
    }

    return(

    
        <form onSubmit={handlesubmit}>
            <input type="text" placeholder="enter name"/>
            <input type="number" placeholder="enter age"/>
            <input type="iplteam" placeholder="enter team"/>
            <button type="submit">submit</button>
        </form>
    
    )
}
export default Forms;