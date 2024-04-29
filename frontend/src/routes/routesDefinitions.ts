const baseAPIUrl: string = "http://localhost:8000/api";

const apiRoutes = {
  createFlashcards: `${baseAPIUrl}/create-flashcards/`,
  login: `${baseAPIUrl}/login/`,
  signup: `${baseAPIUrl}/create-user/`,
  search: `${baseAPIUrl}/search/`,
  fileupload: `${baseAPIUrl}/store-curriculum/`,
  quiz: `${baseAPIUrl}/quiz/`,
  fileUpload: `${baseAPIUrl}/store-curriculum/`,
};

export default apiRoutes;
