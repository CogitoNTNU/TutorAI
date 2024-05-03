import { useContext, useState } from "react";
import { ChatData } from "../types/SearchResponse";
import { ChatContext, CitationContext, FilesContext } from "../pages/ChatPage";
import sendRAGQuery from "../services/SearchService";
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';

const MessageField: React.FC = () => {
    const { chatHistory, setChatHistory } = useContext(ChatContext);
    const { setCitations } = useContext(CitationContext);
    const { activeFiles } = useContext(FilesContext);
    const [message, setMessage] = useState<string>('');

    const sendMessage = async () => {
        setChatHistory([...chatHistory, {role: 'user', content: message}]);
        setMessage('');

        const chatWindow = document.getElementById('chat-window');
        if (chatWindow) {
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }

        // Construct a ChatData object
        const chatData: ChatData = {
            documents: activeFiles,
            user_question: message,
            chat_history: chatHistory
        };

        const response = await sendRAGQuery(chatData);

        // Update the chat history
        setChatHistory([...chatHistory, {role: 'user', content: message}, {role: 'assistant', content: response.data.answer}]);
        setCitations([...response.data.citations]);
        // Scroll to the bottom of the chat window
        if (chatWindow) {
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }
    }

    return (
        <div className='absolute bottom-5 left-1/2 transform -translate-x-1/2 px-3 w-full h-16 flex justify-between items-center bg-blue-100 border-2 border-blue-900 rounded-2xl'>
            <input type='text' className='w-4/5 h-10 m-2 p-2 bg-blue-100 placeholder-gray-900 outline-none' placeholder='Message TutorAI...' value={message} onChange={(e) => setMessage(e.target.value)} />
            <button className='m-2 p-2 w-10 h-10 flex jusitfy-between items-center hover:bg-blue-300 border-blue-900 rounded-xl  outline-none' onClick={() => sendMessage()}>
                <ArrowUpwardIcon />
            </button>
        </div>
    );
};

export default MessageField;