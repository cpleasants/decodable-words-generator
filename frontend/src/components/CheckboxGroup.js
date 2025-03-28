export default function CheckboxGroup({ itemList, idList, selected, setSelected }) {
    // if only an itemList is provided, automatically generate idList
    if (!idList) {
        idList = itemList;
    }

    if (!selected) {
        selected = {};
    }

    if (itemList.length !== idList.length) {
        throw new Error("itemList and idList must be the same length");
    }

    // const [selected, setSelected] = useState({});

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
                <div key={idList[idx]}>
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