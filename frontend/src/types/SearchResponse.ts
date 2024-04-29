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

export interface Citation {
  title: string;
  content: string;
  pageNumber: number;
}

export interface SearchProps {
  answer: string;
  citations: Citation[];
}

export type SearchResponse = {
  data: SearchProps;
};
