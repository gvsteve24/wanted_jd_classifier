import styled from 'styled-components/macro';
import { login, useAuth, logout, authFetch } from "./auth";
import { Prediction } from './components/Prediction'
import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import "./App.css";

const Container = styled.div `
    width: 100vw;
    height: 100vh;

    div {
        width: 1000px;
        height: 100px;
        margin: 0 auto;
        font-size: 20px;
        font-weight: 600;
        text-align: center;
        line-height: 100px;

        form {
            div {
                display: flex;
                height: 4rem;

                input {
                    font-size: 1.5rem;
                    color: white;
                    background-color: #666;
                    margin: auto;
                    padding: 0 10px;
                    width: 30%;
                    height: 2.5rem;

                    ::placeholder {
                        font-size: 1.5rem;
                        color: white;
                        font-weight: 400;
                    }
                }
            }

            button {
                font-size: 1.2rem;
                width: 10rem;
                height: 2.5rem;
                background-color: #666;
                color: #fff;
            }
        }
    }
`;

const Header = styled.nav `
    display: flex;
    font-size: 20px;
    width: 100%;
    height: 80px;
    background-color: #666;

    ul {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        width: 1000px;
        margin: 0 auto;

        li {
            list-style-type: none;
            width: 18rem;
            text-align: center;

            a {
                font-family: Arial, Helvetica, sans-serif;
                font-weight: 700;
                color: white;
                font-size: 2rem;
                text-decoration: none;
            }
        }

        li.half {
            width: 9rem;
        }
    }
`;

export default function App() {
	return (
		<Router>
			<Container>
				<Header>
					<ul>
						<li>
							<Link to="/">원티드 직군 분류</Link>
						</li>
                        <li className="half">
                            <Link to="/login">Login</Link>
                        </li>
					</ul>
				</Header>
				{/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
				<Switch>
					<Route path="/login">
						<Login />
					</Route>
					<Route path="/">
						<Home />
					</Route>
				</Switch>
			</Container>
		</Router>
	);
}

function Home() {
    const [message, setMessage] = useState("");
    const [logged] = useAuth();

	useEffect(() => {
		authFetch("/api/protected")
			.then((response) => {
				if (response.status === 401) {
					setMessage("Sorry you aren't authorized! Please login to use service.");
					return null;
				}
				return response.json();
			})
			.then((response) => {
				if (response && response.message) {
					setMessage(response.message);
				}
			});
	}, []);


	return (
        <div className="section">
            {!logged ? message :<Prediction/>}
        </div>  
    );
}

function Login() {
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
    const [token, setToken] = useState("")
	const [logged] = useAuth();

	const onSubmitClick = (e) => {
		e.preventDefault();
		let opts = {
			username: username,
			password: password,
		};
		fetch("/api/login", {
			method: "post",
			body: JSON.stringify(opts),
		})
			.then((r) => r.json())
			.then((token) => {
				if (token.access_token) {
					login(token);
                    setToken(token.access_token)
					console.log(token);
				} else {
					console.log("Please type in correct username/password");
				}
			});
	};

	const handleUsernameChange = (e) => {
		setUsername(e.target.value);
	};

	const handlePasswordChange = (e) => {
		setPassword(e.target.value);
	};

	return (
		<div>
			<h2>Login</h2>
			{!logged ? (
				<form action="#">
					<div>
						<input
							type="text"
							placeholder="Username"
							onChange={handleUsernameChange}
							value={username}
						/>
					</div>
					<div>
						<input
							type="password"
							placeholder="Password"
							onChange={handlePasswordChange}
							value={password}
						/>
					</div>
					<button onClick={onSubmitClick} type="submit">
						Login Now
					</button>
				</form>
			) : (
                <form>
                    <p>{`Your token: ${token.slice(0, 10)}...`}</p>
                    <button onClick={() => logout()}>Logout</button>
                </form>
			)}
		</div>
	);
}
