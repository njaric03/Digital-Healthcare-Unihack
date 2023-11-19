import React, { useState } from 'react';
import axios from 'axios';

export default function Pharmacy() { //what pharmacy sees on the site
    const [cur, setCur]= useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const handleSubmit = async (event) => { //function to find if the receipt exists, check if it used or not, and update it to used
        event.preventDefault();
        console.log(cur)
        const url = 'http://127.0.0.1:8000/api/receipt/' + cur;
        console.log(url)
        try {
          const response = await axios.get(url);
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
      <b><center>Input prescription ID: <input type='text' onChange={(e) => setCur(e.target.value)} /><br/>
      <button onClick={handleSubmit}>Submit</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green'}} >{success}</p>}
      </center></b>
    </div>
  )
}
