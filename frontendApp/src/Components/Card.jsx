import React from 'react';

export default function Card({text, styleTailwind}) {
  return (
    <div className={styleTailwind}>
      <span className="text-white text-lg font-medium">
        {text}
      </span>
    </div>
  );
}