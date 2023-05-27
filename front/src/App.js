import React, {useEffect, useState} from "react";

const Form = () =>{
  let [title,setTitle]=useState("");
  let [body,setBody]=useState("");

  const sendForm = (ev) =>{
    ev.preventDefault()

    fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      body: JSON.stringify({
        title: title,
        body: body,
        userId: 1,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
      .then((response) => {
        response.json()
      })
      .then((json) => console.log(json));
  }

  return(
    <form onSubmit={(ev)=>sendForm(ev)}>
      <div>
        <label htmlFor="title">Titulo</label>
        <input type="text" id="title" value={title} onChange={(evt)=>setTitle(evt.target.value)}></input>
      </div>
      <div>
        <label htmlFor="body">Publicacion</label>
        <textarea id="body" onChange={(evt)=>setBody(evt.target.value)}></textarea>
      </div>
      <input type="submit" value="enviar"/>
    </form>
  )
}

function App() {
  
  return (
    <div>
      <Form/>
    </div>
  );
}

export default App;
