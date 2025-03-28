import { useState } from "react";
import CheckboxGroup from "./CheckboxGroup";

export default function CheckboxGroupWithToggle({ itemList, idList, groupName }) {
    const [selected, setSelected] = useState({});

    const handleToggleCheckboxGroup = (event) => {
        const { checked } = event.target;
        const newCheckedState = Object.fromEntries(itemList.map(l => [l, checked]));
        setSelected(newCheckedState);
    };

    return (
        <div>
            {/* Checkbox to toggle all letters in the group */}
            <input
                type="checkbox"
                id={`checkbox-for-${groupName}`}
                onChange={handleToggleCheckboxGroup}
                checked={itemList.every(l => selected[l] === true)}
            />
            <label htmlFor={`checkbox-for-${groupName}`}>{`${groupName}`}</label>
            <CheckboxGroup itemList={itemList} idList={idList} />
        </div>
    )
}