import React, { useState } from "react";
import axios from "axios";

export default function Upload({ setResult }) {
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false); // untuk indikator loading

  const handleUpload = async () => {
    if (!image) {
      alert("Pilih gambar dulu!");
      return;
    }

    setResult(null); // reset result sebelum upload baru
    setLoading(true);

    const formData = new FormData();
    formData.append("image", image);

    try {
      const res = await axios.post("http://127.0.0.1:5000/predict", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setResult(res.data); // langsung update result
    } catch (error) {
      console.error(error);
      alert("Terjadi kesalahan. Coba lagi.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-container">
      <input
        type="file"
        accept="image/*"
        onChange={(e) => setImage(e.target.files[0])}
      />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Memproses..." : "Prediksi Katarak"}
      </button>
    </div>
  );
}
