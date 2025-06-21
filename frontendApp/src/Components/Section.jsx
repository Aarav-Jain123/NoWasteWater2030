import React, { useState, useEffect } from 'react';
import Card from '../Components/Card'
import { getCSRFToken } from '../utils/csrf.js';

const Section = () => {
  const [fact, setFact] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/fact-abt-water/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken()
      },
      // credentials: "include",
      body: JSON.stringify({ key: 0 })
    })
    .then((res) => res.json())
    .then((data) => setFact(data))
  }, []);
  
  console.log(fact)
  return (
    <div>
    {fact.map((a) => (
          <Card text={a.response + '- Filtered by Gemma'} styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-40 border-2"} />
        ))}
    <Card text="Time left till all glacier melts: 75 years (2100 most probably)" styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-40 border-2"} />
    {/* <Card text="Your books" styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-40 border-2"} /> */}
    <Card text="Number of quiz completed" styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-40 border-2"} />
    {/* <Card text="This is a card" />
    <Card text="This is a card" /> */}
    </div>

  )
}

export default Section;
