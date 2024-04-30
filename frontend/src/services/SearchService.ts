import axios from "axios";
import { SearchResponse, ChatData } from "../types/SearchResponse";
import apiRoutes from "../routes/routesDefinitions";

const SearchService = async (chat: ChatData): Promise<SearchResponse> => {
  const response = await axios
    .post(apiRoutes.search, chat)
    .then((res) => {
      return res;
    })
    .catch((err) => {
      return err;
    });

  return response;
};

export default SearchService;
