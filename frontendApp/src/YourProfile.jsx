import React, { useState, useEffect } from 'react'
import Header from './Components/Header';
import Footer from './Components/Footer';
import { getCSRFToken } from './utils/csrf.js';


const YourProfile = () => {
  const [userr, setUser] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/your-profile/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
      },
      // credentials: "include",
      body: JSON.stringify({ key: 0 })
    }).then((res) => res.json()).then((data) => {
      setUser(data);
    });
  }, []);

  console.log(userr)

  return (
    <div>
        <Header/>

        <Footer/>
    </div>
  )
}

export default YourProfile;