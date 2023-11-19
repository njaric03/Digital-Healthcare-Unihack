// App.js
import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Doctor from './components/Doctor';
import Login from './components/Login';
import Pharmacy from './components/Pharmacy';
import "./css/App.css";
// component to call everything
const App = () => {
  return (
      <Routes>
        <Route path="/Doctor/" element={<Doctor />} />
        <Route path="/Pharmacy/" element={<Pharmacy />} />
        <Route path="/Login" element={<Login />} />          
        <Route path="/" element={<Navigate to="/Login" />} />
      </Routes>
  );
};

export default App;
