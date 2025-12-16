# 7charUrl-FrontEnd

**Frontend application for the 7charUrl URL Shortener** — a web interface that allows users to shorten long URLs into unique 7-character short links and interact with the URL shortening backend API.

## 🚀 Project Overview

7charUrl-FrontEnd is the **client-side UI** for the 7charUrl service. It lets users:

* Enter a long URL
* Generate a short 7-character URL
* View & copy the shortened link
* (Optionally) Show user feedback on success/error

The frontend communicates with a backend API to perform URL shortening operations. ([GitHub][1])

---

## 🧠 Features

✔ Simple and responsive UI for shortening URLs
✔ Connects to the backend REST API
✔ Displays the generated short link
✔ Copy functionality for easy sharing
✔ Error feedback for invalid URLs or failed API requests

---

## 📦 Tech Stack

> Replace these with your actual technologies if different

* **React** (or your chosen JS framework)
* **Tailwind CSS / Bootstrap / CSS** — styles
* **Vite / Create React App / Next.js** — frontend tooling
* **Fetch / Axios** — HTTP requests

---

## 🔧 Getting Started

### 🗂️ Prerequisites

Make sure you have the following installed:

* Node.js (>=14)
* npm or yarn
* A running backend API for 7charUrl

### 📌 Installation

1. **Clone the repo:**

   ```bash
   git clone https://github.com/Dhruvdangi03/7charUrl-FrontEnd.git
   cd 7charUrl-FrontEnd
   ```

2. **Install dependencies:**

   ```bash
   npm install
   # or
   yarn install
   ```

3. **Set up environment variables:**
   Create a `.env` file (if applicable) and add your API base URL:

   ```
   REACT_APP_API_BASE_URL=https://your-backend-url
   ```

4. **Start dev server:**

   ```bash
   npm start
   # or
   yarn start
   ```

5. Open the app in your browser:

   ```
   http://localhost:3000
   ```

---

## 🛠 Usage

1. Enter the long URL you want to shorten.
2. Click **Generate** (or similar).
3. The app sends the request to the backend API.
4. You will receive a short 7-character link.
5. Copy the link to share it easily.

---

## 📡 API Integration (Example)

This frontend calls your backend API — for example:

| Action           | Endpoint           | Method |
| ---------------- | ------------------ | ------ |
| Create short URL | `/shorten`         | POST   |
| Get analytics    | `/analytics/:code` | GET    |

> Update these with your actual backend routes.

---

## 📁 Project Structure

```
7charUrl-FrontEnd/
├─ src/
│   ├─ components/
│   ├─ services/
│   ├─ utils/
│   ├─ App.js
│   └─ index.js
├─ public/
├─ .gitignore
├─ package.json
├─ README.md
└─ ...
```

---

## ✨ Contributing

Contributions are welcome! If you’d like to improve the UI, add features, or fix bugs:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add some feature"`
4. Push to your fork: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📝 License

MIT License — see the **LICENSE** file for details.

---
