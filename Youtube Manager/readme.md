

```markdown
# YouTube Video Manager

A simple command-line application to manage your YouTube video list using Python. This app allows you to **list**, **add**, **update**, and **delete** videos. Data is stored in a local `youtube.txt` file in JSON format, making it lightweight and easy to use without any database.

---

## 📋 Features

- ✅ List all videos
- ➕ Add a new video
- 🔁 Update existing video details
- ❌ Delete a video
- 💾 Persistent storage using JSON file (`youtube.txt`)
- 🖥️ Simple console-based menu interface

---

## 🛠️ Technologies Used

- **Python 3.x**
- **JSON** – for data persistence

---

## 📂 File Structure

```
youtube_video_manager/
│
├── youtube.txt         # Stores video data in JSON format (auto-generated)
├── main.py             # Main application script
└── README.md           # Project documentation
```

> Note: `youtube.txt` is created automatically when you add your first video.

---

## ▶️ How to Run

1. **Clone the repository (or download the script):**
   ```bash
   git clone https://github.com/your-username/youtube-video-manager.git
   cd youtube-video-manager
   ```

2. **Run the Python script:**
   ```bash
   python main.py
   ```

3. **Follow the on-screen menu** to manage your YouTube videos.

---

## 🧭 Menu Options

| Option | Description |
|-------|-------------|
| 1     | List all videos |
| 2     | Add a new YouTube video |
| 3     | Update a video's name or duration |
| 4     | Delete a video from the list |
| 5     | Exit the application |

---

## 📷 Example Usage

```
YouTube Manager | choose an option 
1. List all youtube videos 
2. Add a youtube video 
3. Update a youtube video details 
4. Delete a youtube video 
5. Exit the app 
Enter your choice:- 2
Enter video name: Learn Python in 1 Hour
Enter video time: 1:00:00
```

After adding videos, the `youtube.txt` will look like:
```json
[
    {"name": "Learn Python in 1 Hour", "time": "1:00:00"}
]
```

---

## 📝 Notes

- The app uses zero external dependencies.
- Data is saved locally, so it's ideal for personal use or learning file handling in Python.
- Invalid indices during update/delete are handled gracefully.

---

## 🙌 Contributions

Contributions are welcome! Feel free to open issues or pull requests for improvements, bug fixes, or UI enhancements (like adding color or using a database).

---

## 📎 License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).

---

> Developed with ❤️ using Python
```
