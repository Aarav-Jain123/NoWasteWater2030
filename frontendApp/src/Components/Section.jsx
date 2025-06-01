import React from 'react'
import Card from '../Components/Card'

const Section = () => {
  return (
    <div>
    <Card text="Fact abt water" styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-40 border-2"} />
    <Card text="Time left till all glacier melts" styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-40 border-2"} />
    <Card text="Your books" styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-40 border-2"} />
    <Card text="Your points" styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-40 border-2"} />
    <Card text="Number of quiz completed" styleTailwind={"m-4 bg-gray-800 rounded-lg shadow flex items-center justify-center h-40 border-2"} />
    {/* <Card text="This is a card" />
    <Card text="This is a card" /> */}
    </div>

  )
}

export default Section;
