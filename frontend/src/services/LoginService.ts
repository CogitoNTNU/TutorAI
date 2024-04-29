import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";
import { LoginAttempt, LoginResponse, User } from "../types/User";

export default async function postLoginAttempt(
  username: string,
  password: string
): Promise<LoginResponse | null> {
  const loginAttempt: LoginAttempt = {
    username: username,
    password: password
  };

  try {
    const res = await axios.post(apiRoutes.login, loginAttempt);
    if (res.status === 200 && res.data) {
      // Assuming res.data.user contains user info and res.data.token contains the authentication token
      const user: User = {
        username: username,
        password: password,
        files: [],
        sets: [],
      };
      const loginResponse: LoginResponse = {
        user: user,
        refreshToken: res.data.refresh,
        accessToken: res.data.access,
      };

      return loginResponse;
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
