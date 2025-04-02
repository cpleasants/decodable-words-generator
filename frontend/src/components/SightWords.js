import CheckboxGroupWithToggle from './common/CheckboxGroup/CheckboxGroupWithToggle';
import sightWordSets from '../constants/sightWordsSets'

const SightWords = ({nextPage, prevPage, handleUpdate, formData, setFormData}) => {
    return (
        <div>
            <h2>Sight Words</h2>
            {Object.keys(sightWordSets).map(groupName => (
                <div key={groupName}>
                    <CheckboxGroupWithToggle
                        groupName={groupName}
                        itemList={sightWordSets[groupName]}
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

export default SightWords;