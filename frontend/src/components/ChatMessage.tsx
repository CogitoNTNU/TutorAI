interface ChatMessageData {
    className: string;
    role: string;
    content: string;
}

const ChatMessage: React.FC<ChatMessageData> = ({ className, role, content }) => {
    return (
        <div className={'flex flex-col' + ' ' + className}>
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