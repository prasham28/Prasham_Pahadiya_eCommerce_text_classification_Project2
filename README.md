E-commerce Text Classification - Test Results

![image](https://github.com/user-attachments/assets/4aaf29f2-d8f2-43a0-b0cd-c97e9fbf973a)


Test Case Results with Screenshots

1. Electronics

Input:

python main.py "This smartphone has a great camera and long battery life."

Expected Output: Electronics




python main.py "Looking for a new laptop with an Intel i7 processor and 16GB RAM."

Expected Output: Electronics



2. Household

Input:

python main.py "Need a vacuum cleaner with powerful suction for home cleaning."

Expected Output: Household



python main.py "This air purifier removes dust and allergens from the air."

Expected Output: Household



3. Books

Input:

python main.py "I want to read a mystery thriller novel this weekend."

Expected Output: Books



python main.py "Looking for a Python programming book for beginners."

Expected Output: Books



4. Clothing & Accessories

Input:

python main.py "Buying a leather jacket for winter fashion."

Expected Output: Clothing & Accessories



python main.py "Looking for a stylish wristwatch under $100."

Expected Output: Clothing & Accessories



Edge Cases

1. Ambiguous Input

Input:

python main.py "I need a good charger for my laptop."

Expected Output: Electronics (but could be misclassified)



2. Multi-category Input

Input:

python main.py "I bought a smartwatch and a pair of running shoes."

Expected Output: Electronics or Clothing & Accessories



3. Out-of-Scope Input

Input:

python main.py "What is the weather today?"

Expected Output: Unrecognized Category




Summary

The model performs well for clear category inputs but may struggle with ambiguous or multi-category data. Future improvements can include confidence thresholds and category overlap handling.
