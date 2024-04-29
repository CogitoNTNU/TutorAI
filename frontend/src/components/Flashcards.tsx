import React, { useContext, useEffect } from 'react';
import Flashcard, { FlashcardProps } from './Flashcard'
import { FlashcardsContext } from '../pages/FlashcardsPage';

const Flashcards: React.FC<{}> = () => {
    const { activeSets } = useContext(FlashcardsContext);
    const [flashcardIndex, setFlashcardIndex] = React.useState<number>(0);

    useEffect(() => {
        console.log('Active sets:', activeSets);

        if (activeSets.length === 0) {
            console.log('No flashcards to display');
            setActiveFlashcards([]);
            return;
        }

        // Iterate through each set of flashcards and add them to the flashcards array
        const cards: FlashcardProps[] = [];
        for (const set of activeSets) {
            if (!Array.isArray(set.flashcards) || set.flashcards.length === 0) {
                console.log('No flashcards in set:', set.name);
                continue;
            }

            for (const card of set.flashcards) {
                console.log('Card:', card);
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
                    <div className='mt-5'>
                        <button
                            className='px-4 py-2 mr-10 w-24 bg-blue-500 text-white rounded'
                            onClick={() => setFlashcardIndex((prevIndex) => prevIndex > 0 ? prevIndex - 1 : activeFlashcards.length - 1)}
                        >
                            Previous
                        </button>
                        <button
                            className='px-4 py-2 w-24 bg-blue-500 text-white rounded'
                            onClick={() => setFlashcardIndex((prevIndex) => (prevIndex + 1) % activeFlashcards.length)}
                        >
                            Next
                        </button>
                    </div>
                </>
                )}
            </div>
        </div>
    );
};

export default Flashcards;