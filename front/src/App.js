import React, {useState} from "react";

const nombres=["Daniel","Eduardo","Cody","Pepito"];


function Saludo({idioma}){
    return(
      <div>
        {
          idioma==="es" ? <p>Como estan?</p> : <p>How are you?</p>
        }    
      </div>
    )
  
}

const Button = () =>{
  const [conteo, actConteo] = useState(0); //hook
  return(
    <div>
      <p> Precionado: {conteo} </p>
      <button onClick={()=>actConteo(conteo+1)}>Click me!</button>
    </div>
  )
}

function App() {
  return (
    <div >
      <h1>Hola estudiantes</h1>
      <Saludo idioma="es"/>
      <ul>
        {
          nombres.map((nombre,index) => <li key={index}>{nombre}</li>)
        }
      </ul>
      <Button/>
    </div>
  );
}

export default App;
