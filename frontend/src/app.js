import React, { useState } from 'react';
import PhoneticGroups from './components/PhoneticGroups';
import phonemes from './constants/phonemes';
import ResponseDisplay from './components/ResponseDisplay';
import CheckboxGroup from './components/CheckboxGroup';

function App() {
  const [selected, setSelected] = useState({});
  const [response, setResponse] = useState(null);

  const getSelectedItems = () => { 
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    const checkboxIds = Array.from(checkboxes).map(checkbox => checkbox.id);
    return checkboxIds;
  }

  const generateRequest = () => {
    const checkboxes = getSelectedItems()
    return {
      "hard_consonants" : phonemes["hard_consonants"].filter(s => checkboxes.includes(s)),
      "soft_consonants" : checkboxes.includes("allow_soft_consonants") || checkboxes.includes("cvce") 
        ? phonemes["soft_consonants"].filter(s => checkboxes.includes(s)) : [],
      "short_vowels" : phonemes["short_vowels"].filter(s => checkboxes.includes(s)),
      "long_vowels" : checkboxes.includes("allow_long_vowels") || checkboxes.includes("cvce") 
        ? phonemes["long_vowels"].filter(s => checkboxes.includes(s)) : [],
      "vowel_teams" : phonemes["vowel_teams"].filter(s => checkboxes.includes(s)),
      "digraphs" : phonemes["digraphs"].filter(s => checkboxes.includes(s)),
      "double_letters" : checkboxes.includes("allow_double_consonants") 
        ? phonemes["double_letters"].filter(s => checkboxes.includes(s[0])) : [],
      "prefix_digraphs" : phonemes["prefix_digraphs"].filter(s => checkboxes.includes(s)),
      "prefix_blends" : phonemes["prefix_blends"].filter(s => checkboxes.includes(s)),
      "suffix_blends" : phonemes["suffix_blends"].filter(s => checkboxes.includes(s)),
      "common_endings" : phonemes["common_endings"].filter(s => checkboxes.includes(s)),
      "allow_silent_e" : checkboxes.includes("allow_silent_e"),
      "allow_vc" : checkboxes.includes("vc"),
      "allow_cvc" : checkboxes.includes("cvc"),
      "allow_cvce" : checkboxes.includes("cvce"),
      "allow_cvcvc" : checkboxes.includes("cvcvc"),
      "decodable_only" : true // TODO: how to include non-decodable words? Should I even?
    }
  }

  const handleSubmit = async (event) => {
    event.preventDefault(); // allows me to handle the form submission manually instead of going to default (which is redirect to URL)

    const data = generateRequest();

    try {
      const res = await fetch('http://localhost:8000/filter-words', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), 
      });
      if (!res.ok) {
        throw new Error('Network response was not ok');
      }

      const result = await res.json();
      setResponse(result);
      
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <h1>Word Generator</h1>

        <h2>Select Patterns</h2>
        <CheckboxGroup 
          itemList={["VC", "CVC", "CVCe", "CVCVC"]}
          idList={["vc", "cvc", "cvce", "cvcvc"]}
          selected={selected}
          setSelected={setSelected}
        />

        <h2>Other Parameters</h2>
        <CheckboxGroup 
          itemList={["Long Vowels", "Soft Consonants", "Alternative Vowel Sounds", "Double Consonants", "Silent E"]}
          idList={["allow_long_vowels", "allow_soft_consonants", "allow_alt_vowels", "allow_double_consonants", "allow_silent_e"]}
          selected={selected}
          setSelected={setSelected}
        />

        <h2>Select Letters/Phonemes</h2>
        <PhoneticGroups/>

        <button type="submit">Submit</button>
      </form>

      <ResponseDisplay response={response} />
    </div>
)
}

export default App;

/*
TODO:
- Separate out CheckboxGroup vs CheckboxGroupWithToggle
- Figure out a better way to separate out hte PhoneticGroups (maybe just a different name)
*/