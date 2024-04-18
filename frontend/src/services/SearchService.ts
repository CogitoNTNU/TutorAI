import axios from 'axios';
import SearchResponse from '../types/SearchResponse';

const SearchService = async(text: string): Promise<SearchResponse> => {
    const response = await axios
        .post('TODO: REPLACE_WITH_SEARCH_URL (e.g., apiRoutes.createFlashcards) (see UploadService.ts for correct implementation)', { text })
        .then((res) => {
            return res;
        })
        .catch((err) => {
            return err;
        });
    
    return response;
};

export default SearchService;