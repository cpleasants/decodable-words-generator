import React from 'react';

const ResponseDisplay = ({ response }) => {
  return (
    <div>
      <h2>Words List</h2>
      {response ? (
        <ul className="response">
            {response["filtered_words"].map(word => <li key={word}>{word}</li>)}
        </ul>
      ) : null}
    </div>
  );
};

export default ResponseDisplay;