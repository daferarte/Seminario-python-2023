import React from "react";
import {BrowserRouter, Routes, Route, Link, Outlet, redirect, useNavigate, Navigate} from 'react-router-dom';

let NotImplemented =()=>{
  return (
    <div>
      <h1>Esta pagina no esta lista</h1>
      <Link to="/">Ir al inicio</Link>
    </div>
  )
}

let ProductosOutlet =()=>{
  let navigate = useNavigate();
  let redirect = () =>{
    navigate('/')
  }
  return(
    <>
      <p>hola desde productos</p>
      <button onClick={redirect}>Ir al home</button>
    </>
  )
}

function App() {
  
  return (
    <BrowserRouter>
      <Routes>
        
        <Route path="/" element={<NotImplemented/>}/>

        <Route path="productos" element={<ProductosOutlet/>}>
          <Route path="add" element={<NotImplemented/>}/>
          <Route path="edit" element={<NotImplemented/>}/>
          <Route path="delete" element={<NotImplemented/>}/>
        </Route>

        <Route path="categorias" element={<NotImplemented/>}>
          <Route path="add" element={<NotImplemented/>}/>
          <Route path="edit" element={<NotImplemented/>}/>
          <Route path="delete" element={<NotImplemented/>}/>
        </Route>

      </Routes>
      
    </BrowserRouter>
  );
}

export default App;
