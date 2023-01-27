import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import App from "./App";
import Main from "./pages/main_page/Main";
import Auth from "./pages/auth_page/Auth";
import './index.css';
import './style.css';
import Profile from "./pages/profile_page/profile";
import ScrollUp from "./components/scroll/scrollUp"

const root = ReactDOM.createRoot(document.getElementById("root"));
const PrivateRoute = ({ component: Component, ...rest}) => {

}
root.render(
    <BrowserRouter>
        <ScrollUp />
        <Routes>
            <Route path="" exact element={<App />}>
                <Route path="" element={<Main />} />
            </Route>
            <Route path="/auth" element={<Auth />} />
            <Route path="" exact element={<App />}>
                <Route path="/profile" element={<Profile />} />
            </Route>
        </Routes>
    </BrowserRouter>
);
