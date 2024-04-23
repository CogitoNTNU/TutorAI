import React from 'react';
import { useNavigate } from 'react-router-dom';

const Header: React.FC = () => {
    const navigate = useNavigate();

    return (
        <header>
            <nav className="bg-blue-500 p-4 flex justify-between">
                <button className="flex-1" onClick={() => navigate('/signup')}>Signup</button>
                <button className="flex-1" onClick={() => navigate('/login')}>Login</button>
                <button className="flex-1" onClick={() => navigate('/file-upload')}>File Upload</button>
                <button className="flex-1" onClick={() => navigate('/pdf-to-flashcards')}>PDF to Flashcards</button>
                <button className="flex-1" onClick={() => navigate('/information-search')}>Information Search</button>
            </nav>
        </header>
    );
};

export default Header;