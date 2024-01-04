import axios from "axios";
import apiRoutes from "../routes/routesDefinitions";
import { LoginAttempt, User } from "../types/User";

export default async function postLoginAttempt(
  username: string,
  password: string
): Promise<User | null> {
  // Create login attempt
  const loginAttempt: LoginAttempt = {
    username: username,
    password: password,
  };

  return await axios
    .post(apiRoutes.login, loginAttempt)
    .then((res) => {
      if (res.status === 200 && res.data.username && res.data.password) {
        const user: User = {
          username: res.data.username,
          password: res.data.password,
        };
        return user;
      }
    })
    .catch((e) => {
      console.log(e);
      return e.response;
    });
}
