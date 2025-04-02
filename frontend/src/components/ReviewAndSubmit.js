import phonemes from "../constants/phonemes";
import sightWordSets from "../constants/sightWordsSets";

const ReviewAndSubmit = ({formData, restart, handleApiResponse}) => {

    const checkedBoxes = Object.keys(formData).filter(c => formData[c] === true)
    
    const generateRequest = () => {
        return {
          "hard_consonants" : phonemes["hard_consonants"].filter(s => checkedBoxes.includes(`l_${s}`)),
          "soft_consonants" : checkedBoxes.includes("allow_soft_consonants") || checkedBoxes.includes("cvce") 
            ? phonemes["soft_consonants"].filter(s => checkedBoxes.includes(s)) : [],
          "short_vowels" : phonemes["short_vowels"].filter(s => checkedBoxes.includes(s)),
          "long_vowels" : checkedBoxes.includes("allow_long_vowels") || checkedBoxes.includes("cvce") 
            ? phonemes["long_vowels"].filter(s => checkedBoxes.includes(s)) : [],
          "vowel_teams" : phonemes["vowel_teams"].filter(s => checkedBoxes.includes(s)),
          "digraphs" : phonemes["digraphs"].filter(s => checkedBoxes.includes(s)),
          "double_letters" : checkedBoxes.includes("allow_double_consonants") 
            ? phonemes["double_letters"].filter(s => checkedBoxes.includes(s[0])) : [],
          "prefix_digraphs" : phonemes["prefix_digraphs"].filter(s => checkedBoxes.includes(s)),
          "prefix_blends" : phonemes["prefix_blends"].filter(s => checkedBoxes.includes(s)),
          "suffix_blends" : phonemes["suffix_blends"].filter(s => checkedBoxes.includes(s)),
          "common_endings" : phonemes["common_endings"].filter(s => checkedBoxes.includes(s)),
          "allow_silent_e" : checkedBoxes.includes("allow_silent_e"),
          "allow_vc" : checkedBoxes.includes("vc"),
          "allow_cvc" : checkedBoxes.includes("cvc"),
          "allow_cvce" : checkedBoxes.includes("cvce"),
          "allow_cvcvc" : checkedBoxes.includes("cvcvc"),
          "decodable_only" : true, // TODO: how to include non-decodable words? Should I even?
          "sight_words" : Object.values(sightWordSets).flat().filter(w => checkedBoxes.includes(w))
        }
      }

      const data = generateRequest();    
    
      const handleSubmit = async (event) => {
        event.preventDefault(); // allows me to handle the <form >submission manually instead of going to default (which is redirect to URL)
    
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
          handleApiResponse(result);
          
        } catch (error) {
          console.error('Error submitting data:', error);
        }
      }


    return (
        <form onSubmit={handleSubmit}>
            <h2>Review</h2>
            <p>{JSON.stringify(data)}</p>
            <div className = "button-footer">
                <button onClick={restart}>Edit</button>
                <button type="submit">Submit</button>
            </div>
        </form>
        
      
    )
}

export default ReviewAndSubmit;