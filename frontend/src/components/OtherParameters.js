import CheckboxGroup from "./common/CheckboxGroup/CheckboxGroup"

const OtherParameters = ({nextPage, prevPage, handleUpdate, formData}) => {
    return (
        <div>
            <h2>Other Parameters</h2>
            <CheckboxGroup 
                itemList={["Long Vowels", "Soft Consonants", "Alternative Vowel Sounds", "Double Consonants", "Silent E"]}
                idList={["allow_long_vowels", "allow_soft_consonants", "allow_alt_vowels", "allow_double_consonants", "allow_silent_e"]}
                handleUpdate={handleUpdate}
                formData={formData}
            />
            <div className='button-footer'>
                <button onClick={prevPage}>Previous</button>
                <button onClick={nextPage}>Next</button>
            </div>
        </div>
    )
}

export default OtherParameters