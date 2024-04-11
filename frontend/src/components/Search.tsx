import React, { useState } from 'react';

const Search: React.FC = () => {
    const [inputValue, setInputValue] = useState('');
    const [outputValue, setOutputValue] = useState('');

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setInputValue(event.target.value);
    };

    const handleSearch = () => {
        // Perform search logic here
        // You can update the outputValue state with the search result
        setOutputValue(`You searched for: ${inputValue}`);
    };

    return (
        <div>
            <input type="text" value={inputValue} onChange={handleInputChange} />
            <button onClick={handleSearch}>Search</button>
            <div>{outputValue}</div>
        </div>
    );
};

export default Search;