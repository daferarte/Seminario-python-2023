import React from "react";

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

function App() {
  return (
    <div >
      <h1>Hola estudiantes</h1>
      <Saludo idioma="es"/>
      <ul>
        {
          nombres.map(nombre => <li>{nombre}</li>)
        }
      </ul>
    </div>
  );
}

export default App;
