import React from 'react';
import { useNavigate } from 'react-router-dom';

const Header: React.FC = () => {
    const [currentPage, setCurrentPage] = React.useState('flashcards' as string)
    
    const navigate = useNavigate();

    return (
        <header>
            <nav className="bg-blue-500 px-40 flex justify-between">                
                <button className={`flex-1 py-4 text-white text-xl font-semibold ${currentPage === 'flashcards' ? 'active-page-button' : ''}`} onClick={() => {navigate('/flashcards'); setCurrentPage('flashcards');}}>Flashcards</button>
                <button className={`flex-1 py-4 text-white text-xl font-semibold ${currentPage === 'chat' ? 'active-page-button' : ''}`} onClick={() => {navigate('/chat'); setCurrentPage('chat');}}>Chat</button>
                <button className={`flex-1 py-4 text-white text-xl font-semibold ${currentPage === 'compendium' ? 'active-page-button' : ''}`} onClick={() => {navigate('/compendium'); setCurrentPage('compendium');}}>Compendium</button>
                <button className={`flex-1 py-4 text-white text-xl font-semibold ${currentPage === 'test' ? 'active-page-button' : ''}`} onClick={() => {navigate('/test'); setCurrentPage('test');}}>Test</button>
            </nav>
        </header>
    );
};

export default Header;