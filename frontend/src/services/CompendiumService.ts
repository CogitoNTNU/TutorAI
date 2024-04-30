import { DocumentData } from "../types/Quiz";
import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";
import { Compendium } from "../types/Compendium";

/**
 * Service to create a compendiums.
 * @param data - The document data to generate the quiz.
 */
export const createCompendium = async (
  data: DocumentData
): Promise<Compendium> => {
  try {
    const response = await axios.post(apiRoutes.createCompendium, data);
    if (response.status === 200) {
      return response.data;
    } else {
      throw new Error("Failed to create Compendium");
    }
  } catch (error: any) {
    console.error("Error creating Compendium:", error.message || error);
    throw error;
  }
};
