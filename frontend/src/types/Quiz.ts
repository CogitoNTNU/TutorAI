interface QuestionAnswer {
  question: string;
  answer: string;
}

interface Quiz {
  document: string;
  start: number;
  end: number;
  questions: QuestionAnswer[];
}
