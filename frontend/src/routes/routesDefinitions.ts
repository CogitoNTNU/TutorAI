const baseAPIUrl: string = "http://localhost:8000/api";

const apiRoutes = {
  createFlashcards: `${baseAPIUrl}/create-flashcards/`,
  login: `${baseAPIUrl}/login/`,
  signup: `${baseAPIUrl}/create-user/`,
};

export default apiRoutes;
