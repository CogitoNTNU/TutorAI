import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";

const UploadPDF = async (file: File): Promise<Response> => {
  let formData = new FormData();
  formData.append("pdf", file);
  
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

export default UploadPDF;
