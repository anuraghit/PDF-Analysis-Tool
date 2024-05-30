// src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [pdf, setPdf] = useState(null);
  const [query, setQuery] = useState('');
  const [result, setResult] = useState('');

  const handlePdfChange = (e) => {
    setPdf(e.target.files[0]);
  };

  const handleQueryChange = (e) => {
    setQuery(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('pdf', pdf);
    formData.append('query', query);

    try {
      const response = await axios.post('http://127.0.0.1:8000/submit', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResult(response.data.result);
    } catch (error) {
      console.error('There was an error!', error);
    }
  };

  const handleReset = () => {
    setPdf(null);
    setQuery('');
    setResult('');
  };

  return (
    <div className="container">
      <h2 className="title">PDF Query Form</h2>
      <form onSubmit={handleSubmit}>
        <div className="field">
          <label className="label">Upload PDF</label>
          <div className="control">
            <input className="input" type="file" accept="application/pdf" onChange={handlePdfChange} required />
          </div>
        </div>
        <div className="field">
          <label className="label">Query</label>
          <div className="control">
            <input className="input" type="text" value={query} onChange={handleQueryChange} required />
          </div>
        </div>
        <div className="field is-grouped">
          <div className="control">
            <button className="button is-link" type="submit">Submit</button>
          </div>
          <div className="control">
            <button className="button is-light" type="button" onClick={handleReset}>Reset</button>
          </div>
        </div>
      </form>
      {result && (
        <div className="result">
          <div className="box">
            <h3 className="title is-4">Result</h3>
            <p>{result}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
