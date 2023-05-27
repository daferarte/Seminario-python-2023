import React from "react";

function Saludo(props){

  if(props.idioma === "es"){
    return(
      <div>
        Como estan?
      </div>
    )
  }else{
    return(
      <div>
        how are you?
      </div>
    )
  }
  
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
