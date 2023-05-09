import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import App from "./App";
import Main from "./pages/main_page/Main";
import Auth from "./pages/auth_page/Auth";
import './index.css';
import './style.css';
import Profile from "./pages/profile_page/profile";
import User_Settings_Page from "./pages/user_settings_page/user_settings_page";
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
                <Route path="/TheOnlyOne1" element={<Profile />} />
            </Route>
            <Route path="" exact element={<App />}>
                <Route path="/user_settings" element={<User_Settings_Page />} />
            </Route>
        </Routes>
    </BrowserRouter>
);
