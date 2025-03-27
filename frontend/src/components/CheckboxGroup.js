import { useState } from "react";

export default function CheckboxGroup({ letterList, groupId }) {
    const [selected, setSelected] = useState({});

    const handleToggleCheckboxGroup = (event) => {
        handleChange(event);
        const { checked } = event.target
        const newCheckedState = Object.fromEntries(letterList.map(l => [l, checked]))
        setSelected(newCheckedState)
    }

    const handleChange = (event) => {
        const { name, checked } = event.target;
        setSelected(prev => ({
            ...prev,
            [name]: checked
        }))
    }

    return (
        <div>
            {/* Checkbox to toggle all letters in the group */}
            <input
                type="checkbox"
                id={`checkbox-for-${groupId}`}
                onChange={handleToggleCheckboxGroup}
            />
            <label htmlFor={`checkbox-for-${groupId}`}>{`${groupId}`}</label>

            {/* Create the whole group */}
            <div className="checkbox-group">
                {letterList.map(l =>  (
                    <div key={`${l}`}>
                        <input
                            type="checkbox"
                            id={`${groupId}-${l}`}
                            name={`${groupId}-${l}`}
                            checked={selected[l] || false}
                            onChange={handleChange}
                        />
                        <label htmlFor={`${groupId}-${l}`}>{l}</label>
                    </div>
                ))}
            </div>
        </div>
    )
}