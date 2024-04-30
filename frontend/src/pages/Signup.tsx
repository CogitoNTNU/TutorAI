import { useEffect, useState } from "react";
import postSignupAttempt from "../services/SignupService";
import { useNavigate } from "react-router-dom";
import postLoginAttempt from "../services/LoginService";
import { LoginResponse } from "../types/User";
import Header from "../components/Header";

const Signup = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [signupMessage, setSignupMessage] = useState("");
    const [loginCredentials, setLoginCredentials] = useState({} as LoginResponse);

    useEffect(() => {
        if (loginCredentials.accessToken) {
            // TODO - set login credentials in context both accessToken and accessToken
        }
    }, [loginCredentials]);
    
    const handleSignup = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        if (password !== confirmPassword) {
            setSignupMessage("Passwords do not match.");
            return;
        }

        await postSignupAttempt(username, password, confirmPassword)
        .then((response) => {
            if (response) {
                // Valid signup 
                postLoginAttempt(username, password)
                .then((response) => {
                    if (response) {
                        setLoginCredentials(response);
                    }
                }).catch((error) => {
                    console.log(error);
                    setSignupMessage("An error occurred during signup. Please try again later.");
                });

                setSignupMessage("Signup successful. Welcome, " + response.user.username);
            } else {
                setSignupMessage("Signup failed. Please try again.");
            }
        }).catch((error) => {
            console.log(error);
            setSignupMessage("An error occurred during signup. Please try again later.");
        });
    };

    const navigate = useNavigate();

    const navigateToLogin = () => {
        navigate('/login');
    };

    return (
        <div>
            <Header />
            
            <h1>This is the signup page</h1>
            <div>
                {/* Signup with username, password, and confirm password */}
                <form onSubmit={handleSignup}>
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
                    <label htmlFor="confirmPassword">Confirm Password</label>
                    <input 
                        type="password" 
                        id="confirmPassword" 
                        value={confirmPassword} 
                        onChange={(e) => setConfirmPassword(e.target.value)} 
                    />
                    <button type="submit">Signup</button>
                </form>
                {signupMessage && <p>{signupMessage}</p>}
            </div>
            <button onClick={navigateToLogin}>Go to Login</button>
        </div>
    );
};

export default Signup;
