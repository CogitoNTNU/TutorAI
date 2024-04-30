import React, { createContext, useState } from 'react';
import Flashcards from '../components/Flashcards';
import { FlashcardsProps } from '../components/Flashcard';
import { pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';
import SideBar from '../components/SideBar';

// Configure PDF.js worker
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

const FlashcardsContext = createContext<{
    activeSets: FlashcardsProps[],
    setActiveSets: (flashcardsProps: FlashcardsProps[]) => void;
}>({
    activeSets: [],
    setActiveSets: () => {}
});

const FlashcardsPage: React.FC = () => {
    const [activeSets, setActiveSets] = useState<FlashcardsProps[]>([]);

    return (
        <div className="bg-blue-100">
            <FlashcardsContext.Provider value={{activeSets, setActiveSets}}>
                <SideBar />

                <Flashcards />
            </FlashcardsContext.Provider>
        </div>
    );
};

export default FlashcardsPage;
export { FlashcardsContext };