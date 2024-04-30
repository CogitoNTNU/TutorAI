import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";
import FlashcardResponse from "../types/FlashcardResponse";

const CreateFlashcards = async (file: string, start: number, end: number): Promise<FlashcardResponse> => {
    let formData = new FormData();
    formData.append("document", file);
    formData.append("start", start.toString());
    formData.append("end", end.toString());

    const response = await axios
        .post(apiRoutes.createFlashcards, formData)
        .then((res) => {
            return res.data;
        })
        .catch((err) => {
            return err;
        });

    return response;
};

export default CreateFlashcards;
