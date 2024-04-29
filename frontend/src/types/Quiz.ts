export interface DocumentData {
  document: string;
  start: number;
  end: number;
  learningGoals?: string[];
}

export interface QuizStudentAnswerData {
  questions: string[];
  correct_answers: string[];
  student_answers: string[];
}

export interface GradedQuiz {
  answers_was_correct: boolean[];
  feedback: string[];
}

export interface Quiz {
  document: string;
  start: number;
  end: number;
  questions: Question[];
}

export interface Question {
  question: string;
  answer: string;
}
