import { Route, Routes } from "react-router-dom";

import "./index.css";
import "./style.css";

import { Main } from "@/pages/main_page/Main";
import { Auth } from "@/pages/auth_page/Auth";
import { Profile } from "@/pages/profile_page/profile";
import { Profile1 } from "@/pages/profile_page/profile1";
import { Profile2 } from "@/pages/profile_page/profile2";
import { Profile3 } from "@/pages/profile_page/profile3";

import { ScrollUp } from "@/components/scroll/scrollUp";
import { Layout } from "@/components/Layout";

export const App = () => {
  return (
    <>
      <ScrollUp />
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Main />} />
          <Route path="auth" element={<Auth />} />
          <Route path="TheOnlyOne1" element={<Profile />} />
          <Route path="ObabMaster" element={<Profile1 />} />
          <Route path="YOUNG77" element={<Profile2 />} />
          <Route path="NeDlaProdagi" element={<Profile3 />} />
        </Route>
      </Routes>
    </>
  );
};
