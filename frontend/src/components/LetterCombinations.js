import CheckboxGroupWithToggle from './common/CheckboxGroup/CheckboxGroupWithToggle';
import letterCombinationSets from '../constants/letterCombinationSets';

const LetterCombinations = ({nextPage, prevPage, handleUpdate, formData, setFormData}) => {
    return (
        <div>
            <h2>Letter Combinations</h2>
            {Object.keys(letterCombinationSets).map(groupName => (
                <div key={groupName}>
                    <CheckboxGroupWithToggle
                        groupName={groupName}
                        itemList={letterCombinationSets[groupName]}
                        handleUpdate={handleUpdate}
                        formData={formData}
                        setFormData={setFormData}
                    />
                </div>
            ))}
            <div className='button-footer'>
                <button onClick={prevPage}>Previous</button>
                <button onClick={nextPage}>Next</button>
            </div>
        </div>
    )
}

export default LetterCombinations;