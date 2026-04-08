import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!message.trim()) return;

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });

      const data = await response.json();
      setAnswer(data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("エラーが発生しました");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "40px auto", padding: "16px" }}>
      <h1>RAG App</h1>

      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="質問を入力"
        rows={5}
        style={{ width: "100%", marginBottom: "12px" }}
      />

      <button onClick={handleSend} disabled={loading}>
        {loading ? "送信中..." : "送信"}
      </button>

      <div style={{ marginTop: "24px" }}>
        <h2>回答</h2>
        <p>{answer}</p>
      </div>
    </div>
  );
}

export default App;