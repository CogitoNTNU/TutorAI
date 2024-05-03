import React, { useState, ChangeEvent, useContext } from 'react';
import { QuizContext } from '../pages/QuizPage';
import { gradeQuizAnswer } from "../services/QuizService";
import { GradedQuiz, QuizStudentAnswerData } from '../types/Quiz';

const QuizComponent: React.FC = () => {
    // Create a state to handle the answers
    const { activeQuiz } = useContext(QuizContext);
    const [answers, setAnswers] = useState<string[]>(activeQuiz?.questions.map(() => '') || []);
    const [gradedQuiz, setGradedQuiz] = useState<GradedQuiz>();

    // Handle input change
    const handleInputChange = (index: number, event: ChangeEvent<HTMLInputElement>) => {
        const newAnswers = [...answers];
        newAnswers[index] = event.target.value;
        setAnswers(newAnswers);
    };

    const handleSubmit = async () => {
        // Create QuizStudentAnswerData object
        const quizStudentAnswerData: QuizStudentAnswerData = {
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
        <>
            {!activeQuiz && (
            <h1 className='text-m font-bold'>Select or create a test...</h1>
            )}
        
            {activeQuiz && (
            <div className='flex flex-col h-chatheight overflow-y-scroll'>
                <h1>Quiz on '{activeQuiz?.document}' covering pages {activeQuiz?.start} to {activeQuiz?.end}</h1>
                {activeQuiz.questions.map((question, index) => (
                    <div key={index} className="mb-4">
                        <p>{question.question}</p>
                        <input
                            className={`p-2 rounded focus:outline-none focus:ring-2 w-full ${
                                gradedQuiz ? (gradedQuiz.answers_was_correct[index] ? 'focus:ring-green-500 bg-green-100' : 'focus:ring-red-500 bg-red-100') : 'focus:ring-blue-500 bg-white'
                            }`}
                            type="text"
                            value={answers[index]}
                            onChange={(event) => handleInputChange(index, event)}
                            placeholder="Your answer: "
                        />
                        {gradedQuiz && (
                            <p className="text-sm mt-1">
                                {gradedQuiz.feedback[index]}
                            </p>
                        )}
                    </div>
                ))}
                <button
                    className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4'
                    onClick={handleSubmit}
                >
                    Grade
                </button>
            </div>
            )}
        </>
    );
};

export default QuizComponent;
