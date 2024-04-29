import { SearchProps } from "../pages/InformationSearch";

export interface ChatMessageData {
  role: string;
  content: string;
}

export interface ChatData {
  documents: string[]; // The names of the documents
  user_question: string; // The user question
  chat_history?: ChatMessageData[]; // The chat history, optional
}

export type SearchResponse = {
  data: SearchProps;
};
