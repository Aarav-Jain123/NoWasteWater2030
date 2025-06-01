import React, { useState } from 'react'
import Header from './Components/Header'
import Card from './Components/Card'

const Quiz = () => {
  const [lockedIndex, setLockedIndex] = useState(null);

  const options = [
    { text: 'A. H2O' },
    { text: 'B. CO2' },
    { text: 'C. HO2' },
    { text: 'D. Mg' },
  ];

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
