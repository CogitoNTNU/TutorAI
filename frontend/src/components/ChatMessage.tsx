import { ChatMessageData } from "../types/SearchResponse";

const ChatMessage: React.FC<ChatMessageData> = ({ role, content }) => {
    return (
        <div className='flex flex-col'>
            <div className='p-2'>
                <p className='font-bold'>{role}</p>
            </div>
            <div className='mb-5 p-2'>
                <p className=''>{content}</p>
            </div>
        </div>
    );
};

export default ChatMessage;