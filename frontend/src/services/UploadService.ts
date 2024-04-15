import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";
import FlashcardResponse from "../types/FlashcardResponse";

const UploadService = async (file: File): Promise<FlashcardResponse> => {
  let formData = new FormData();
  formData.append("curriculum", file);
  console.log(formData);

  for (let [key, value] of formData.entries()) {
    console.log(key, value);
  }
  console.log(apiRoutes.createFlashcards)
  const response = await axios
    .post(apiRoutes.createFlashcards, formData)
    .then((res) => {
      return res;
    })
    .catch((err) => {
      return err;
    });

  return response;
};

export default UploadService;
