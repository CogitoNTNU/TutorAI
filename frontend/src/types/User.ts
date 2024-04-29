import { FlashcardsProps } from "../components/Flashcard";

type User = {
  username: string;
  password: string;
  files: string[];
  sets: FlashcardsProps[];
};

type LoginAttempt = {
  username: string;
  password: string;
};

type LoginResponse = {
  user: User;
  refreshToken: string;
  accessToken: string;
};

type SignupAttempt = {
  username: string;
  password: string;
  confirmPassword: string;
};

type SignupResponse = {
  user: User;
};
export type {
  User,
  LoginAttempt,
  LoginResponse,
  SignupAttempt,
  SignupResponse,
};
