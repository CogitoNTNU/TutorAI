import axios from "axios";
import SearchResponse from "../types/SearchResponse";
import apiRoutes from "../routes/routesDefinitions";

const SearchService = async (text: string): Promise<SearchResponse> => {
  // Get documents from the frontend context
  const chatRequest = {
    documents: ["PLACEHOLDER"],
    user_question: text,
  };

  const response = await axios
    .post(apiRoutes.search, chatRequest)
    .then((res) => {
      return res;
    })
    .catch((err) => {
      return err;
    });

  return response;
};

export default SearchService;
