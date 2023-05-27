import React from "react";

const nombres=["Daniel","Eduardo","Cody","Pepito"];

function getNombres(){
  const elementosLista=[];
  for(let i=0;i<nombres.length;i++){
    elementosLista.push(<li>{nombres[i]}</li>);
  }

  console.log(elementosLista);
  return elementosLista;
}

function Saludo({idioma}){
    return(
      <div>
        {
          idioma==="es" ? <p>Como estan?</p> : <p>How are you?</p>
        } 
        <ul>{getNombres()}</ul>       
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
