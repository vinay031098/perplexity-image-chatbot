# Perplexity Image Chatbot 🤖

**An end-to-end chatbot application that combines Perplexity AI for intelligent responses with image search to provide contextual visuals.**

---

## Features ✨

- 💬 **AI-Powered Chat** - Leverages Perplexity API for intelligent, context-aware responses
- 🖼️ **Image Integration** - Automatically fetches relevant images for queries via Pixabay API
- 🎨 **Modern UI** - Clean, responsive interface with smooth animations
- ⚡ **Real-time Processing** - Instant responses with streaming updates
- 🔄 **CORS-Enabled** - Full cross-origin support for frontend flexibility
- 🛡️ **Production-Ready** - Error handling, timeouts, and rate limiting

---

## Project Structure 📁

```
perplexity-image-chatbot/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── requirements.txt        # Python dependencies
│   └── .env.example           # Environment variables template
├── frontend/
│   └── index.html             # React-free responsive UI
├── README.md                  # This file
├── LICENSE                    # MIT License
└── .gitignore                 # Git ignore rules
```

---

## Tech Stack 🛠️

### Backend
- **Flask** - Lightweight Python web framework
- **Requests** - HTTP library for API calls
- **Python-dotenv** - Environment variable management
- **Flask-CORS** - Cross-Origin Resource Sharing support

### Frontend
- **Vanilla JavaScript** - No framework dependencies
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations

### APIs
- **Perplexity AI** - Advanced language model
- **Pixabay** - Free image search and download

---

## Getting Started 🚀

### Prerequisites

- Python 3.8+
- Perplexity API Key (from https://www.perplexity.ai/)
- Pixabay API Key (from https://pixabay.com/api/)

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/vinay031098/perplexity-image-chatbot.git
cd perplexity-image-chatbot
```

#### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

#### 3. Configure Environment Variables

Edit `backend/.env`:
```env
PERPLEXITY_API_KEY=your_perplexity_api_key_here
PIXABAY_API_KEY=your_pixabay_api_key_here
```

#### 4. Start the Backend Server

```bash
python app.py
```

Server will run on `http://localhost:5000`

#### 5. Open Frontend

- Open `frontend/index.html` in your web browser
- Or serve it with any local server:
  ```bash
  cd frontend
  python -m http.server 8000
  ```

---

## API Endpoints 🔗

### POST `/api/chat`
Sends a message and receives AI response with relevant images.

**Request:**
```json
{
  "message": "Tell me about quantum computing"
}
```

**Response:**
```json
{
  "message": "Tell me about quantum computing",
  "response": "Quantum computing uses quantum mechanics principles...",
  "images": [
    {
      "url": "https://pixabay.com/image.jpg",
      "thumbnail": "https://pixabay.com/thumb.jpg",
      "user": "photographer_name"
    }
  ]
}
```

### POST `/api/search-images`
Search for images without AI response.

**Request:**
```json
{
  "query": "nature landscape"
}
```

### GET `/api/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

---

## Usage Examples 📚

### Chat Interface

1. Type any question in the input field
2. Press Enter or click Send
3. View AI response with relevant images
4. Images appear in a grid below the response
5. Click images to view full resolution

### Sample Queries

- "What are the health benefits of exercise?"
- "How do solar panels work?"
- "Tell me about ancient Egyptian civilization"
- "What is machine learning?"

---

## Development 💻

### Backend Development

```python
# Adding a new endpoint
@app.route('/api/your-endpoint', methods=['POST'])
def your_endpoint():
    data = request.json
    # Process data
    return jsonify({"result": "success"})
```

### Frontend Development

- All code is in `frontend/index.html`
- Modify CSS in the `<style>` section
- Modify JS in the `<script>` section
- No build process required

---

## Troubleshooting 🔧

### CORS Errors
- Ensure backend is running on `http://localhost:5000`
- Frontend should access from `http://localhost` or file protocol

### API Key Errors
- Verify `.env` file exists in `backend/` directory
- Check API keys are correct and have remaining quota
- Ensure no spaces in `.env` values

### Images Not Loading
- Check Pixabay API key is valid
- Verify internet connection
- Check browser console for errors

---

## Performance Tips ⚡

1. **Optimize API Calls** - Cache frequent queries
2. **Image Lazy Loading** - Load images as needed
3. **Rate Limiting** - Implement per-user limits
4. **Database** - Add PostgreSQL for chat history

---

## Deployment 🌐

### Deploy Backend (Heroku)

```bash
heroku create your-app-name
heroku config:set PERPLEXITY_API_KEY=your_key
heroku config:set PIXABAY_API_KEY=your_key
git push heroku main
```

### Deploy Frontend (Vercel/Netlify)

1. Push to GitHub
2. Connect repository to Vercel/Netlify
3. Set backend URL in environment

---

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Future Enhancements 🚀

- [ ] Chat history with database
- [ ] User authentication
- [ ] Multiple conversation threads
- [ ] Image generation with DALL-E
- [ ] Voice input/output
- [ ] Mobile app (React Native)
- [ ] Advanced analytics
- [ ] Custom models support

---

## License 📄

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## Support & Contact 💬

- **GitHub Issues** - Report bugs and request features
- **Email** - vinay031098@example.com
- **Twitter** - @yourtwitterhandle

---

## Acknowledgments 🙏

- Perplexity AI for powerful language models
- Pixabay for free stock images
- Flask community for excellent framework
- All contributors and supporters

---

**Made with ❤️ by [Your Name](https://github.com/vinay031098)**
