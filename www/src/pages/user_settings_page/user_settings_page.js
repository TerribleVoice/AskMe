//import "./profile.css";
import React, { Component } from 'react'
import Footer from '../../components/main/footer/Footer';
import User_Settings from '../../components/user_settings/user_settings';

export default class User_Settings_Page extends Component {
  render() {
    return (
        <div>
          <div className="container">
          <User_Settings />
          </div>
        <footer className="footer">
          <Footer/>
        </footer>
    </div>
    );
  }
}
