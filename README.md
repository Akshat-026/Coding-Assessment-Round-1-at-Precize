# Coding-Assessment-Round-1-at-Precize
Coding Assessment Round 1 at Precize(Python file)
The provided Python script defines a simple program for managing and analyzing SAT (Scholastic Assessment Test) results for individuals. Here's an overview of the approach used in the script:

1. **Class Definitions:**
   - **`SATResults` Class:** Represents an individual's SAT results. It has attributes like `name`, `address`, `city`, `country`, `pincode`, `sat_score`, and `passed` (a status based on the SAT score).
   - **`SATResultsManager` Class:** Manages a list of `SATResults` objects. It includes methods for inserting data, viewing all data, getting ranks, updating scores, deleting records, and saving data to a JSON file.

2. **Approach to Data Handling:**
   - The script uses classes to encapsulate data related to SAT results and their management. The `SATResults` class defines the structure of an individual result, and the `SATResultsManager` class manages a collection of these results.

3. **Data Validation and Processing:**
   - The script performs basic data validation. For example, it checks whether a student has passed or failed based on a threshold of 30% of the maximum SAT score.
   - The program allows users to insert, view, update, and delete SAT results. It also provides a method to retrieve the rank of a student based on their SAT score.

4. **User Interaction:**
   - The `SATResultsManager` class includes methods for user input to gather information such as name, address, SAT score, etc.
   - The main loop in the `main()` function presents a menu to the user, allowing them to choose various operations like inserting data, viewing data, getting ranks, updating scores, deleting records, and saving data to a file.

5. **File Handling:**
   - The script uses the `json` module to serialize and deserialize data. It includes a method (`save_to_file`) to save the SAT results to a JSON file.

6. **Menu-Driven Interface:**
   - The main loop in the `main()` function provides a simple text-based menu for users to interact with the program. Users can choose different options by entering a corresponding number.

7. **Modularity and Readability:**
   - The script is organized into functions and classes, promoting modularity and readability. Each method in the `SATResultsManager` class performs a specific task, contributing to the overall functionality of the program.

Overall, the approach focuses on creating a modular, user-friendly program for managing SAT results with basic data validation and persistent storage through JSON files.
