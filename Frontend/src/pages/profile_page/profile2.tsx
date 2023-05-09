//import "./profile.css";
import { Footer } from "@/components/main/footer/Footer";
import { Profile_page2 } from "@/components/AuthorPage/profile_page2";

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

export const Profile2 = () => {
  return (
    <div>
      <div className="container">
        <Profile_page2 />
      </div>
      <footer className="footer">
        <Footer />
      </footer>
    </div>
  );
};
