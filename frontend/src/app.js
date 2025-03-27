import React from 'react';
import CheckboxGroup from './components/CheckboxGroup';

function App() {
    const letters = ['m', 's', 'r', 't', 'n', 'p', 'o', 'c', 'a', 'd'];
    const groupId = "First Letters"

    return (
        <div>
            <h1>Select Letters</h1>
            <CheckboxGroup letterList={letters} groupId={groupId}/>
        </div>
    )
}

export default App;
