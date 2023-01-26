//import "./profile.css";
import React, { Component } from 'react'
import Footer from '../../components/main/footer/Footer';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Profile_page from '../../components/author_page/profile_page';

export default class Profile extends Component {
  render() {
    return (
        <div>
          <div className="container">
          <Profile_page/>
          </div>
        <footer className="footer">
          <Footer/>
        </footer>
    </div>
    );
  }
}
