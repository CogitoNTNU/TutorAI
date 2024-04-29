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
    const { user } = useContext(UserContext);
    const [flashcards, setFlashcards] = React.useState<FlashcardProps[]>([]);

    useEffect(() => {
        if (user.sets.length < 0) {
            console.log('No flashcards to display');
            return;
        }
        
        console.log('User sets:', user.sets);
        // Iterate through each set of flashcards and add them to the flashcards array
        const cards: FlashcardProps[] = [];
        for (const set of user.sets) {
            console.log('Set:', set);
            console.log('Flashcards:', set.flashcards)
            if (Array.isArray(set.flashcards) && set.flashcards.length < 0) {
                console.log('No flashcards in set:', set.name);
                continue;
            }

            for (const card of set.flashcards) {
                console.log('Card:', card);
                cards.push({ front: card.front, back: card.back });
            }
        }
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