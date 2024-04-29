import { useEffect, useState } from "react";
import QuizService from "../services/QuizService";
import QuizComponent from "../components/QuizComponent";

const QuizPage: React.FC = () => {
    // Get all the quizzes 
    const quizData: Quiz = {
        document: "Sample Document",
        start: 1,
        end: 10,
        questions: [
            { question: "What is React?", answer: "My love" },
            { question: "What is TypeScript?", answer: "" }
        ]
    };

    return <QuizComponent quiz={quizData} />;
};

export default QuizPage;