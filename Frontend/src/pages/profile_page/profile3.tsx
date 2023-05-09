//import "./profile.css";
import { Footer } from "@/components/main/footer/Footer";
import { Profile_page3 } from "@/components/AuthorPage/profile_page3";

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

export const Profile3 = () => {
  return (
    <div>
      <div className="container">
        <Profile_page3 />
      </div>
      <footer className="footer">
        <Footer />
      </footer>
    </div>
  );
};
