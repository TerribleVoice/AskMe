import { Navigate, Route, Routes } from "react-router-dom";

import "./index.css";
import "./style.css";

import { Main } from "@/pages/main_page/Main_Page";
import { Profile } from "@/pages/profile_page/profile";
import { Profile1 } from "@/pages/profile_page/profile1";
import { Profile2 } from "@/pages/profile_page/profile2";
import { Profile3 } from "@/pages/profile_page/profile3";

import { Layout } from "@/components/Layout";
import { Auth } from "./pages/auth_page/Auth_Page";
import { ProfilePageVa } from "./pages/profile_page/Profile_Page";
import { UserSettingsLayout } from "./pages/user_settings_page/components/UserSettingsLayout";
import { UserSettingsForm } from "./pages/user_settings_page/components/UserSettingsForm/UserSettingsForm";
import { UserSettingsSubscriptions } from "./pages/user_settings_page/components/UserSettingsSubscriptions";
import { UserSettingsPayments } from "./pages/user_settings_page/components/UserSettingsPayments";
import { FeedPage } from "./pages/feed_page/Feed_Page";
import { FeedLayout } from "./pages/feed_page/components/FeedLayout";
import { CreateSubscription } from "./pages/profile_page/components/CreateSubscription/CreateSubscription";
import { CreatePost } from "./pages/profile_page/components/CreatePost/CreatePost";
import { CreateDescription } from "./pages/profile_page/components/CreateDescription/CreateDescription";
import { Error_Page } from "./pages/Error_Page";
import { EditSubscription } from "./pages/profile_page/components/EditSubscription/EditSubscription";
import { EditPost } from './pages/profile_page/components/EditPost/EditPost'

export const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Main />} />
          <Route path=":LoginName/">
            <Route index element={<ProfilePageVa />} />
            <Route path="create_description" element={<CreateDescription />} />
            <Route path="create_post" element={<CreatePost />} />
            <Route
              path="create_subscription"
              element={<CreateSubscription />}
            />
            <Route
              path="edit_subscription/:id"
              element={<EditSubscription />}
            />
            <Route 
              path="edit_post/:id"
              element={<EditPost />}
            />
          </Route>
          <Route path="feed" element={<FeedLayout />}>
            <Route index element={<FeedPage />} />
          </Route>
          <Route path="404" element={<Error_Page />} />
          <Route path="TheOnlyOne1" element={<Profile />} />
          <Route path="ObabMaster" element={<Profile1 />} />
          <Route path="YOUNG77" element={<Profile2 />} />
          <Route path="NeDlaProdagi" element={<Profile3 />} />
          <Route path=":LoginName/settings/" element={<UserSettingsLayout />}>
            <Route index element={<Navigate to={"profile"} replace />} />
            <Route path="profile" element={<UserSettingsForm />} />
            <Route
              path="subscriptions"
              element={<UserSettingsSubscriptions />}
            />
            <Route path="payments" element={<UserSettingsPayments />} />
          </Route>
        </Route>
        <Route path="auth" element={<Auth />} />
      </Routes>
    </>
  );
};
