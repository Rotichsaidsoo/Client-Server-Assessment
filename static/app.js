const sendButton = document.getElementById("send");
const messageInput = document.getElementById("message");
const statusText = document.getElementById("status");
const result = document.getElementById("result");

async function sendMessage() {
  const message = messageInput.value.trim();
  if (!message) {
    statusText.textContent = "Please enter a message first.";
    statusText.className = "status error";
    result.hidden = true;
    messageInput.focus();
    return;
  }

  sendButton.disabled = true;
  statusText.textContent = "Sending request to localhost server...";
  statusText.className = "status";
  result.hidden = true;

  try {
    const response = await fetch("/api/message", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });
    const data = await response.json();
    if (!response.ok || !data.ok) throw new Error(data.error || "Request failed.");

    document.getElementById("received").textContent = data.received;
    document.getElementById("reply").textContent = data.reply;
    document.getElementById("serverStatus").textContent = data.status;
    statusText.textContent = "HTTP communication successful (200 OK).";
    statusText.className = "status success";
    result.hidden = false;
  } catch (error) {
    statusText.textContent = "Could not reach the server. Make sure server.py is running.";
    statusText.className = "status error";
  } finally {
    sendButton.disabled = false;
  }
}

sendButton.addEventListener("click", sendMessage);
messageInput.addEventListener("keydown", event => {
  if (event.key === "Enter") sendMessage();
});
