# Party Details Form - PyQt6

This project is a simple desktop application built using **Python** and **PyQt6**.
The UI is based on the provided Party Details Form design and includes a top navigation bar, input fields, and bottom action buttons. 

## Features

* Clean and responsive PyQt6 layout
* Top action bar with buttons like New, Modify, Delete, Search, etc.
* Input fields for:

  * Party Code
  * Date
  * Party Name
  * Mobile
  * Email
  * GST Number
  * Price List
  * Address
* Save and Clear functionality
* Custom styling using Qt Style Sheets

## Technologies Used

* Python 3
* PyQt6

## How to Run

1. Install PyQt6:

```bash
pip install PyQt6
```

2. Run the application:

```bash
python main.py
```

## Project Structure

```text
project-folder/
│
├── main.py
├── down_arrow.svg
└── README.md
```

## Notes

* The application currently prints saved form data to the console.
* Layouts are created using `QVBoxLayout` and `QHBoxLayout`.
* Styling is done directly inside the application using `setStyleSheet()`.

## Screenshot

The UI is designed to closely match the reference form provided in the assignment.

---

Made for learning and practice with PyQt6.
