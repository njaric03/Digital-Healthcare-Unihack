import React, { useState } from 'react';
import axios from 'axios';

export default function Pharmacy() { //what pharmacy sees on the site
    const [cur, setCur]= useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const [sucFind, setSucFind] = useState('');
    const [receiptData, setReceiptData] = useState('');
    const [medication, setMedication] = useState('')
    const checkReceipt = async() => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/receipt/' + cur)
        console.log(response.data)
        const data = response.data
        setReceiptData(data);
        if(data["USED"] == 'N') {
          setSucFind("Found the receipt");
          setError('')
        }
        else {
          setError("The receipt has already been used");
          setSucFind('');
        }
      }
      catch(error) {
        setError("Didn't find the receipt");
        setSucFind('');
        setReceiptData('');
      }
    }

    const changeReceipt = async () => {
      const url = 'http://127.0.0.1:8000/api/receipt/update_used/' + cur;
      console.log(url);
      setSucFind('');
      setError('');
      setReceiptData('')
      setMedication('')
        try {
          const response = await axios.get(url);
          // Handle successful submit              console.log('Prescription ID successful:', response.data);
            setSuccess('Successfuly found and removed');           
        }catch (error) {
          // Handle prescription error
          console.error('Prescription ID failed:', error.message);
          setError('Invalid prescription ID');
        }
    }

    const findMedication = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/receipt/" + cur + '/medications/');
        const data = response.data;
        let s = ''
        for(let i = 0; i < data.length; i++) {
          const item = data[i];
          s += item["MEDNAME"] + " ";
        }
        setMedication(s);
      }
      catch(error) {
        console.error("Error loading")
      }
    }

    const handleSubmit =  (event) => { //function to find if the receipt exists, check if it used or not, and update it to used
        checkReceipt();
        findMedication();
    };

  return (
    <div>
      <b><center>Input receipt ID: <input type='text' onChange={(e) => setCur(e.target.value)} /><br/>
      {sucFind && <p style={{color:'green'}}>{sucFind}</p>}
      {receiptData && <p>Doctor id:{receiptData["Doctor"]}<br/>Patient id: {receiptData["Patient"]}</p>}
      {medication && <p>{medication}</p>}
      {!sucFind && <button onClick={handleSubmit}>Submit</button>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green'}} >{success}</p>}
      {sucFind && <button onClick={changeReceipt}>Use the receipt</button>}
      </center></b>
    </div>
  )
}
