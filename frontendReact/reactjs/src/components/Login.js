import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function Login() { //what doctor sees when he enters the web app
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (event) => { //function to check with backend if the login credentials are good
    event.preventDefault();
    const docName = "Vanja";
    try {
      const response = await axios.post('http://your-django-backend-url/api/login/', {
        username,
        password,
      });
      // Handle successful login
      console.log('Login successful:', response.data);
        navigate('/Doctor/', {state: {docName}});
    } catch (error) {
      // Handle login error
      console.error('Login failed:', error.message);
      setError('Invalid username or password');
      navigate('/Doctor/', {state: {docName}});
    }
  };

  return (
    <div>
      <h2>Login</h2>
        <label>
          Username:
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        <br />
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <button type="submit" onClick={handleLogin}>Login</button>
    </div>
  );
}