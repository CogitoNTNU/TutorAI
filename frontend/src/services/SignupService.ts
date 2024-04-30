import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";
import { SignupAttempt, SignupResponse, User } from "../types/User";

export default async function postSignupAttempt(
  username: string,
  password: string,
  confirmPassword: string
): Promise<SignupResponse | null> {
  const SignupAttempt: SignupAttempt = {
    username: username,
    password: password,
    confirmPassword: confirmPassword,
  };

  // Check if passwords match
  if (SignupAttempt.password !== SignupAttempt.confirmPassword) {
    return null;
  }

  try {
    const res = await axios.post(apiRoutes.signup, SignupAttempt);
    if (res.status === 201 && res.data) {
      const user: User = {
        username: username,
        password: password,
        files: [],
        sets: [],
      };
      const signupResponse: SignupResponse = {
        user: user,
      };

      return signupResponse;
    } else {
      // Handle unsuccessful login attempts
      return null;
    }
  } catch (e) {
    console.error(e);
    // You can return a more specific error message or object here
    return null;
  }
}
