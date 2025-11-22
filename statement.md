## 📝 Project Statement: Laundry Management System (LMS)

---

### 1. 🎯 Problem Statement

Student hostels, residential colleges, and small-scale laundry service providers often manage orders using **manual, paper-based, or non-integrated systems**. This archaic method results in several critical operational failures:

1.  **High Error Rate:** Manual recording and calculation of charges for diverse items (shirts, jeans, etc.) are prone to human errors, leading to incorrect billing and inventory discrepancies.
2.  **Inefficient Retrieval:** Searching for a specific student's order or tracking historical charges is time-consuming and cumbersome, resulting in poor customer service and operational delays.
3.  **Lack of Data Persistence/Integrity:** Paper records can be lost, damaged, or become illegible, leading to a complete loss of transactional history and accountability.

---

### 2. 🔭 Scope of the Project

The scope of this project is to develop a **simple, persistent, and reliable command-line interface (CLI) application** that fully digitizes the core laundry order workflow.

The system will focus exclusively on **order management and cost calculation** and will not include advanced features like inventory tracking, multi-user accounts, network integration, or graphical user interfaces (GUIs).

---

### 3. 👥 Target Users

The primary users of this system are:

* **Hostel Wardens/Administrators:** For managing resident laundry needs and ensuring correct billing.
* **Laundry Service Operators/Attendants:** Personnel responsible for accepting, processing, and delivering laundry orders.
* **Small Business Owners:** Individuals running small, independent laundry shops serving a regular, localized client base.

---

### 4. ✨ High-Level Features

The system implements essential CRUD (Create, Read, Update, Delete) functionality to manage laundry records:

| Feature | Description |
| :--- | :--- |
| **Add Order** | Allows for structured data entry (Roll No., Name) and **automated cost calculation** based on selected items and quantities. |
| **View Orders** | Displays a complete, organized list of all recorded orders. |
| **Search Order** | Enables quick lookup of any order using the unique **Roll Number**. |
| **Update Order** | Allows modification of client details and replacement of the item list/re-calculation of the total cost. |
| **Delete Order** | Permanently removes a specified order from the system. |
| **Data Persistence** | Automatically saves and loads all data from a local file (`laundry.txt`) between application sessions. |
