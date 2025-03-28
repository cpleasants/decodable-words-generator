import { useState } from "react";

export default function CheckboxGroup({ itemList, idList }) {
    const [selected, setSelected] = useState({});

    const handleChange = (event) => {
        const { name, checked } = event.target;
        setSelected(prev => ({
            ...prev,
            [name]: checked
        }));
    };

    return (
        <div className="checkbox-group">
            {itemList.map((item, idx) =>  (
                <div>
                    <input
                        type="checkbox"
                        id={idList[idx]}
                        name={idList[idx]}
                        checked={selected[idList[idx]] || false}
                        onChange={handleChange}
                    />
                    <label htmlFor={idList[idx]}>{item}</label>
                </div>
            ))}
        </div>
    )
}