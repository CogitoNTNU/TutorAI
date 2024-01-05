// UploadComponent.tsx

import React, { useState } from 'react';
import uploadPDF from '../services/uploadService';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/Page/AnnotationLayer.css';

// Configure PDF.js worker
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;


const UploadComponent: React.FC = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [pdfData, setPdfData] = useState<any>(null);
    const [numPages, setNumPages] = useState<number | null>(null);
    const [pageNumber, setPageNumber] = useState<number>(1);

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
                const response = await uploadPDF(selectedFile);
                console.log(response);
                // Handle the response data
            } catch (error) {
                console.error('Error uploading file:', error);
            }
        }
    };

    return (
        <>
            <form onSubmit={handleSubmit}>
                <input type="file" accept=".pdf" onChange={handleFileChange} />
                <button type="submit">Upload PDF</button>
            </form>

            {pdfData && (
                <Document file={pdfData} onLoadSuccess={onDocumentLoadSuccess}>
                    <Page pageNumber={pageNumber} />
                </Document>
            )}

            {pdfData && numPages && (
                <p>Page {pageNumber} of {numPages}</p>
            )}
        </>
    );
};

export default UploadComponent;
