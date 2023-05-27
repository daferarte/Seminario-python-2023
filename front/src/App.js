import React from "react";
import {BrowserRouter, Routes, Route, Link, Outlet, redirect, useNavigate, Navigate, useParams} from 'react-router-dom';

let NotImplemented =()=>{
  return (
    <div>
      <h1>Esta pagina no esta lista</h1>
      <Link to="/">Ir al inicio</Link>
    </div>
  )
}

let Error404 = () =>{
  return (
    <div>
      <h1>Esta pagina no existe</h1>
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

let ProductosEdit = () =>{
  let {id} = useParams();
  let params = useParams();
  console.log(params);

  return(
    <p>
      {id}
    </p>
  )
}

function App() {
  const isAuth = false;
  return (
    <BrowserRouter>
      <Routes>
        
        <Route path="/" element={<NotImplemented/>}/>

        <Route path="/productos" >

          <Route path="add" element={ isAuth ? <Navigate to='/'/> : <NotImplemented/>}/>
          <Route path="edit/:id" element={<ProductosEdit/>}/>
          <Route path="delete" element={<NotImplemented/>}/>
        </Route>

        <Route path="categorias" element={<NotImplemented/>}>
          <Route path="add" element={<NotImplemented/>}/>
          <Route path="edit" element={<NotImplemented/>}/>
          <Route path="delete" element={<NotImplemented/>}/>
        </Route>

        <Route path="*" element={<Error404/>}/>
      </Routes>
      
    </BrowserRouter>
  );
}

export default App;
