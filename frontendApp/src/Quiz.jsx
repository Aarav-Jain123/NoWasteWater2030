import React, { useState, useEffect } from 'react'
import Header from './Components/Header'
import Card from './Components/Card'
import { getCSRFToken } from './utils/csrf.js';

const Quiz = () => {
  const [lockedIndex, setLockedIndex] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [options, setOptions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [currentOptions, setCurrentOptions] = useState([]);
  const [currentAnswer, setCurrentAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const []

  const req = fetch("http://127.0.0.1:8000/api/quiz/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCSRFToken()
    },
    // credentials: "include",
    body: JSON.stringify({ key: 0 })
  }).then(res => res.json())
    .then(data => {
        for(let i=0;i<4;i++){
          let question = {
            text: data[0].response[i].question
          }
          setQuestions(questions => [...questions, question]);
          let option = {
            text: data[0].response[i].choices
          }
          setOptions(options => [...options, option]);
        }
    })
    .catch(err => console.log(err));
  
  console.log(req)

  // const options = [
  //   { text: 'A. H2O' },
  //   { text: 'B. CO2' },
  //   { text: 'C. HO2' },
  //   { text: 'D. Mg' },
  // ];

  return (
    <div className="min-h-screen flex flex-col">
      <Header/>
      <div className="flex-1">
        <Card text="Q1. What is the Chemical formula of water?" styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-32 border-2"}/>
        {options.map((option, idx) => (
          <button
            key={idx}
            onClick={() => setLockedIndex(lockedIndex === idx ? null : idx)}
            className={
              "m-4 rounded-lg shadow flex items-center justify-left h-16 w-32 " +
              (lockedIndex === idx
                ? "bg-gray-900"
                : "bg-gray-600 hover:bg-gray-800 active:bg-gray-900")
            }
          >
            {option.text}
          </button>
        ))}
      </div>
      <div className="flex justify-center items-center py-6 bg-white border-t">
        <button
          className="px-8 py-3 bg-blue-600 text-white rounded-lg font-semibold shadow hover:bg-blue-700 transition"
          disabled={lockedIndex === null}
        >
          Submit
        </button>
      </div>
    </div>
  )
}

export default Quiz
