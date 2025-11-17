# 🛍️ AI-Powered E-Commerce Chat SDK

A plug-and-play **AI Chat SDK** designed to integrate seamlessly with any e-commerce website.

This SDK enables customers to interact using **text**, **voice** (English, Hindi, Arabic), or **product images**, and receive AI-powered personalized product recommendations driven by:

* Order history
* Browsing behavior
* Clickstream data

Built using **OpenAI Agents SDK**, **FastAPI**, and **vector similarity search**, this SDK provides a modern, multimodal shopping assistant experience.

---

## 🚀 Features

### **Chat SDK for Websites**

* Embeddable JavaScript widget
* Mobile + desktop compatible
* Plug-and-play integration

### **Multi-Modal Product Discovery**

* Smart text-based query search
* Image upload → similar product identification
* Voice input (English / Hindi / Arabic)

### **Personalized Recommendations**

Uses customer-specific data:

* Order history
* Clickstream events
* Browsing patterns

### **AI Shopping Assistant**

* Answers product-related questions
* Suggests alternatives
* Helps with cart decisions
* Shows similar items using image-based search

### **Conversation Memory**

* Maintains multi-turn dialog context
* Personalization using `user_id`

### **Robust API Layer**

Includes tools for:

* Product recommendations
* Image similarity search
* Voice transcription
* Order lookup
* Tool-call + conversation logging

---

## 📦 Requirements

* **Python 3.9+**
* **Node.js** (for the embeddable widget)
* **OpenAI API key**
* **FFmpeg** (required for voice/audio processing)

---

## 🛠️ Setup

### **1. Clone the repository**

```bash
git clone https://github.com/yourusername/chat-sdk-ecommerce.git
cd chat-sdk-ecommerce
```

### **2. Install Python dependencies**

```bash
pip install -r requirements.txt
```

### **3. Configure environment variables**

Duplicate the example file:

```bash
cp .env.example .env
```

Add your OpenAI API key:

```
OPENAI_API_KEY=your_key_here
```

### **4. Install JS widget dependencies**

```bash
cd widget
npm install
```

---

## 🔐 Security Notes

* Never commit `.env` files or real API keys to GitHub.
* `.env` is already included in `.gitignore`.
* For deployment, always use:

  * Cloud secret managers (AWS / GCP / Azure)
  * Environment variables

---

## ▶️ Running the API Server

Start the FastAPI backend:

```bash
python main.py
```

API will be available at:

**[http://localhost:8000](http://localhost:8000)**

---

## 🧩 API Endpoints

### **POST /chat**

Sends text, image, or audio message to the AI assistant.

#### **Request Body**

```json
{
  "message": "Show me similar sneakers",
  "image": "optional_base64_image",
  "audio": "optional_base64_audio",
  "thread_id": "optional_thread_id",
  "user_id": "optional_user_id"
}
```

#### **Example Response**

```json
{
  "response": "Here are similar sneakers based on your past purchases.",
  "products": [
    { "id": "SKU123", "name": "AirMax Runner" }
  ],
  "thread_id": "thread_abc_123"
}
```

---

## 💬 Example Interactions

### **📝 Text Query**

**User:** “Show me dresses similar to the one I bought last month.”
**Assistant:** “Here are 5 similar dresses you may like.”

### **🖼️ Image Upload**

User uploads sneaker image →
**Assistant:** “Here are visually similar sneakers available in our store.”

### **🎤 Voice Query (Hindi)**

**User:** “मुझे रेड कलर की पार्टी वियर ड्रेस दिखाओ”
**Assistant:** “यहाँ कुछ रेड पार्टी वियर ड्रेसेज़ हैं जो आपको पसंद आ सकती हैं।”

---

## 🧪 Example Past Work (GitHub-Style References)

### **Image Similarity Search**

* Built using CLIP embeddings + FAISS index
  *("Product Visual AI Search Engine")*

### **Voice-to-Text System**

* Multilingual Whisper API integration (English/Hindi/Arabic)
  *("AI Multilingual Voice Assistant")*

### **Personalized Recommendation Engine**

* Order history + clickstream + embeddings
  *("Behavior-Based Ecommerce Recommender")*

### **Chat SDK + Web Widget**

* Embeddable widget for ecommerce storefronts
  *("AI Chat Widget for Retail")*

> Add your actual GitHub links here.

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to modify, distribute, and use it commercially.

---
