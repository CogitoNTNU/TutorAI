import React, { useContext, useEffect } from 'react';
import Flashcard, { FlashcardProps } from './Flashcard'
import { FlashcardsContext } from '../pages/FlashcardsPage';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

const Flashcards: React.FC<{}> = () => {
    const { activeSets } = useContext(FlashcardsContext);
    const [flashcardIndex, setFlashcardIndex] = React.useState<number>(0);

    useEffect(() => {
        if (activeSets.length === 0) {
            setActiveFlashcards([]);
            return;
        }

        // Iterate through each set of flashcards and add them to the flashcards array
        const cards: FlashcardProps[] = [];
        for (const set of activeSets) {
            if (!Array.isArray(set.flashcards) || set.flashcards.length === 0) {
                continue;
            }

            for (const card of set.flashcards) {
                cards.push({ front: card.front, back: card.back });
            }
        }

        // Update the active flashcards state
        setActiveFlashcards(cards);
        setFlashcardIndex(0);
    }, [activeSets]);

    const [activeFlashcards, setActiveFlashcards] = React.useState<FlashcardProps[]>([]);

    return (
        <div className='absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2'>
            <div className='flex flex-col justify-center items-center'>
                {activeFlashcards.length == 0 && (
                <h1 className='text-2xl font-bold'>No flashcards to display</h1>   
                )}
                {activeFlashcards.length > 0 && (
                <>
                    <Flashcard
                        key={flashcardIndex}
                        front={activeFlashcards[flashcardIndex].front}
                        back={activeFlashcards[flashcardIndex].back}
                    />

                    <p>{flashcardIndex+1} / {activeFlashcards.length} </p>
                    <div className='mt-5'>
                        <button
                            className='px-4 py-2 mr-10 w-24 bg-blue-500 text-white rounded select-none'
                            onClick={() => setFlashcardIndex((prevIndex) => prevIndex > 0 ? prevIndex - 1 : activeFlashcards.length - 1)}
                        >
                            <ArrowBackIcon />
                        </button>
                        <button
                            className='px-4 py-2 w-24 bg-blue-500 text-white rounded select-none'
                            onClick={() => setFlashcardIndex((prevIndex) => (prevIndex + 1) % activeFlashcards.length)}
                        >
                            <ArrowForwardIcon />
                        </button>
                    </div>
                </>
                )}
            </div>
        </div>
    );
};

export default Flashcards;