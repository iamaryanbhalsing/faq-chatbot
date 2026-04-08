// Get chatbox and send button elements
const chatbox = document.getElementById('chatbox');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Add event listeners
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (event) => {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

// Function to send message
function sendMessage() {
  const message = userInput.value.trim();
  
  if (message === '') {
    return;
  }
  
  // Display user message in chatbox
  displayMessage(message, 'user');
  
  // Clear input field
  userInput.value = '';
  
  // Send message to backend
  sendToBackend(message);
}

// Function to display message in chatbox
function displayMessage(message, sender) {
  const messageElement = document.createElement('li');
  messageElement.className = `chat ${sender}`;
  
  const paragraph = document.createElement('p');
  paragraph.textContent = message;
  
  messageElement.appendChild(paragraph);
  chatbox.appendChild(messageElement);
  
  // Auto-scroll to bottom
  chatbox.scrollTop = chatbox.scrollHeight;
}

// Function to send message to Flask backend
function sendToBackend(message) {
  fetch('/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message: message })
  })
  .then(response => response.json())
  .then(data => {
    // Display bot response
    displayMessage(data.reply, 'bot');
  })
  .catch(error => {
    console.error('Error:', error);
    displayMessage('Sorry, something went wrong. Please try again.', 'bot');
  });
}

// Focus on input field when page loads
window.addEventListener('load', () => {
  userInput.focus();
});
