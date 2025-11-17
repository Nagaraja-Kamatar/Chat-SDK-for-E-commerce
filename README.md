🛍️ AI-Powered E-Commerce Chat SDK
A plug-and-play AI Chat SDK designed for online shopping websites.
This SDK enables customers to chat using text, voice (English, Hindi, Arabic), or product images, and receive AI-powered product recommendations based on their past orders, browsing history, and clickstream behavior.
Built with OpenAI Agents SDK, FastAPI, and vector search systems, the SDK integrates seamlessly into any e-commerce frontend.
🚀 Features
Chat SDK for Websites
Embeddable JS Widget for any e-commerce site
Supports mobile + desktop
Multi-Modal Product Discovery
Text-based search
Image upload → similar product recommendations
Voice input (English / Hindi / Arabic)
Personalized Recommendations
Uses historical:
Orders
Clickstream data
Browsing behavior
AI Shopping Assistant
Answers product queries
Suggests alternatives
Helps in cart decisions
Shows similar items based on image
Conversation Memory
Maintains context across multiple messages
User ID–based personalization
Robust API Layer
Tools: recommendations, image similarity, voice transcript, order lookup
Logs tool calls and conversation data
📦 Requirements
Python 3.9+
Node.js (for the web widget)
OpenAI API key
FFmpeg (for voice processing)
🛠️ Setup
1. Clone the repository
git clone https://github.com/yourusername/chat-sdk-ecommerce.git
cd chat-sdk-ecommerce
2. Install Python dependencies
pip install -r requirements.txt
3. Set environment variables
Duplicate the example file:
cp .env.example .env
Add your OpenAI API key inside .env:
OPENAI_API_KEY=your_key_here
4. Install JS widget dependencies
cd widget
npm install
🔐 Security Notes
Never commit .env or real API keys into GitHub.
.env is already in .gitignore.
For deployment, always use:
secure secret managers
environment variables
▶️ Running the API Server
Start the FastAPI backend:
python main.py
Your API will be available at:
http://localhost:8000
🧩 API Endpoints
POST /chat
Send a message or image/voice to the AI shopping assistant.
Request body:
{
  "message": "Show me similar sneakers",
  "image": "optional_base64_image",
  "audio": "optional_base64_audio",
  "thread_id": "optional_thread_id",
  "user_id": "optional_user_id"
}
Example response:
{
  "response": "Here are similar sneakers based on your past purchases.",
  "products": [
    { "id": "SKU123", "name": "AirMax Runner" }
  ],
  "thread_id": "thread_abc_123"
}
💬 Example Interactions
📝 Text
User: "Show me dresses similar to the one I bought last month."
Assistant: "Based on your order history, here are 5 similar dresses you may like."
🖼️ Image
User uploads: image of a sneaker  
Assistant: "Here are visually similar sneakers available on our store."
🎤 Voice
User (Hindi): "मुझे रेड कलर की पार्टी वियर ड्रेस दिखाओ"
Assistant: "यहाँ कुछ रेड पार्टी वियर ड्रेसेज़ हैं जो आपको पसंद आ सकती हैं।"
🧪 Example Past Work (Github-Style References)
These are example-style descriptions of past components that inspired this design:
Image Similarity Search
Built using CLIP embeddings + FAISS index
("Product Visual AI Search Engine")
Voice-to-Text Conversion System
Multi-language STT (English/Hindi/Arabic) using Whisper API
("AI Multilingual Voice Assistant")
Personalized Recommendation Engine
Merged order history + clickstream + embeddings
("User Behavior-Based Ecommerce Recommender")
Chat SDK + Widget
Embeddable JS widget for ecommerce product search
("AI Chat Widget for Retail")
Add your GitHub links here if you have them.
📄 License
MIT License
Feel free to modify, distribute, and use this project commercially.
