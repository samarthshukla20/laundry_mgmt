# 🧺 Laundry Management System

## ⭐ Overview of the Project

The **Laundry Management System** is a simple, command-line interface (CLI) application developed in Python. It provides a digital solution for small-scale operations, such as student hostels or residential colleges, to manage laundry orders efficiently. The system replaces manual, error-prone record-keeping with an automated digital process for order entry, cost calculation, and data persistence.

The core functionality involves managing a list of laundry orders, which are saved to and loaded from a local file (`laundry.txt`), ensuring that all data persists between sessions.

---

## ✨ Features

The project provides a full range of CRUD (Create, Read, Update, Delete) operations:

* **Add Order (Create):** Record a new laundry order, automatically calculating the total cost based on the quantity and type of items selected.
* **View Orders (Read All):** Display a complete list of all recorded laundry orders.
* **Search Order (Read One):** Quickly find and display the details of a specific order using the student's **Roll Number**.
* **Update Order (Update):** Modify the student's name and replace the entire item list and recalculate the cost for an existing order.
* **Delete Order (Delete):** Permanently remove an order from the system and the persistent data file.
* **Data Persistence:** All orders are automatically saved to and loaded from the `laundry.txt` file.

---

## 🛠️ Technologies/Tools Used

* **Primary Language:** **Python 3.x**
* **Environment:** Command-Line Interface (CLI)
* **Data Storage:** Local Flat File (`laundry.txt`) using **CSV format**.

---

## 🚀 Steps to Install & Run the Project

### Prerequisites

* You must have **Python 3.x** installed on your system.

### Installation & Execution

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/samarthshukla20/laundry_mgmt
    cd laundry-mgmt
    ```

2.  **Save the Code:** Ensure the main program file, `laundry_mgmt.py`, is present in the directory.

3.  **Run the Application:**
    Execute the Python script directly from your terminal:
    ```bash
    python laundry_mgmt.py
    ```
4.  **Data File Creation:** The first time you run the application, it will automatically create the **`laundry.txt`** file in the same directory to store your orders.

---

## 🧪 Instructions for Testing

Follow these steps to test the core functionality of the system:

### 1. Test Adding an Order (Option 1)

1.  Choose **Option 1: Add Laundry Order**.
2.  Enter a unique **Roll Number** (e.g., `101`) and a **Student Name**.
3.  Select multiple items, such as `1` (Shirt) with quantity `3`, and `3` (Jeans/Pant) with quantity `1`.
4.  Type **`done`** to finalize. Verify that the **Total Cost** (e.g., Rs 50) is calculated and the success message appears.

### 2. Test Viewing Orders (Option 2)

1.  Choose **Option 2: View Laundry Orders**.
2.  Verify that the order you just added (Roll No. 101) appears correctly in the list.

### 3. Test Searching for an Order (Option 3)

1.  Choose **Option 3: Search for an Order**.
2.  Enter the Roll Number (`101`).
3.  Verify that the correct order details are displayed.

### 4. Test Updating an Order (Option 4)

1.  Choose **Option 4: Update Laundry Order**.
2.  Enter the Roll Number (`101`).
3.  Enter an updated name (e.g., "Alice Smith").
4.  Select a completely new set of items and quantities, then type **`done`**.
5.  Choose **Option 2: View Laundry Orders** again and verify that the name and cost for Roll No. 101 have been updated.

### 5. Test Deleting an Order (Option 5)

1.  Choose **Option 5: Delete Laundry Order**.
2.  Enter the Roll Number (`101`).
3.  Choose **Option 2: View Laundry Orders** and confirm that the order for Roll No. 101 is no longer listed.

## 🖼️ Screenshots / Repository View

This image provides a quick overview of the main repository structure and the application interface.

![GitHub Repository File View](images/code1.png)

![GitHub Repository File View](images/res1.png)

![GitHub Repository File View](images/res2.png)
---