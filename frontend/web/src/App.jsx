import React, { useState } from "react";
import Upload from "./components/Upload";
import "./App.css";

export default function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="app-container">
      <h2 className="title">Deteksi Katarak Retina</h2>

      <div className="upload-container">
        <Upload setResult={setResult} />
      </div>

      {result && (
        <div className="result-container">
          <h3>Hasil Prediksi:</h3>
          <p>Label: {result.label}</p>
          <p>Confidence: {(result.confidence * 100).toFixed(1)}%</p>
        </div>
      )}
    </div>
  );
}
