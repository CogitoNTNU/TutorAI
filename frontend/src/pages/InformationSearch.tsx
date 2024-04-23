import React, { useEffect, useState } from 'react';
import Header from '../components/Header';
import SearchService from '../services/SearchService';

interface SearchProps {
    ragResponse: string;
    citations: Citation[];
}

interface Citation {
    title: string;
    content: string;
    pageNumber: number;
}

const InformationSearch: React.FC = () => {

    useEffect(() => {
    }, []);
    const [inputValue, setInputValue] = useState('');
    const [outputValue, setOutputValue] = useState<string>();

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setInputValue(event.target.value);
    };

    const handleSearch = async () => {
        if (inputValue) {
            try {
                
                const response = await SearchService(inputValue);
                console.log("Response:", response);
                setOutputValue(response.data.ragResponse);
                setOutputValue("You searched for: " + inputValue)
            } catch (error) {
                console.error('Error uploading file:', error);
            }
        }
    };

    return (
        <div className="bg-blue-100">
            <Header />
            
            <input className="bg-white-100" type="text" placeholder="Search..." value={inputValue} onChange={handleInputChange} />
            <button onClick={handleSearch}>Search</button>
            <div>{outputValue}</div>
        </div>
    );
};

export default InformationSearch;
export type { SearchProps };