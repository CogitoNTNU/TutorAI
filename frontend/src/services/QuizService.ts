import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";

interface Quiz {
  document: string;
  start: number;
  end: number;
  content: QuestionAnswers[];
}

interface QuestionAnswers {
  question: string;
  answer: string;
}

const QuizService = async (
  document_name: string,
  start_index: number,
  end_index: number
): Promise<Quiz> => {
  const quizRequest = {
    document: document_name,
    start: start_index,
    end: end_index,
  };

  const response = await axios
    .post(apiRoutes.quiz, quizRequest)
    .then((res) => {
      return res;
    })
    .catch((err) => {
      return err;
    });

  return response;
};

export default QuizService;
