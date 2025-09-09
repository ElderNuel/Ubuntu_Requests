# 🌍 Ubuntu-Inspired Image Fetcher

> *“I am because we are” – The Wisdom of Ubuntu*

This project is a **Python-based image fetcher** inspired by the Ubuntu philosophy of **community, respect, sharing, and practicality**.
It connects to the global community of the internet, respectfully fetches images, and organizes them for later appreciation.

---

## ✨ Features

* 📂 Automatically creates a **Fetched\_Images** directory to store images
* 🌍 Accepts **one or multiple URLs** at once
* ✅ Validates that downloaded files are actually images
* 🔄 Prevents **duplicate downloads** using content hashing
* ⚠️ Handles errors gracefully without crashing
* 🛡️ Uses respectful HTTP headers to connect responsibly

---

## 🛠️ Requirements

* Python **3.7+**
* [requests](https://docs.python-requests.org/en/latest/) library

Install dependencies:

```bash
pip install requests
```

---

## 🚀 Usage

Run the script in your terminal:

```bash
python Ubuntu_Requests.py
```

When prompted, enter one or more image URLs separated by spaces:

```
🌍 Enter image URL(s), separated by spaces:
> https://example.com/cat.jpg https://example.com/dog.png
```

The fetched images will be saved in the **Fetched\_Images/** directory.

---

## 🧩 Example Output

```
✅ Successfully fetched: Fetched_Images/cat.jpg
⏩ Skipping https://example.com/dog.png - Duplicate image already downloaded.
⚠️ Skipping https://example.com/file.txt - Not an image (Content-Type: text/plain)
❌ Error fetching https://badlink.com/pic.jpg: 404 Client Error: Not Found
```

---

## 🔐 Safety & Precautions

When downloading files from the internet:

* ✔️ Verify the **Content-Type** to ensure files are images
* ✔️ Check **Content-Length** to avoid excessively large files (optional)
* ✔️ Use a **User-Agent header** to prevent being flagged as a bot
* ✔️ Avoid downloading from untrusted sources

---

## 🧠 Challenge Extensions

* [x] Handle multiple URLs in one run
* [x] Prevent duplicate downloads
* [x] Check important HTTP headers (`Content-Type`, `Content-Length`)
* [ ] (Optional) Add a file size limit to avoid harmful/huge files

---

## 🌱 Ubuntu Principles Reflected

* **Community** → Connects with the wider web to fetch resources
* **Respect** → Graceful error handling and responsible requests
* **Sharing** → Organizes images for easy access and reuse
* **Practicality** → Provides a useful and real-world tool

---

## 📜 License

This project is provided for educational purposes.
Feel free to share and adapt in the spirit of Ubuntu.
