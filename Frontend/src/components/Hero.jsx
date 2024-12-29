import React from 'react'
import Navbar from './Navbar'

const Hero = () => {
  return (
    <section className='hero'>
        <div className="content">
            <div className="title">
                <h1>WHERE</h1>
                <h1>FLAVORS</h1>
                <h1>COME TO LIFE</h1>
            </div>
            <div className="sub-title">
                <p>Embark on a Journey Through Authentic Tastes & Rich Aromas</p>
                <p>Crafted To Perfection</p>
            </div>
            <div className="buttons">
            <button className="menuBtn" onClick={'/Menu.jsx'}>Discover Menu</button>
            <button className="menuBtn" >Book a Reservation</button>
            </div>
        </div>

    </section>
  )
}

export default Hero