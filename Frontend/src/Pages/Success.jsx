import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { HiOutlineArrowNarrowRight } from 'react-icons/hi';

const Success = () => {
  const [countDown, setCountDown] = useState(10);
  const navigate = useNavigate();

  useEffect(() => {
    const timeoutId = setInterval(() => {
      setCountDown(prevCount => {
        if (prevCount === 1) {
          clearInterval(timeoutId);
          navigate("/");
        }
        return prevCount - 1;
      });
    }, 1000);

    return () => clearInterval(timeoutId);
  }, [navigate]);

  return (
    <section className='notFound'>
      <div className="container">
        <img src="/sandwich.png" alt="success" />
        <h1>Reservation successful! 🎉</h1>
        <h2>Redirecting to Home in {countDown} seconds...</h2>
        <Link to="/">Back to Home <HiOutlineArrowNarrowRight /></Link>
      </div>
    </section>
  );
};

export default Success;
