import React, { useState } from 'react';

interface FlashcardProps {
    front: string;
    back: string;
}

interface FlashcardsProps {
    name: string;
    flashcards: FlashcardProps[];
}

const Flashcard: React.FC<FlashcardProps> = ({ front, back }) => {
    const [isFrontVisible, setIsFrontVisible] = useState(true);

    const handleClick = () => {
        setIsFrontVisible(!isFrontVisible);
    };

    return (
        <div
            className='text-center'
            style={{
                width: '200px',
                height: '150px',
                border: '1px solid #0000FF', // Blue border
                backgroundColor: '#E0E0FF', // Light blue background
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                cursor: 'pointer',
                color: '#000080', // Navy text color
                margin: '10px',
                borderRadius: '10px',
                userSelect: 'none', // Disable text selection
            }}
            onClick={handleClick}
        >
            {isFrontVisible ? front : back}
        </div>
    );
};

export default Flashcard;
export type { FlashcardProps, FlashcardsProps };
