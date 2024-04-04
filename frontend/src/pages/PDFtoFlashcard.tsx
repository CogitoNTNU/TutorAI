import React, { useEffect } from 'react';
import Flashcard from '../components/Flashcard';
import UploadPDF from '../components/Upload';
import { FlashcardProps } from '../components/Flashcard';
// import { uploadPDF } from '../utils/api

const PDFtoFlashcard: React.FC = () => {
    const [flashcards, setFlashcards] = React.useState<FlashcardProps[]>([]);
    const [flashcardIndex, setFlashcardIndex] = React.useState<number>(0);

    useEffect(() => {
        // Test flashcards by hardcoding them
        setFlashcards([
            { front: "What is Lionel Messi's nationality?", back: "Argentinian" },
            { front: "How many Ballon d'Or awards has Messi won?", back: "7" },
            { front: "Which club did Messi play for most of his career?", back: "FC Barcelona" }
        ]);
    }, []);

    return (
        <div>
            <UploadPDF />

            {/* When the user uploads a PDF, the backend will convert the PDF to a list of flashcards
            The backend will then send the list of flashcards to the frontend
            The frontend will then display the flashcards */}

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

export default PDFtoFlashcard;