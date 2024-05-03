// CitationSidebar.tsx
import React from 'react';
import { Citation } from '../types/SearchResponse';

interface CitationSidebarProps {
  citations: Citation[];
}

const CitationSidebar: React.FC<CitationSidebarProps> = ({ citations }) => {
    return (
        <div className="fixed right-0 w-1/4 h-full bg-gray-100 p-4 overflow-auto">
            <h2 className="font-bold text-lg">Citations</h2>
            {citations.map((citation, index) => (
                <div key={index} className="border-b border-gray-300 py-2">
                    <p className="text-sm text-gray-700">{citation.text}</p>
                    <p className="text-xs text-gray-500">Page {citation.page_num} from {citation.pdf_name}</p>
                </div>
            ))}
        </div>
    );
};

export default CitationSidebar;