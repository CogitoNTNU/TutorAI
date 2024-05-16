const baseAPIUrl: string = "http://localhost:8000/api";

const apiRoutes = {
  createFlashcards: `${baseAPIUrl}/flashcards/create/`,
  login: `${baseAPIUrl}/login/`,
  signup: `${baseAPIUrl}/create-user/`,
  search: `${baseAPIUrl}/search/`,
  quiz: `${baseAPIUrl}/quiz/create/`,
  gradeQuizAnswer: `${baseAPIUrl}/quiz/grade/`,
  fileUpload: `${baseAPIUrl}/curriculum/`,
  createCompendium: `${baseAPIUrl}/compendium/`,
};

export default apiRoutes;
