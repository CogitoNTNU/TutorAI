import React, { useEffect } from 'react';
import Flashcard from '../components/Flashcard';
import UploadPDF from '../components/Upload';
import { FlashcardProps } from '../components/Flashcard';
// import { uploadPDF } from '../utils/api

const PDFtoFlashcard: React.FC = () => {
    const [flashcards, setFlashcards] = React.useState<FlashcardProps[]>([]);

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

            <h1>Lionel Messi Flashcards</h1>
            {flashcards.map((flashcard, index) => {
                return <Flashcard key={index} front={flashcard.front} back={flashcard.back} />;
            })}
        </div>
    );
};

export default PDFtoFlashcard;