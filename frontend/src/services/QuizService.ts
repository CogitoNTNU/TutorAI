import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";
import {
  DocumentData,
  GradedQuiz,
  Quiz,
  QuizStudentAnswerData,
} from "../types/Quiz";

/**
 * Service to create a quiz.
 * @param data - The document data to generate the quiz.
 */
export const createQuiz = async (data: DocumentData): Promise<Quiz> => {
  try {
    const response = await axios.post(apiRoutes.quiz, data);
    if (response.status === 200) {
      return response.data;
    } else {
      throw new Error("Failed to create quiz");
    }
  } catch (error: any) {
    console.error("Error creating quiz:", error.message || error);
    throw error;
  }
};

/**
 * Service to grade a quiz.
 * @param data - The answers data to grade the quiz.
 */
export const gradeQuizAnswer = async (
  data: QuizStudentAnswerData
): Promise<GradedQuiz> => {
  try {
    const response = await axios.post(apiRoutes.gradeQuizAnswer, data);
    if (response.status === 200) {
      console.log("Quiz graded successfully", response.data);
      return response.data;
    } else {
      throw new Error("Failed to grade quiz");
    }
  } catch (error: any) {
    console.error("Error grading quiz:", error.message || error);
    throw error;
  }
};
