# Minimization Algorithm

## Team
- Juan Manuel Gallo López
- David Garcia 
- Class code: 7309

## Development environment
- **Operative System:** Windows 11
- **Programming language:** Python 
- **Tools:** Visual Studio Code

## 🛠️ How to Run the Implementation
1. **Clone or download** this repository to your local machine.
2. **Open a terminal** (or command prompt) in the project’s folder.
3. **Place the input file** (e.g., `input.txt`) in the same directory as the code.
4. **Run the program** with the following command (example for Python):
   ```bash
   python minimize_dfa.py   input.txt
   
## 📂 Estructura del Proyecto
1. **minimizar_dfa.py** 
2. **input.txt**       
3. **README.md**         

---

## 📝 Explanation of the Algorithm
1. **Input Reading:**  
   The test cases are extracted, which include the number of states, the alphabet, the final states, and the transition table.

2. **Initialization of the Indistinguishability Table:**  
   A lower-triangular matrix is created where each cell represents a pair of states:
   - Each cell is initially marked with "0" (indistinguishable).
   - The diagonal is filled with the corresponding state number.
   - Pairs in which one state is final and the other is not are marked with "x" (since they are immediately distinguishable).

3. **Iterative Process:**  
   The matrix is traversed and, for each unmarked pair, it is checked whether, for any symbol in the alphabet, the transitions lead to a pair that is already marked. If so, the current pair is marked.

4. **Determination of Equivalent States:**  
   The pairs that remain unmarked are considered equivalent and are printed in lexicographical order.


## 🎯 Example Test Cases

### Case 1
- **Description:** DFA with 4 states (0, 1, 2, 3), alphabet `{a, b}`, and final states `{1, 3}`.
- **Input:**
1 4 a b 1 3 0 1 2 1 1 3 2 1 2 3 1 3

- **Expected Output:**  
(0,2) (1,3)

### Case 2
- **Description:** DFA with 5 states (0, 1, 2, 3, 4), alphabet `{a, b}`, and final states `{2, 4}`.
- **Input:**
1 5 a b 2 4 0 1 2 1 1 3 2 1 4 3 1 3 4 1 4

- **Expected Output:**  
(1,3) (2,4)





