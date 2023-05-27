import { ProfilePage } from "@/pages/profile_page/components/ProfilePage";
import { useLayoutEffect } from "react";

export const ProfilePageVa = () => {
  useLayoutEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  return (
    <div className="container">
      <div className="pp_main">
        <div className="pp_main__container">
          <ProfilePage />
        </div>
      </div>
    </div>
  );
};
