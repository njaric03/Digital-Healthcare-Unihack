import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { BrowserRouter as Router } from 'react-router-dom';

//default component that is run first
ReactDOM.createRoot(document.getElementById('root')).render(
  <Router>
    <App />
  </Router>
)