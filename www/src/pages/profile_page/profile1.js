//import "./profile.css";
import React, { Component } from 'react'
import Footer from '../../components/main/footer/Footer';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Profile_page1 from '../../components/author_page/profile_page1';

export default class Profile extends Component {
  render() {
    return (
        <div>
          <div className="container_profile">
          <Profile_page1/>
          </div>
        <footer className="footer">
          <Footer/>
        </footer>
    </div>
    );
  }
}
