// Handle form submission
document.getElementById('messageForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  console.log("✅ Form submitted");

  const data = {
    recipient_number: document.getElementById('recipient_number').value,
    message_text: document.getElementById('message_text').value,
  };

  try {
    const res = await fetch('http://127.0.0.1:8080/api/messages/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    if (res.ok) {
      console.log("✅ Message saved to backend");
      document.getElementById('messageForm').reset();
      loadMessages();
    } else {
      const error = await res.json();
      console.error("❌ API error:", error);
      alert("Could not save message. See console for details.");
    }
  } catch (err) {
    console.error("❌ Fetch error:", err);
    alert("A connection error occurred. Please try again.");
  }
});

// Load all saved messages from backend
async function loadMessages() {
  try {
    const res = await fetch('http://127.0.0.1:8080/api/messages/');
    const messages = await res.json();

    const list = document.getElementById('messageList');
    list.innerHTML = '';

    if (messages.length === 0) {
      list.innerHTML = '<li>No messages yet.</li>';
    }

    messages.forEach(msg => {
      const li = document.createElement('li');
      li.textContent = `[${msg.status}] To ${msg.recipient_number}: ${msg.message_text}`;
      list.appendChild(li);
    });

    console.log("📦 Messages loaded:", messages);

  } catch (err) {
    console.error("❌ Error loading messages:", err);
  }
}

// Load messages on page load
loadMessages();