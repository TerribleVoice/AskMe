// import "./App.css";
import React from "react";
import { Outlet } from "react-router-dom";
import Header from "./components/header/Header";

function App() {
    return (
        <div>
            <Header />
            <Outlet />
        </div>
    );
}

export default App;
