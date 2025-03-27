import React, { useState } from 'react';
import CheckboxGroupContainer from './components/CheckboxGroupContainer';

const phonemes = {
  "hard_consonants": ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "y", "z"],
  "soft_consonants": ["c", "g"],
  "short_vowels": ["a", "e", "i", "o", "u"],
  "long_vowels": ["a", "e", "i", "o", "u"],
  "secondary_vowel_pronunciations": ["a", "e", "o", "i"],
  "secondary_consonant_pronunciations": ["t"],
  "vowel_teams": ["ee", "ea", "ai", "ay", "oa", "ow", "igh"],
  "digraphs": ["ow", "ch", "th", "ng", "oy", "sh", "qu", "ck", "wh", "er", "xc"],
  "double_letters": ["aa", "bb", "cc", "dd", "ff", "gg", "jj", "kk", "ll", "mm", "nn", "pp", "rr", "ss", "tt", "xx", "zz"],
  "prefix_digraphs": ["wr-", "kn-", "ph-", "gh-", "gn-"],
  "prefix_blends": ["bl-", "cl-", "fl-", "gl-", "pl-", "sl-", "br-", "cr-", "dr-", "fr-", "gr-", "pr-", "tr-", "sc-", "shr-", "sk-", "sm-", "sn-", "sp-", "squ-", "st-", "sw-"],
  "suffix_blends": ["-lp", "-st", "-ct", "-pt", "-sk", "-lk", "-lf", "-xt", "-ft", "-nd", "-mp", "-lt", "-nch", "-mb", "-tch", "-dge"],
  "common_endings": ["-ing", "-ang", "-ong", "-ung", "-ank", "-ink", "-onk", "-unk", "-oe", "-ed", "-ard", "-y"]
}


function App() {
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
      "soft_consonants" : checkboxes.includes("allow_soft_consonants") ? phonemes["soft_consonants"].filter(s => checkboxes.includes(s)) : [],
      "short_vowels" : phonemes["short_vowels"].filter(s => checkboxes.includes(s)),
      "long_vowels" : checkboxes.includes("allow_long_vowels") ? phonemes["long_vowels"].filter(s => checkboxes.includes(s)) : [],
      "vowel_teams" : phonemes["vowel_teams"].filter(s => checkboxes.includes(s)),
      "digraphs" : phonemes["digraphs"].filter(s => checkboxes.includes(s)),
      "double_letters" : checkboxes.includes("allow_double_consonants") ? phonemes["double_letters"].filter(s => checkboxes.includes(s[0])) : [],
      "prefix_digraphs" : phonemes["prefix_digraphs"].filter(s => checkboxes.includes(s)),
      "prefix_blends" : phonemes["prefix_blends"].filter(s => checkboxes.includes(s)),
      "suffix_blends" : phonemes["suffix_blends"].filter(s => checkboxes.includes(s)),
      "common_endings" : phonemes["common_endings"].filter(s => checkboxes.includes(s)),
      "allow_silent_e" : checkboxes.includes("cvce"),
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
    console.log(data)

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
        <div className="checkbox-group">
          <input type="checkbox" id="vc"/>
          <label htmlFor="vc">VC</label>
          <input type="checkbox" id="cvc"/>
          <label htmlFor="cvc">CVC</label>
          <input type="checkbox" id="cvce"/>
          <label htmlFor="cvce">CVCe</label>
          <input type="checkbox" id="cvcvc"/>
          <label htmlFor="cvcvc">CVCVC</label>
        </div>

        <h2>Other Parameters</h2>
        <div>
          <input type="checkbox" id="allow_long_vowels"/>
          <label htmlFor="allow_long_vowels">Allow Long Vowels? (outside of CVCe words)</label>
        </div>
        <div>
          <input type="checkbox" id="allow_soft_consonants"/>
          <label htmlFor="allow_soft_consonants">Allow Soft Consonants? (outside of CVCe words)</label>
        </div>
        <div>
          <input type="checkbox" id="allow_alt_vowels"/>
          <label htmlFor="allow_alt_vowels">Allow Alternative Vowel Pronunciations</label> 
        </div>
        <div>
          <input type="checkbox" id="allow_double_consonants"/>
          <label htmlFor="allow_double_consonants">Allow Double-Consonants (e.g. "mm")</label> 
        </div>

        <h2>Select Letters/Phonemes</h2>
        <CheckboxGroupContainer/>

        <button type="submit">Submit</button>
      </form>

      {response && <div>Response from API: {JSON.stringify(response)}</div>}
    </div>
)
}

export default App;

/*
TODO:
- Separate out CheckboxGroup vs CheckboxGroupWithToggle
- Figure out a better way to separate out hte CheckboxGroupContainer (maybe just a different name)
*/