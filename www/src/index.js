import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import App from "./App";
import Main from "./pages/main_page/Main";
import Auth from "./pages/auth_page/Auth";
import './index.css'

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <BrowserRouter>
        <Routes>
            <Route path="" exact element={<App />}>
                <Route path="" element={<Main />} />
            </Route>
            <Route path="/auth" element={<Auth />} />
        </Routes>
    </BrowserRouter>
);
