import { useState } from "react";

export default function CheckboxGroup({ letterList, groupId }) {
    const [selected, setSelected] = useState({});

    const handleToggleCheckboxGroup = (event) => {
        const { checked } = event.target;
        const newCheckedState = Object.fromEntries(letterList.map(l => [l, checked]));
        setSelected(newCheckedState);
    };

    const handleChange = (event) => {
        const { name, checked } = event.target;
        setSelected(prev => ({
            ...prev,
            [name]: checked
        }));
    };

    return (
        <div>
            {/* Checkbox to toggle all letters in the group */}
            <input
                type="checkbox"
                id={`checkbox-for-${groupId}`}
                onChange={handleToggleCheckboxGroup}
                checked={letterList.every(l => selected[l] === true)}
            />
            <label htmlFor={`checkbox-for-${groupId}`}>{`${groupId}`}</label>

            {/* Create the whole group */}
            <div className="checkbox-group">
                {letterList.map(l =>  (
                    <div key={l}>
                        <input
                            type="checkbox"
                            id={l}
                            name={l}
                            checked={selected[l] || false}
                            onChange={handleChange}
                        />
                        <label htmlFor={l}>{l}</label>
                    </div>
                ))}
            </div>
        </div>
    )
}