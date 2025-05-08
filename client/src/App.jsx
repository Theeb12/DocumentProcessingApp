import './App.css';
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [matches, setMatches] = useState([]);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:5000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      // Directly set the response data as an array of item names
      const resultList = response.data; // Assuming the response is just an array of item names
      setMatches(resultList);
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };

  return (
    <div>
      <h1>Document Processing</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      <h2>Matches</h2>
      {matches.length > 0 ? (
        matches.map((item, index) => (
          <div key={index} style={{ margin: '10px 0' }}>
            <p>{item}</p>
          </div>
        ))
      ) : (
        <p>No matches to display.</p>
      )}
    </div>
  );
}

export default App;
