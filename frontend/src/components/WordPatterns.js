import CheckboxGroup from "./common/CheckboxGroup/CheckboxGroup";

const WordPatterns = ({nextPage, handleUpdate, formData}) => {
    
    // const handleNext = (e) => {
    //     e.preventDefault();
    //     nextPage();
    // }

    return (
        <div>
            <CheckboxGroup 
            itemList={["VC", "CVC", "CVCe", "CVCVC"]}
            idList={["vc", "cvc", "cvce", "cvcvc"]}
            handleUpdate={handleUpdate}
            formData={formData}
            />
            <div className='button-footer'>
                <button onClick={nextPage}>Next</button>
            </div>
        </div>
    )
}

export default WordPatterns;