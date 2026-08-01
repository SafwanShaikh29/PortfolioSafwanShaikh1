# 👨‍💻 Safwan Feroz Shaikh | AI & Data Science Portfolio

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=white)

A modern, responsive, and stylish personal portfolio website featuring **Glassmorphism design**, **smooth scroll animations**, and a **custom interactive cursor**. Built entirely with vanilla HTML, CSS, and JavaScript.

## 🚀 Live Demo
[View Live Portfolio](https://your-username.github.io/portfolio)

---

## ✨ Key Features

* **🎨 Glassmorphism UI:** Modern translucent card effects with background blur and glowing gradients.
* **🖱️ Custom Cursor:** A magnetic "follower" cursor that expands when hovering over interactive elements.
* **🎭 Scroll Animations:** Sections smoothly fade in and slide up as the user scrolls down (Intersection Observer).
* **📱 Fully Responsive:** Optimized layout for desktops, tablets, and mobile devices.
* **📄 Downloadable Resume:** Dedicated button to directly download the user's CV/Resume.
* **✉️ Contact Form:** Stylized input fields ready for backend integration.

---

## 🛠️ Installation & Setup

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [https://github.com/your-username/portfolio.svg](https://github.com/your-username/portfolio.svg)
    ```

2.  **Open the file:**
    Simply double-click `index.html` to open it in your web browser. No local server or dependencies (Node.js/npm) are required!

---

## ⚙️ How to Configure the "Download Resume" Button

To make the download button work with your actual PDF file, follow these steps:

1.  Place your PDF resume file in the same folder as `index.html`.
2.  Rename your file to `Safwan_Shaikh_Resume.pdf` (or update the code to match your filename).
3.  Edit **Line 330** in `index.html`:

    ```html
    <a href="./Safwan_Shaikh_Resume.pdf" download="Safwan_Shaikh_Resume.pdf" class="resume-btn hover-trigger">
    ```

> **Note:** The `download` attribute forces the browser to download the file instead of opening it in a new tab.

---

## 📂 File Structure

```text
/Portfolio
│
├── index.html        # Main HTML file (contains all CSS & JS)
├── assets/           # (Optional) Folder for images/icons
└── Safwan_Resume.pdf # Your actual resume file