import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { BackendURL } from "./component/backendURL";
import { Registration } from "./pages/Registration.jsx";
import ModalApproval from "./pages/ModalApproval.jsx";
import Home from "./pages/Home.jsx";
import { Single } from "./pages/single";

import Board from "./pages/Board.jsx";
import Homeadmin from "./pages/Homeadmin.jsx";

import UserRegister from "./pages/UserRegister.jsx";

import injectContext from "./store/appContext";
import Footer from "./component/footer.jsx";
import Homeuser from "./pages/Homeuser.jsx";
import Paneladmin from "./pages/Paneladmin.jsx";
import Modal from "./pages/Modal.jsx";
import ModalgenericP from "./pages/ModalgenericP.jsx";
import Aprobaciones from "./pages/Aprobaciones.jsx";

//create your first component
const Layout = () => {
  //the basename is used when your project is published in a subdirectory and not in the root of the domain
  // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
  const basename = process.env.BASENAME || "";

  if (!process.env.BACKEND_URL || process.env.BACKEND_URL == "")
    return <BackendURL />;

  return (
    <div>
      <BrowserRouter basename={basename}>
        
          <Routes>
            <Route element={<Home />} path="/" />
            <Route element={<Homeuser />} path="/homeuser" />
            <Route element={<Homeadmin />} path="/homeadmin" />
            <Route element={<Registration />} path="/registration" />
            <Route element={<UserRegister />} path="/userRegister" />
            <Route element={<ModalApproval />} path="/modalApprobal" />
            <Route element={<Modal />} path="/modal" />
            <Route element={<ModalgenericP />} path="/modalgeneric" />
            <Route element={<Aprobaciones />} path="/aprobaciones" />
            <Route element={<Board />} path="/board" />
            <Route element={<Paneladmin/>} path="/paneladmin"/>
            <Route element={<Single />} path="/single/:theid" />
            <Route element={<h1>Not found!</h1>} />
          </Routes>
          <Footer />
       
      </BrowserRouter>
    </div>
  );
};

export default injectContext(Layout);
