import CheckboxGroupWithToggle from './common/CheckboxGroup/CheckboxGroupWithToggle';
import letterSets from '../constants/letterSets';

const Letters = ({nextPage, prevPage, handleUpdate, formData, setFormData}) => {
    return (
        <div>
            <h2>Letter Sets</h2>
            {Object.keys(letterSets).map(groupName => (
                <div key={groupName}>
                    <CheckboxGroupWithToggle
                        groupName={groupName}
                        itemList={letterSets[groupName]}
                        idList={letterSets[groupName].map(l => `l_${l}`)}
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

export default Letters;