# 🧺 Laundry Management System

This is a simple command-line interface (CLI) application written in Python for managing laundry orders for students. It allows users to add, view, search, update, and delete laundry orders, with data persistently stored in a local file.

## ✨ Features

* **Add Order:** Record a new laundry order, including student roll number, name, selected items, and calculated total cost.
* **View Orders:** Display all existing laundry orders.
* **Search Order:** Find a specific order using the student's roll number.
* **Update Order:** Modify the student's name and re-select items for an existing order.
* **Delete Order:** Remove an order from the system using the roll number.
* **Data Persistence:** Orders are saved to and loaded from a file named `laundry.txt`.

## ⚙️ Setup and Installation

### Prerequisites

* **Python 3.x** must be installed on your system.

### Running the Program

1.  **Save the code:** Save the provided Python code into a file named `laundry_mgmt.py`.
2.  **Run from terminal:** Open your terminal or command prompt and navigate to the directory where you saved the file. Execute the program using the Python interpreter:

    ```bash
    python laundry_mgmt.py
    ```

3.  **Data File:** The program will automatically create a file named **`laundry.txt`** in the same directory to store the orders.

## 🚀 How to Use

When the program starts, it presents a main menu. Enter the number corresponding to the action you wish to perform.

### Main Menu

1. Add Laundry Order

2. View Laundry Orders

3. Search for an Order

4. Update Laundry Order

5. Delete Laundry Order

6. Exit


### Action Details

* **1. Add Laundry Order:** Prompts for Roll Number and Name. You will then select items and quantities from a numbered list (1-6). Type **`done`** to finalize the items and calculate the total cost.
* **2. View Laundry Orders:** Displays a list of all orders, showing Roll Number, Name, Items, and Total Cost.
* **3. Search for an Order:** Prompts for a **Roll Number** to find and display the details of a specific order.
* **4. Update Laundry Order:** Prompts for a Roll Number. You can update the student's name and will be guided to re-select **all** items for the order (replacing the old item list).
* **5. Delete Laundry Order:** Prompts for a **Roll Number** and permanently removes that order from the system and the file.
* **6. Exit:** Closes the program.

---

## 💾 Data Format

The program saves and loads data from the `laundry.txt` file using a **Comma Separated Value (CSV)** format. Each line represents a single order:

```csv
roll_no,name,items_string,cost_string
