import React, { useState, ChangeEvent, useContext } from 'react';
import { QuizContext } from '../pages/QuizPage';
import { gradeQuizAnswer } from "../services/QuizService";
import { GradedQuiz, QuizStudentAnswerData } from '../types/Quiz';

const QuizComponent: React.FC = () => {
    // Create a state to handle the answers
    const { activeQuiz } = useContext(QuizContext);
    const [answers, setAnswers] = useState<string[]>(activeQuiz?.questions.map(q => q.answer) || []);
    const [gradedQuiz, setGradedQuiz] = useState<GradedQuiz>();

    // Handle input change
    const handleInputChange = (index: number, event: ChangeEvent<HTMLInputElement>) => {
        const newAnswers = [...answers];
        newAnswers[index] = event.target.value;
        setAnswers(newAnswers);
    };

    const handleSubmit = async () => {
        
        // Create QuizStudentAnswerData object
        const quizStudentAnswerData : QuizStudentAnswerData= {
            questions: activeQuiz?.questions.map(q => q.question) || [],
            correct_answers: activeQuiz?.questions.map(q => q.answer) || [],
            student_answers: answers,
        };
        try {
            const gradedQuiz = await gradeQuizAnswer(quizStudentAnswerData);
            console.log("Graded quiz", gradedQuiz);
            setGradedQuiz(gradedQuiz);
        } catch (error) {
            console.error("Error grading quiz:", (error as Error).message || error);
        }
    }

    return (
        activeQuiz && (
            <div className='flex flex-col h-chatheight overflow-y-scroll'>
                <h1>Quiz on '{activeQuiz?.document}' covering pages {activeQuiz?.start} to {activeQuiz?.end} </h1>
                {activeQuiz?.questions.map((question, index) => (
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

                <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4' onClick={() => handleSubmit()}>
                    Submit
                </button>
            </div>
        ) 
    );
};

export default QuizComponent;