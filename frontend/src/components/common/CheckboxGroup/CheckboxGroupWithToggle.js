import CheckboxGroup from "./CheckboxGroup";

const CheckboxGroupWithToggle = ({ itemList, idList, groupName, handleUpdate, formData, setFormData }) => {
    if (!idList) {
        idList = itemList;
    }

    if (itemList.length !== idList.length) {
        throw new Error("itemList and idList must be the same length");
    }
    
    const handleToggleCheckboxGroup = (event) => {
        const { checked } = event.target;
        setFormData(prev => ({
            ...prev, 
            ...Object.fromEntries(idList.map(l => [l, checked]))
        }))
    };
    

    return (
        <div>
            {/* Checkbox to toggle all letters in the group */}
            <input
                type="checkbox"
                id={`checkbox-for-${groupName}`}
                onChange={handleToggleCheckboxGroup}
                checked={idList.every(l => formData[l] === true)}
            />
            <label htmlFor={`checkbox-for-${groupName}`}>{`${groupName}`}</label>
            <CheckboxGroup 
                itemList={itemList} 
                idList={idList} 
                handleUpdate={handleUpdate}
                formData={formData}
            />
        </div>
    )
}

export default CheckboxGroupWithToggle