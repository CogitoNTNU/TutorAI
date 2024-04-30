import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";
import FlashcardResponse from "../types/FlashcardResponse";

const UploadService = async (file: File): Promise<FlashcardResponse> => {
  let formData = new FormData();
  formData.append("curriculum", file);
  
  const response = await axios
    .post(apiRoutes.fileUpload, formData)
    .then((res) => {
      return res;
    })
    .catch((err) => {
      return err;
    });

  return response;
};

export default UploadService;
