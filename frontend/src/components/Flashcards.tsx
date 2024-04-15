import React from "react";
import Flashcard, { FlashcardProps } from "./Flashcard"

const Flashcards: React.FC<{ flashcards: FlashcardProps[] }> = ({ flashcards }) => {
    const [flashcardIndex, setFlashcardIndex] = React.useState<number>(0);

    return (
        <div>
            <h1 className="mt-10 text-4xl">Your Flashcards</h1>
            <div className="flex justify-center mt-5">
                {flashcards.length > 0 && (
                    <Flashcard
                        key={flashcardIndex}
                        front={flashcards[flashcardIndex].front}
                        back={flashcards[flashcardIndex].back}
                    />
                )}
            </div>

            <div className="flex justify-center mt-5">
                <button
                    className="px-4 py-2 mr-2 bg-blue-500 text-white rounded"
                    onClick={() => setFlashcardIndex((prevIndex) => prevIndex > 0 ? prevIndex - 1 : flashcards.length - 1)}
                >
                    Previous
                </button>
                <button
                    className="px-4 py-2 bg-blue-500 text-white rounded"
                    onClick={() => setFlashcardIndex((prevIndex) => (prevIndex + 1) % flashcards.length)}
                >
                    Next
                </button>
            </div>
        </div>
    );
};

export default Flashcards;