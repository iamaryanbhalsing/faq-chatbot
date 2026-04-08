# FAQ Chatbot

A simple yet powerful FAQ (Frequently Asked Questions) chatbot built with Flask, NLTK, and Cosine Similarity. The chatbot intelligently matches user queries to the most relevant FAQ answers using natural language processing.

## Features

- **Intelligent Matching**: Uses cosine similarity with TF-IDF vectorization to find the best matching FAQ answer
- **Responsive UI**: Modern chat interface with real-time message updates
- **Easy Customization**: Simple JSON-based FAQ configuration
- **Deployed on Render**: Live web application ready to use
- **Lightweight**: Minimal dependencies and fast response times

## Tech Stack

- **Backend**: Flask (Python web framework)
- **NLP**: NLTK (Natural Language Toolkit)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render (cloud platform)
- **Similarity Matching**: Scikit-learn (TF-IDF and Cosine Similarity)

## Project Structure

```
faq-chatbot/
├── app.py              # Flask backend with /chat endpoint
├── faqs.json           # FAQ data (questions and answers)
├── requirements.txt    # Python dependencies
├── Procfile            # Render deployment configuration
├── templates/
│   └── index.html       # Chat UI
├── static/
│   ├── style.css        # Styling
│   └── script.js        # Frontend JavaScript
└── README.md          # This file
```

## How It Works

1. **User Input**: User types a question in the chat interface
2. **Backend Processing**: Flask receives the query and processes it
3. **Similarity Matching**: NLTK and scikit-learn compute TF-IDF vectors and cosine similarity
4. **Response Delivery**: The most relevant FAQ answer is returned to the user
5. **Display**: JavaScript updates the chat UI in real-time

## Setup Instructions

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/iamaryanbhalsing/faq-chatbot.git
   cd faq-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000`

### Customizing FAQs

Edit `faqs.json` to add your own questions and answers:

```json
{
  "faqs": [
    {
      "question": "What is your product?",
      "answer": "Our product is an intelligent FAQ chatbot."
    },
    {
      "question": "How do I use it?",
      "answer": "Simply type your question and the chatbot will provide relevant answers."
    }
  ]
}
```

## API Endpoints

### POST /chat

Sends a user query and receives a matching FAQ answer.

**Request:**
```json
{
  "query": "What is your product?"
}
```

**Response:**
```json
{
  "response": "Our product is an intelligent FAQ chatbot.",
  "confidence": 0.95
}
```

## Deployment on Render

1. Push your code to GitHub
2. Sign up on [Render](https://render.com)
3. Connect your GitHub repository
4. Create a new Web Service
5. Set the build command to `pip install -r requirements.txt`
6. Set the start command to `gunicorn app:app`
7. Deploy!


## Technologies Used

- **Flask**: Web framework
- **NLTK**: Natural language processing
- **Scikit-learn**: Machine learning library for TF-IDF and cosine similarity
- **Gunicorn**: WSGI HTTP server for production
- **Render**: Cloud hosting platform

## Future Enhancements

- [ ] Add conversation history
- [ ] Implement user feedback mechanism
- [ ] Add support for multiple languages
- [ ] Integrate with chatbot platforms (Slack, Discord, etc.)
- [ ] Add advanced NLP models (Transformers)
- [ ] Implement user authentication

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## License

This project is open source and available under the MIT License.

## Author

Created by [Aryan Bhalsing](https://github.com/iamaryanbhalsing)

**Connect with me:**

- **LinkedIn:** [linkedin.com/in/iamaryanbhalsing](https://linkedin.com/in/iamaryanbhalsing)
- **Instagram:** [@iamaryanbhalsing](https://instagram.com/iamaryanbhalsing)
- **Email:** aryanbhalsing7090@gmail.com

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Happy Chatting! 🚀**
