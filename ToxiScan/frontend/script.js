function analyzeText() {
    let text = document.getElementById("textInput").value;

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = 
            data.toxic ? "⚠️ Toxic Comment Detected!" : "✅ Safe Comment";
    })
    .catch(error => console.error("Error:", error));
}
