import { useState, createContext } from "react";
import QuizComponent from "../components/QuizComponent";
import { Quiz } from "../types/Quiz";
import SideBar from "../components/SideBar";

const QuizContext = createContext<{
    activeQuiz: Quiz | null,
    setActiveQuiz: (quiz: Quiz | null) => void;
}>({
    activeQuiz: null,
    setActiveQuiz: () => {}
});

const QuizPage: React.FC = () => {

    const [activeQuiz, setActiveQuiz] = useState<Quiz | null>(null);

    return (
        <div className="bg-blue-50 relative flex flex-grow w-full flex flex-col ">
            <QuizContext.Provider value={{activeQuiz, setActiveQuiz}}>
                <SideBar />
                <div className="absolute left-1/2 transform -translate-x-1/2 w-2/5 h-full'">
                    <QuizComponent />
                </div>
            </QuizContext.Provider>
      
        </div>
    );
};

export default QuizPage;
export { QuizContext }