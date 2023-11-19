import React, { useState } from 'react';
import axios from 'axios';

export default function Pharmacy() {
    const [cur, setCur]= useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const handleSubmit = async (event) => {
        event.preventDefault();
        const url = 'http://127.0.0.1:8000/api/receipt/' + cur;
        try {
          const response = await axios.get(url, { withCredentials: true });
          // Handle successful submit
            console.log('Prescription ID successful:', response.data);
            setSuccess('Successfully found and removed');
            
        } catch (error) {
          // Handle prescription error
          console.error('Prescription ID failed:', error.message);
          setError('Invalid prescription ID');
        }
    };
  return (
    <div>
      <b><center>Input prescription ID: <input type='text' onChange={(e) => setCur(e)} /><br/>
      <button onClick={handleSubmit}>Submit</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green'}} >{success}</p>}
      </center></b>
    </div>
  )
}
