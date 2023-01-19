//import "./main_page.css";
import React, { Component } from 'react'
import Ask from '../../components/Ask/Ask';
import Footer from '../../components/main/footer/Footer';
import Let from '../../components/main/let/Let';
import Service from '../../components/service/Service';

export default class Main extends Component {
  render() {
    return (
        <div>
        <div className="container">
          <Ask/>
        </div>
        <Service/>
        <div className="container">
          <Let/>
        </div>
        <footer className="footer">
          <Footer/>
        </footer>
    </div>


    );
  }
}
