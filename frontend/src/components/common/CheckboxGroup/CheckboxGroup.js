const CheckboxGroup = ({ itemList, idList, handleUpdate, formData }) => {
    // if only an itemList is provided, automatically generate idList
    if (!idList) {
        idList = itemList;
    }

    if (itemList.length !== idList.length) {
        throw new Error("itemList and idList must be the same length");
    }

    return (
        <div className="checkbox-group">
            {idList.map((id, idx) =>  (
                <div key={id}>
                    <input
                        type="checkbox"
                        id={id}
                        name={id}
                        checked={formData[id] || false}
                        onChange={handleUpdate}
                    />
                    <label htmlFor={idList[idx]}>{itemList[idx]}</label>
                </div>
            ))}
        </div>
    )
}

export default CheckboxGroup;