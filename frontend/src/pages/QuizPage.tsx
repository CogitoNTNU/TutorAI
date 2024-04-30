import { useEffect, useState } from "react";
import QuizService from "../services/QuizService";
import QuizComponent from "../components/QuizComponent";
import { Quiz } from "../types/Quiz";
import SideBar from "../components/SideBar";

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

    return (
        <div className="bg-blue-100 relative flex flex-grow w-full flex flex-col ">

            <SideBar />
            <div className="absolute left-1/2 transform -translate-x-1/2 w-2/5 h-full'">
                <QuizComponent quiz={quizData} />
            </div>
      
        </div>
    );
};

export default QuizPage;