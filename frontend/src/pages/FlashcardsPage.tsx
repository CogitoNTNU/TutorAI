import React, { useContext, useEffect } from 'react';
import Flashcards from '../components/Flashcards';
import { FlashcardProps } from '../components/Flashcard';
import { pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import SideBar from '../components/SideBar';
import { UserContext } from '../App';

// Configure PDF.js worker
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

const FlashcardsPage: React.FC = () => {
    const user = useContext(UserContext);
    const [flashcards, setFlashcards] = React.useState<FlashcardProps[]>([]);

    useEffect(() => {
        if (user.sets.length < 0) {
            console.log('No flashcards to display');
            return;
        }
        
        console.log('User sets:', user.sets);
        // Iterate through each set of flashcards and add them to the flashcards array
        const cards: FlashcardProps[] = [];
        user.sets.forEach((set) => {
            set.flashcards.forEach((card) => {
                cards.push(card);
            });
        });
        setFlashcards(cards);
    }, [user.sets]);

    return (
        <div className="bg-blue-100">
            <SideBar />

            <Flashcards flashcards={flashcards} />
        </div>
    );
};

export default FlashcardsPage;