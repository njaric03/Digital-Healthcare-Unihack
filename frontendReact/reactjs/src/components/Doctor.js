import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { v4 as uuidv4 } from 'uuid';
import '../css/Doctor.css';
import axios from 'axios';

export default function Doctor() {
  const [filteredSug, setFilteredSug] = useState([]);
  const [receiptID, setReceiptID] = useState(null);
  const location = useLocation();
  const [text, setText] = useState('');
  const [time, setTime] = useState(0);
  const [error, setError] = useState('');
  const [good, setGood] = useState(false);
  const [submit, setSubmit] = useState(false);
  const [patientID, setPatientID] = useState('');
  const curDate = new Date();

  const handleInputChange = async (event) => {
    const cur = event.target.value;
    setText(cur);
    setGood(false);
    if(cur) {
      const url = 'http://127.0.0.1:8000/api/medicationsuggestion/' + cur;
      //console.log(url)
      try {
        const response = await axios.get(url);
        console.log(response)
        console.log(response.data)
        setFilteredSug(response.data);
      }
      catch(error) {
        console.error("Didn't go!");
        setError("Not good!");
      }
    }
    else {
      setFilteredSug([]);
    }
  };

  const handleSuggestionClick = (suggestion) => {
    setText(suggestion);
    setFilteredSug([]);
    setGood(true);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const intValue = parseInt(time);
    console.log(intValue);
    console.log(good);
    console.log(text);
    if (isNaN(intValue) || text === '' || intValue <= 0 || !good) {
      setError('Please fill in everything correctly!');
    }
    else {
      const receiptID = uuidv4();
      const doctorID = 1;
      const url = 'http://127.0.0.1:8000/api/receiptmedication/post/';
      const sendData = {Receipt:'1',DocMedPermission:'1', PERIOD:intValue};
      try {
        const response = await axios.post(url, sendData);
        setError('');
        setText('');
        setTime('');
      }
      catch (error) {
        console.error("WRONG!");  
      }
    }
    if(!submit) {
      setSubmit(true);
      const url2 = 'http://127.0.0.1:8000/api/receipt/post/';
      const jsonData = {id:receiptID, USED:'N', EXPIRYDATE:"2023-11-29", Doctor:1,Patient:patientID} //expirydate needs change!!!
      try {
        const response = await axios.post(url2, jsonData);
        console.log(response)
      }
      catch(error) {
        console.error("Didn't go through")
      }
    }
  };

  const docName = location.state ? location.state.docName : 'Bodes se';
  return (
    <div className="autocomplete">
      <center>
        <h1>Hello, {docName}</h1>
        <br />
        Patiend ID: <input type='text' onChange= {(e) => setPatientID(e.target.value)}/><br/><br/>
        <button onClick={(e) => setReceiptID(Math.floor(Math.random() * (71) + 30))}><b>New receipt:</b></button>{receiptID && <p style={{color:'black'}}>Current receipt ID: {receiptID}</p>}
        <br />
        Time between consuming in hours: <input type="text" value={time} onChange={(e) => setTime(e.target.value)} />{' '}
        <br />
        <br />
        Medication name: <input type="text" value={text} onChange={handleInputChange} />
        <div className="dropdown-content">
          {filteredSug.map((suggestion, index) => (
            <div key={index} className="autocomplete-item" onClick={() => handleSuggestionClick(suggestion)}>
              {suggestion}
            </div>
          ))}
        </div><br />
        <button onClick={handleSubmit}>Submit</button>
        {error && <p style={{ color: 'red' }}>{error}</p>}
      </center>
    </div>
  );
}