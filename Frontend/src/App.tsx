import { Navigate, Route, Routes } from "react-router-dom";

import "./index.css";
import "./style.css";

import { Main } from "@/pages/main_page/Main";
import { Profile } from "@/pages/profile_page/profile";
import { Profile1 } from "@/pages/profile_page/profile1";
import { Profile2 } from "@/pages/profile_page/profile2";
import { Profile3 } from "@/pages/profile_page/profile3";

import { Layout } from "@/components/Layout";
import { Auth } from "./pages/auth_page/Auth";
import { ProfilePageVa } from "./pages/profile_page/profile_page";
import { UserSettingsPage } from "./pages/user_settings_page/user_settings_page";
import { UserSettingsLayout } from "./pages/user_settings_page/components/UserSettingsLayout";
import { UserSettingsForm } from "./pages/user_settings_page/components/UserSettingsForm";
import { UserSettingsSubscriptions } from "./pages/user_settings_page/components/UserSettingsSubscriptions";

export const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Main />} />
          <Route path=":LoginName" element={<ProfilePageVa />} />
          <Route path="TheOnlyOne1" element={<Profile />} />
          <Route path="ObabMaster" element={<Profile1 />} />
          <Route path="YOUNG77" element={<Profile2 />} />
          <Route path="NeDlaProdagi" element={<Profile3 />} />
          <Route path=":LoginName/settings/" element={<UserSettingsLayout />} >
            <Route index element={<Navigate to={"profile"} replace/>}/>
            <Route path="profile" element={<UserSettingsForm />}/>
            <Route path="subscriptions" element={<UserSettingsSubscriptions/>} />
          </Route>
        </Route>
        <Route path="auth" element={<Auth />} />
      </Routes>
    </>
  );
};
