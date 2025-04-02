import React from 'react';

const ResponseDisplay = ({ apiResponse, restart }) => {
  return (
    <div>
      
      <h2>Words List</h2>
      {apiResponse ? (
        <ul className="response">
            {apiResponse["filtered_words"].map(word => <li key={word}>{word}</li>)}
        </ul>
      ) : null}
      <div className='button-footer'>
        <button onClick={restart}>Start Over</button>
      </div>
    </div>
    
  );
};

export default ResponseDisplay;