
import React, { useState } from 'react';
import WordPatterns from './WordPatterns'
import Letters from './Letters'
import LetterCombinations from './LetterCombinations'
import OtherParameters from './OtherParameters'
import SightWords from './SightWords'
import ReviewAndSubmit from './ReviewAndSubmit';
import ResponseDisplay from './ResponseDisplay'

const Selection = () => {
    const [page, setPage] = useState(0);
    const [formData, setFormData] = useState({})
    const [apiResponse, setApiResponse] = useState(null);

    const nextPage = () => setPage(page + 1)
    const prevPage = () => setPage(page - 1)
    const restart = () => setPage(0)

    const handleUpdate = (event) => {
        const { name, value, checked, type } = event.target;
        setFormData(prev => ({
            ...prev, [name] : type === 'checkbox' ? checked : value
        }));
    }

    const handleApiResponse = (response) => {
        setPage(page + 1)
        setApiResponse(response)
    }

    switch (page) {
        case 0:
            return <WordPatterns
                nextPage = {nextPage}
                handleUpdate = {handleUpdate}
                formData = {formData}/>
        case 1:
            return <Letters
                nextPage = {nextPage}
                prevPage = {prevPage}
                handleUpdate = {handleUpdate}
                formData = {formData}
                setFormData = {setFormData}/>
        case 2:
            return <LetterCombinations
                nextPage = {nextPage}
                prevPage = {prevPage}
                handleUpdate = {handleUpdate}
                formData = {formData}
                setFormData = {setFormData}/>
        case 3:
            return <OtherParameters
                nextPage = {nextPage}
                prevPage = {prevPage}
                handleUpdate = {handleUpdate}
                formData = {formData}/>
        case 4:
            return <SightWords
                nextPage = {nextPage}
                prevPage = {prevPage}
                handleUpdate = {handleUpdate}
                formData = {formData}
                setFormData = {setFormData}/>
        case 5: 
            return <ReviewAndSubmit
                formData = {formData}
                handleApiResponse = {handleApiResponse}
                restart = {restart}/>
        default:
            return <ResponseDisplay
                apiResponse = {apiResponse}
                restart={restart}/>
    }
}

export default Selection;