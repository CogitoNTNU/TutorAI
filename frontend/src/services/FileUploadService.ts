import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";

const FileUploadService = async (file: File): Promise<Response> => {
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

export default FileUploadService;
