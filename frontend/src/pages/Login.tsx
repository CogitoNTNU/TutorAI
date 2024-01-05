import { useState } from "react";
import postLoginAttempt from "../services/LoginService";
import { useNavigate } from "react-router-dom";

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loginMessage, setLoginMessage] = useState("");

    const handleLogin = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const user = await postLoginAttempt(username, password)
        .then((response) => {
            
            return response;
        }
        ).catch((error) => {
            console.log(error);
            setLoginMessage("An error occurred during login. Please try again later.");
            return error;
        });
        if (!!user) {
            setUsername(user.username);
            setPassword(user.password);
            // TODO - set login credentials in context both accessToken and accessToken
            setLoginMessage("Login successful. Welcome " + username);
        } else {
            setLoginMessage("Incorrect username or password.");
        }
    };

    const navigate = useNavigate();

    const navigateToSignup = () => {
        navigate('/signup');
    };

    return (
        <div>
            <h1>This is the login page</h1>
            <div>
                {/* Login with username and password */}
                <form onSubmit={handleLogin}>
                    <label htmlFor="username">Username</label>
                    <input 
                        type="text" 
                        id="username" 
                        value={username} 
                        onChange={(e) => setUsername(e.target.value)} 
                    />
                    <label htmlFor="password">Password</label>
                    <input 
                        type="password" 
                        id="password" 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)} 
                    />
                    <button type="submit">Login</button>
                </form>
                {loginMessage && <p>{loginMessage}</p>}
            </div>
            <button onClick={navigateToSignup}>Go to Signup</button>
        </div>
    );
};

export default Login;
