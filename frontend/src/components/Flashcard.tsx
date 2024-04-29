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
            className='flex justify-center items-center p-3 select-none text-center w-64 h-64 bg-blue-200 border-4 border-blue-500 rounded-3xl cursor-pointer m-5'
            onClick={handleClick}
        >
            {isFrontVisible ? front : back}
        </div>
    );
};

export default Flashcard;
export type { FlashcardProps, FlashcardsProps };
