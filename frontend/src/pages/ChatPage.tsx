import React, { createContext, useState } from "react";
import ChatMessage from "../components/ChatMessage";
import { ChatMessageData, Citation } from "../types/SearchResponse";
import MessageField from "../components/MessageField";
import SideBar from "../components/SideBar";
import CitationSidebar from "../components/CitationsSideBar";

const ChatContext = createContext<{
    chatHistory: ChatMessageData[],
    setChatHistory: (chatHistory: ChatMessageData[]) => void;
}>({} as {
    chatHistory: ChatMessageData[],
    setChatHistory: (chatHistory: ChatMessageData[]) => void;
});

const FilesContext = createContext<{
    activeFiles: string[],
    setActiveFiles: (files: string[]) => void;
}>({} as {
    activeFiles: string[],
    setActiveFiles: (files: string[]) => void;
});

const CitationContext = createContext<{
    citations: Citation[],
    setCitations: (citations: Citation[]) => void;
}>({} as {
    citations: Citation[],
    setCitations: (citations: Citation[]) => void;
});

const ChatPage: React.FC = () => {
    const [chatHistory, setChatHistory] = useState<ChatMessageData[]>([]);
    const [activeFiles, setActiveFiles] = useState<string[]>([]);
    const [citations, setCitations] = useState<Citation[]>([]);
    
    return (
        <div className='relative flex flex-grow w-full flex flex-col'>
            <FilesContext.Provider value={{activeFiles, setActiveFiles}}>
                <SideBar />
                <CitationContext.Provider value={{citations, setCitations}}>
                    <ChatContext.Provider value={{chatHistory, setChatHistory}}>
                            <div className='absolute left-1/2 transform -translate-x-1/2 w-2/5 h-full'>
                                <div className='flex flex-col h-chatheight overflow-y-scroll' id='chat-window'>
                                    <ChatMessage className='pt-5' role="TutorAI" content="Hello! How can I help you today?" />
                                    {chatHistory.map((chat, index) => (
                                        <ChatMessage className='' key={index} role={chat.role === "assistant" ? "TutorAI" : "You"} content={chat.content} />
                                    ))}
                                </div>
                                <MessageField />
                            </div>
                    </ChatContext.Provider>
                    <CitationSidebar citations={citations}/>
                </CitationContext.Provider>
            </FilesContext.Provider>
        </div>
    );
};

export default ChatPage;
export { ChatContext, FilesContext, CitationContext };