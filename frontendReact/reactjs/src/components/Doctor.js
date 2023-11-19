import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { v4 as uuidv4 } from 'uuid';
import '../css/Doctor.css';
import axios from 'axios';

export default function Doctor() {
  const suggestions = ["Andol", "Brufen", "Febricet", "C vitamin", "D vitamin", "I don't know"]
  const [filteredSug, setFilteredSug] = useState([]);
  const location = useLocation();
  const [text, setText] = useState('');
  const [time, setTime] = useState(0);
  const [error, setError] = useState('');
  const [good, setGood] = useState(false);

  const handleInputChange = async (event) => {
    const cur = event.target.value
    setText(cur)
    setGood(false)
    if(cur) {
      const url = 'http://127.0.0.1:8000/api/medicationsuggestion/' + cur
      //console.log(url)
      try {
        const response = await axios.get(url)
        //console.log(response)
        setFilteredSug(response.data)
        //console.log(filteredSug)
      }
      catch(error) {
        console.error("Didn't go!")
        setError("Not good!")
      }
    }
    else {
      setFilteredSug([])
    }
  };

  const handleSuggestionClick = (suggestion) => {
    setText(suggestion);
    setFilteredSug([]);
    setGood(true);
  };

  const handleTimeChange = (event) => {
    setTime(event.target.value);
  };

  const sendReceipt = () => {
    // Implement your logic to send the receipt to Django backend
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const intValue = parseInt(time)
    console.log(intValue);
    console.log(good);
    console.log(text);
    if (isNaN(intValue) || text === '' || intValue <= 0 || !good) setError('Please fill in everything correctly!');
    else {
      const receiptID = uuidv4();
      const doctorID = 1;
      const url = 'http://127.0.0.1:8000/api/receipt/post/';
      const response = await axios.post(url, );
      sendReceipt();
      setError('');
      setText('');
      setTime('');
    }
  };

  const docName = location.state ? location.state.docName : 'Bodes se';

  return (
    <div className="autocomplete">
      <center>
        <h1>Hello, {docName}</h1>
        <br />
        <h2>New receipt:</h2>
        <br />
        Time between consuming in hours: <input type="text" value={time === 0 ? '' : time} onChange={handleTimeChange} />{' '}
        <br />
        <br />
        Medication name: <input type="text" value={text} onChange={handleInputChange} />
        <div className="dropdown-content">
          {filteredSug.map((suggestion, index) => (
            <div key={index} className="autocomplete-item" onClick={() => handleSuggestionClick(suggestion)}>
              {suggestion}
            </div>
          ))}
        </div>
        <br />
        <button onClick={handleSubmit}>Submit</button>
        {error && <p style={{ color: 'red' }}>{error}</p>}
      </center>
    </div>
  );
}