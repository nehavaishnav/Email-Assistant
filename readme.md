# Email Assistant

An AI-powered email assistant designed to streamline your email management by providing intelligent summarizations and context-aware reply suggestions. This project utilizes Flask for the backend and integrates AI models to process and manage emails efficiently.

## Features

- **AI-Powered Email Summarization**: Automatically generates concise summaries of your emails to help you quickly understand the content without reading the entire message.

- **Context-Aware Reply Suggestions**: Provides intelligent reply suggestions based on the context of the email, enabling faster and more efficient responses.

- **Mock Email Data for Testing**: Includes `mockEmail.json` to simulate email data, allowing for testing and development without the need for actual email accounts.

- **Web-Based Interface**: Offers a user-friendly web interface built with Flask templates for seamless interaction with the assistant.


## 📸 Screenshots
![App UI](https://github.com/nehavaishnav/Email-Assistant/blob/main/assets/1.png)  
![App UI](https://github.com/nehavaishnav/Email-Assistant/blob/main/assets/2.png)  

## Project Structure

```
Email-Assistant/
├── templates/
│   └── index.html       # Main HTML template for the web interface
├── app.py                  # Main Flask application script
├── mockEmail.json          # Sample email data for testing
├── requirements.txt        # List of Python dependencies
├── render.yaml             # Deployment configuration for Render
└── README.md               # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/nehavaishnav/Email-Assistant.git
   cd Email-Assistant
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   python app.py
   ```

   Access the application at `http://127.0.0.1:5000` in your web browser.

## Testing with Mock Data

The `mockEmail.json` file contains sample email data that the application uses to demonstrate its summarization and reply suggestion features. This allows you to test the application's functionality without connecting to a real email account.

## Future Enhancements

- **Integration with Gmail API**: Implement OAuth authentication to fetch and manage real emails from Gmail accounts.

- **Advanced AI Models**: Incorporate more sophisticated natural language processing models to improve the accuracy and relevance of summaries and reply suggestions.

- **User Authentication**: Add user authentication to provide personalized experiences and secure access to emails.

- **Enhanced User Interface**: Develop a more intuitive and responsive frontend to improve user experience.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or feedback, please open an issue on the [GitHub repository](https://github.com/nehavaishnav/Email-Assistant/issues).

---

*This README provides an overview of the Email Assistant project, including its features, setup instructions, and future development plans.* 
