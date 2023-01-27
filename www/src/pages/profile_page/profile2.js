//import "./profile.css";
import React, { Component } from 'react'
import Footer from '../../components/main/footer/Footer';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Profile_page2 from '../../components/author_page/profile_page2';

export default class Profile extends Component {
  render() {
    return (
        <div>
          <div className="container">
          <Profile_page2/>
          </div>
        <footer className="footer">
          <Footer/>
        </footer>
    </div>
    );
  }
}
