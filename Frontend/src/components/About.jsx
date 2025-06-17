import React from 'react';
import {Link} from "react-router-dom";
import {HiOutlineArrowNarrowRight} from 'react-icons/hi'
function About() {
  return (
    <section className='about' id='about'>
        <div className="container">
            <div className="banner">
                <img src="/about.png" alt="about" />
            </div>
            <div className="banner">
                <div className="top">
                    <h1 className='heading'>ABOUT US</h1>
                    <p>The only thing we are serious about is food</p>
                </div>
                <p className='mid'>Welcome to <b>Continental Cuisine</b>, where flavors from every corner of the world come together on your plate. Our mission is to take you on a global culinary journey, offering authentic dishes crafted with the finest ingredients and traditional techniques. Whether it’s the bold spices of Asia, the rich flavors of Europe, or the vibrant zest of South America, we serve a taste of every continent, all in one place <br />At <b>Continental Cuisine</b>, we are committed to quality, authenticity, and exceptional service. Join us and explore the world through food, one bite at a time.</p>
                <Link to={"/"}>Explore Menu <span><HiOutlineArrowNarrowRight/></span></Link>
            </div>
        </div>
    </section>
  )
}

export default About