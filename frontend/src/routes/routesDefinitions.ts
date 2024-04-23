const baseAPIUrl: string = "http://localhost:8000/api";

const apiRoutes = {
  createFlashcards: `${baseAPIUrl}/create-flashcards/`,
  login: `${baseAPIUrl}/login/`,
  signup: `${baseAPIUrl}/create-user/`,
  search: `${baseAPIUrl}/search/`,
  quiz: `${baseAPIUrl}/quiz/`,
};

export default apiRoutes;
