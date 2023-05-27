import React from "react";

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
    </div>
  );
}

export default App;
