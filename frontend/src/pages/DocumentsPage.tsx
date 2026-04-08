import { useEffect, useState } from "react";

export default function DocumentsPage() {
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("error"));
  }, []);

  return (
    <div>
      <h2>Documents Page</h2>
      <p>Backend status: {status}</p>
    </div>
  );
}