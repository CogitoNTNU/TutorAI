import React, { useEffect, useState } from 'react';
import Flashcards from '../components/Flashcards';
import { FlashcardProps } from '../components/Flashcard';
import UploadService from '../services/stoopiderror';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';

// Configure PDF.js worker
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

const PDFtoFlashcard: React.FC = () => {
    const [flashcards, setFlashcards] = React.useState<FlashcardProps[]>([]);
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [pdfData, setPdfData] = useState<any>(null);
    const [numPages, setNumPages] = useState<number | null>(null);
    const [pageNumber, setPageNumber] = useState<number>(1);
    const [showDocument, setShowDocument] = useState<boolean>(false);
    const [successfulUpload, setSuccessfulUpload] = useState<boolean>(false);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files[0]) {
            const file = event.target.files[0];
            setSelectedFile(file);
            setPdfData(file);
            setPageNumber(1);

            // Convert file to a data URL for react-pdf
            const reader = new FileReader();
            reader.onload = (e) => setPdfData(e.target?.result);
            reader.readAsDataURL(file);
        }
    };

    const onDocumentLoadSuccess = ({ numPages }: { numPages: number }) => {
        setNumPages(numPages);
    };

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        if (selectedFile) {
            try {
                const response = await UploadService(selectedFile);
                console.log("Response:", response);
                setSuccessfulUpload(true);
                // Set flashcards from response
                const flashcards = response.data; // This is NOT an actual error
                setFlashcards(flashcards)
            } catch (error) {
                console.error('Error uploading file:', error);
            }
        }
    };

    const handleToggleDocument = () => {
        setShowDocument(!showDocument);
    };

    useEffect(() => {
        // Test flashcards by hardcoding them
        setFlashcards([
            { front: "What is Lionel Messi's nationality?", back: "Argentinian" },
            { front: "How many Ballon d'Or awards has Messi won?", back: "7" },
            { front: "Which club did Messi play for most of his career?", back: "FC Barcelona" }
        ]);
    }, []);

    return (
        <div className="bg-blue-100">

            <h1 className="my-5 text-4xl">Upload PDF</h1>

            <form className="mt-5 bg-blue-200" onSubmit={handleSubmit}>
                <input className="bg-white text-black py-2 px-4 rounded-md" type="file" accept=".pdf" onChange={handleFileChange} />
                <button className="bg-blue-700 text-white py-2 px-4 rounded-md" type="submit">Upload PDF</button>
            </form>

            {successfulUpload && <p className="m-2 text-green-700">File uploaded successfully!</p>}

            {pdfData && (
            <button className="bg-blue-700 text-white py-2 px-4 rounded-md" onClick={handleToggleDocument}>
                {showDocument ? 'Hide Document' : 'Show Document'}
            </button>
            )}

            {showDocument && pdfData && (
                <div className="flex justify-center">
                    <Document file={pdfData} onLoadSuccess={onDocumentLoadSuccess}>
                        <Page pageNumber={pageNumber} />
                    </Document>
                </div>
            )}

            {showDocument && pdfData && numPages && (
                <p>Page {pageNumber} of {numPages}</p>
            )}

            <Flashcards flashcards={flashcards} />
        </div>
    );
};

export default PDFtoFlashcard;