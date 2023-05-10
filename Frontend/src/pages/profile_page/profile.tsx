//import "./profile.css";
import { Footer } from "@/components/main/footer/Footer";
import { Profile_page } from "@/components/AuthorPage/profile_page";

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

export const Profile = () => {
  return (
    <div>
      <div className="container">
        <Profile_page />
      </div>
      <footer className="footer">
        <Footer />
      </footer>
    </div>
  );
};
