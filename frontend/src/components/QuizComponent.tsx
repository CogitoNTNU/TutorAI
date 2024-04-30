import React, { useState, ChangeEvent } from 'react';
import { Quiz } from '../types/Quiz';

// Define the props type based on the Quiz interface
interface QuizProps {
    quiz: Quiz;
}


const QuizComponent: React.FC<QuizProps> = ({ quiz }) => {
    // Create a state to handle the answers
    const [answers, setAnswers] = useState<string[]>(quiz.questions.map(q => q.answer));

    // Handle input change
    const handleInputChange = (index: number, event: ChangeEvent<HTMLInputElement>) => {
        const newAnswers = [...answers];
        newAnswers[index] = event.target.value;
        setAnswers(newAnswers);
    };

    return (
        <div className='flex flex-col h-chatheight overflow-y-scroll'>
            <h1>Quiz on '{quiz.document}' covering pages {quiz.start} to {quiz.end} </h1>
            {quiz.questions.map((question, index) => (
                <div key={index}>
                    <p>{question.question}</p>
                    <input
                        className=' text-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full'
                        type="text"
                        placeholder={"Your answer: "}
                        onChange={(event) => handleInputChange(index, event)}
                    />
                </div>
            ))}

            <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4'>
                Submit
            </button>
        </div>
    );
};

export default QuizComponent;