//import "./profile.css";
import { Footer } from "@/components/main/footer/Footer";
import { Profile_page1 } from "@/components/AuthorPage/profile_page1";

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

export const Profile1 = () => {
  return (
    <div>
      <div className="container_profile">
        <Profile_page1 />
      </div>
      <footer className="footer">
        <Footer />
      </footer>
    </div>
  );
};
