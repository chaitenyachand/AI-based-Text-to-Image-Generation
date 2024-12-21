# **🌟 Text-to-Image Generator using Stable Diffusion**

## **📋 Project Overview**
The **Text-to-Image Generator** is an AI-powered web application that converts descriptive text prompts into stunning, high-quality images. Using the **Stable Diffusion model** from Hugging Face, the application provides a user-friendly interface with multilingual support, allowing users to create and visualize unique images in their preferred language.

---

## **✨ Features**
- **AI-Driven Image Generation**: Generate high-quality images using text prompts.
- **Multilingual Support**: Input prompts in over 100 languages via Google Translate API.
- **Voice Input Integration**: Easily input prompts using speech recognition.
- **Responsive Design**: Cross-browser compatibility and mobile-friendly interface.
- **Save and Share Images**: Download or share generated images effortlessly.

---

## **🛠️ Tech Stack**
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **APIs**: 
  - [Hugging Face API](https://huggingface.co/) for Stable Diffusion.
  - [Google Translate API](https://cloud.google.com/translate) for multilingual support.
- **Libraries**: 
  - `Flask-CORS` for cross-origin requests.
  - `Requests` for API communication.
  - `Pillow (PIL)` for image handling.
  - `Base64` for image encoding.
- **Other**: SpeechRecognition API for voice input.

---

## **🚀 Installation and Setup**

### **Prerequisites**
- Python 3.8 or higher
- Virtual environment (optional but recommended)

### **Steps**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/text-to-image-generator.git
   cd text-to-image-generator
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Hugging Face API Key**:
   - Obtain a token from [Hugging Face](https://huggingface.co/).
   - Replace `your_token_here` in the code with your token.

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the App**:
   - Open your browser and navigate to `http://localhost:5000`.

---

## **🌐 How It Works**
1. Enter a descriptive text prompt (e.g., *"A futuristic city at sunset with flying cars"*).
2. Select your preferred language or use voice input.
3. Click the **Generate** button to create the image.
4. View, save, or share the generated images directly from the app.

---

## **📚 Project Structure**
```
📁 text-to-image-generator
├── 📂 static
│   ├── style.css        # Styling for the frontend
│   └── images           # Placeholder/loading images
├── 📂 templates
│   └── index.html       # Frontend HTML template
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```


## **💡 Key Challenges**
1. Managing API rate limits for Hugging Face and Google Translate.
2. Handling ambiguous or complex prompts for accurate image generation.
3. Ensuring cross-browser compatibility for a smooth user experience.

---

## **📈 Future Enhancements**
- **Customization Options**: Allow users to specify image style, resolution, or color palette.
- **User Accounts**: Add authentication to save user prompts and generated images.
- **Mobile App**: Extend the application to Android and iOS platforms.
- **Real-Time Feedback**: Provide users with intermediate previews during image generation.

---

## **🤝 Contributing**
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

---

## **📄 License**
This project is licensed under the [MIT License](LICENSE).

---

## **📬 Contact**
For questions or suggestions, feel free to reach out:

- **Email**: chaitenyachand@gmail.com  
- **GitHub**: [Chaitenya Chand](https://github.com/chaitenyachand)
