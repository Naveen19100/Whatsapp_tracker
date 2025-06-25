document.getElementById('messageForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const data = {
    recipient_number: document.getElementById('recipient_number').value,
    message_text: document.getElementById('message_text').value,
  };

  const res = await fetch('/api/messages/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (res.ok) {
    loadMessages();
  }
});

async function loadMessages() {
  const res = await fetch('/api/messages/');
  const messages = await res.json();
  const list = document.getElementById('messageList');
  list.innerHTML = '';
  messages.forEach(msg => {
    const li = document.createElement('li');
    li.textContent = `[${msg.status}] To ${msg.recipient_number}: ${msg.message_text}`;
    list.appendChild(li);
  });
}

loadMessages();