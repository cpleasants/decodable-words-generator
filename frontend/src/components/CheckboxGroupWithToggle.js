import { useState } from "react";
import CheckboxGroup from "./CheckboxGroup";

export default function CheckboxGroupWithToggle({ itemList, idList, groupName }) {
    if (!idList) {
        idList = itemList;
    }

    if (itemList.length !== idList.length) {
        throw new Error("itemList and idList must be the same length");
    }
    
    const [selected, setSelected] = useState({});

    const handleToggleCheckboxGroup = (event) => {
        const { checked } = event.target;
        const newCheckedState = Object.fromEntries(idList.map(l => [l, checked]));
        setSelected(newCheckedState);
    };
    

    return (
        <div>
            {/* Checkbox to toggle all letters in the group */}
            <input
                type="checkbox"
                id={`checkbox-for-${groupName}`}
                onChange={handleToggleCheckboxGroup}
                checked={idList.every(l => selected[l] === true)}
            />
            <label htmlFor={`checkbox-for-${groupName}`}>{`${groupName}`}</label>
            <CheckboxGroup 
                itemList={itemList} 
                idList={idList} 
                selected = {selected} 
                setSelected = {setSelected}
            />
        </div>
    )
}