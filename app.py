import streamlit as st
import numpy as np
import pandas as pd
import itertools
import math
import random

# Configure matplotlib for Streamlit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('default')

# Import plotly for interactive graphs
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Basic NetworkX for simple graph operations
try:
    import networkx as nx
    NETWORKX_AVAILABLE = True
except ImportError:
    NETWORKX_AVAILABLE = False
    st.warning("NetworkX not available - using basic graph functions")

# SymPy for symbolic math
try:
    import sympy as sp
    from sympy.logic.boolalg import BooleanTrue, BooleanFalse, And, Or, Not
    SYMPY_AVAILABLE = True
except ImportError:
    SYMPY_AVAILABLE = False
    st.warning("SymPy not available - using basic Boolean operations")

st.set_page_config(page_title="MathCraft | Discrete Structures", layout="wide")
st.title("🔗 MathCraft: Discrete Structures & Logic")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.selectbox("Choose a section:", [
    "📚 Introduction", 
    "🔗 Logic & Propositions", 
    "🎯 Truth Tables & Gates", 
    "🛠️ Physical Manipulatives", 
    "💻 Real-World Applications", 
    "📝 Problem Solving",
    "🌐 Graph Theory & Networks"
])

if section == "📚 Introduction":
    st.markdown("""
    ### 🔗 What are Discrete Structures?
    **Discrete structures** are mathematical structures that deal with distinct, separate values rather than continuous ranges. They form the foundation of computer science, digital logic, and modern technology!
    
    **Key Areas:**
    - **Propositional Logic**: True/false statements and logical operators
    - **Set Theory**: Collections of objects and their relationships
    - **Graph Theory**: Networks of connected nodes
    - **Boolean Algebra**: Mathematical foundation of digital circuits
    - **Combinatorics**: Counting and arrangement principles
    """)
    
    # Core concepts table
    st.markdown("""
    ### 📐 Fundamental Discrete Concepts
    | Concept | Description | Real-World Example | Applications |
    |---------|-------------|-------------------|--------------|
    | Propositions | Statements that are either true or false | "It is raining" | Computer logic, AI reasoning |
    | Sets | Collections of distinct objects | {students in class} | Database design, data analysis |
    | Graphs | Networks of connected vertices | Social networks, maps | Internet routing, GPS systems |
    | Boolean Functions | Functions with true/false outputs | AND, OR, NOT gates | Computer processors, circuits |
    | Relations | Connections between elements | "is friends with" | Social media, recommendation systems |
    """)
    
    # Visual demonstration of discrete vs continuous
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🔢 Discrete vs Continuous
        **Discrete Examples:**
        - Number of students: 1, 2, 3, 4...
        - Digital signals: 0 or 1
        - Network connections: connected or not
        - Truth values: true or false
        
        **Key Properties:**
        - Countable values
        - Distinct states
        - No values "in between"
        - Perfect for digital systems
        """)
    
    with col2:
        # Create visual comparison
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Discrete plot
        x_discrete = [1, 2, 3, 4, 5, 6]
        y_discrete = [2, 5, 3, 8, 6, 4]
        ax1.scatter(x_discrete, y_discrete, s=100, color='blue', label='Discrete Points')
        ax1.set_title('Discrete Data\n(Separate, Countable Values)')
        ax1.set_xlabel('Input')
        ax1.set_ylabel('Output')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Continuous plot
        x_continuous = np.linspace(0, 6, 100)
        y_continuous = 2 * np.sin(x_continuous) + 3
        ax2.plot(x_continuous, y_continuous, 'r-', linewidth=2, label='Continuous Function')
        ax2.set_title('Continuous Data\n(Smooth, Unbroken Values)')
        ax2.set_xlabel('Input')
        ax2.set_ylabel('Output')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        plt.tight_layout()
        st.pyplot(fig)

elif section == "🔗 Logic & Propositions":
    st.header("🔗 Propositional Logic & Logical Operators")
    
    st.markdown("""
    **Explore the building blocks of logical reasoning!**
    Propositions are statements that can be definitively classified as true or false.
    """)
    
    # Logic symbols reference
    with st.expander("📋 Logic Symbols Reference"):
        st.markdown("""
        | Symbol | Name | Meaning | Example |
        |--------|------|---------|---------|
        | ~ or ¬ | NOT (negation) | ~P means "not P" | If P = "it's raining", ~P = "it's not raining" |
        | ∨ | OR (disjunction) | P ∨ Q means "P or Q (or both)" | "I'll bring lunch ∨ dinner" |
        | ∧ | AND (conjunction) | P ∧ Q means "P and Q" | "It's sunny ∧ warm" |
        | → | IF...THEN (implication) | P → Q means "if P, then Q" | "If it rains → I'll bring umbrella" |
        | ↔ | IF AND ONLY IF (biconditional) | P ↔ Q means "P if and only if Q" | "You pass ↔ you score ≥ 70%" |
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Interactive Logic Builder")
        
        # Proposition inputs
        prop_p = st.text_input("Proposition P:", "It is raining")
        prop_q = st.text_input("Proposition Q:", "I carry an umbrella")
        
        # Truth value inputs
        st.markdown("**Set Truth Values:**")
        p_value = st.checkbox("P is true", key="p_val")
        q_value = st.checkbox("Q is true", key="q_val")
        
        # Calculate logical operations
        not_p = not p_value
        not_q = not q_value
        p_and_q = p_value and q_value
        p_or_q = p_value or q_value
        p_implies_q = (not p_value) or q_value  # ¬P ∨ Q
        p_iff_q = p_value == q_value
        
        st.markdown(f"""
        **Logical Operations Results:**
        - **P**: {prop_p} = {p_value}
        - **Q**: {prop_q} = {q_value}
        - **~P**: Not ({prop_p}) = {not_p}
        - **~Q**: Not ({prop_q}) = {not_q}
        - **P ∧ Q**: ({prop_p}) AND ({prop_q}) = {p_and_q}
        - **P ∨ Q**: ({prop_p}) OR ({prop_q}) = {p_or_q}
        - **P → Q**: If ({prop_p}) then ({prop_q}) = {p_implies_q}
        - **P ↔ Q**: ({prop_p}) if and only if ({prop_q}) = {p_iff_q}
        """)
    
    with col2:
        st.subheader("📊 Complete Truth Table")
        
        # Generate complete truth table
        truth_table_data = []
        for p, q in itertools.product([False, True], repeat=2):
            not_p = not p
            not_q = not q
            p_and_q = p and q
            p_or_q = p or q
            p_implies_q = (not p) or q
            p_iff_q = p == q
            
            truth_table_data.append({
                'P': p,
                'Q': q,
                '~P': not_p,
                '~Q': not_q,
                'P ∧ Q': p_and_q,
                'P ∨ Q': p_or_q,
                'P → Q': p_implies_q,
                'P ↔ Q': p_iff_q
            })
        
        df = pd.DataFrame(truth_table_data)
        
        # Display truth table with styling
        st.dataframe(df.style.applymap(lambda x: 'background-color: lightgreen' if x else 'background-color: lightcoral'), 
                    use_container_width=True)
        
        st.markdown("""
        **Truth Table Key:**
        - 🟢 Green = True
        - 🔴 Red = False
        """)
    
    # Logic puzzles section
    st.markdown("---")
    st.subheader("🧩 Logic Puzzles")
    
    puzzle_choice = st.selectbox("Choose a logic puzzle:", [
        "Knights and Knaves",
        "Boolean Satisfiability",
        "Logical Equivalence Challenge"
    ])
    
    if puzzle_choice == "Knights and Knaves":
        st.markdown("""
        **Knights and Knaves Puzzle:**
        
        On an island, Knights always tell the truth and Knaves always lie.
        You meet two people, A and B.
        
        **A says:** "B is a Knave"
        **B says:** "We are both Knaves"
        
        What are A and B?
        """)
        
        with st.expander("💡 Solution Process"):
            st.markdown("""
            **Let's analyze B's statement: "We are both Knaves"**
            
            **Case 1: If B is a Knight (truth-teller)**
            - Then B's statement "We are both Knaves" must be true
            - But this means B is a Knave, which contradicts our assumption
            - Therefore, B cannot be a Knight
            
            **Case 2: If B is a Knave (liar)**
            - Then B's statement "We are both Knaves" must be false
            - This means it's NOT true that both are Knaves
            - Since B IS a Knave, A must NOT be a Knave
            - Therefore, A is a Knight
            
            **Check A's statement: "B is a Knave"**
            - A is a Knight (truth-teller) and says "B is a Knave"
            - This statement is true (B is indeed a Knave)
            - Consistent! ✓
            
            **Answer: A is a Knight, B is a Knave**
            """)

elif section == "🎯 Truth Tables & Gates":
    st.header("🎯 Logic Gates & Digital Circuits")
    
    st.markdown("""
    **Discover how logical operations power digital technology!**
    Logic gates are the building blocks of all digital circuits and computers.
    """)
    
    # Interactive logic gate simulator
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🔧 Logic Gate Simulator")
        
        # Gate selection
        gate_type = st.selectbox("Select Logic Gate:", [
            "AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"
        ])
        
        # Input selection (NOT gate only needs one input)
        if gate_type == "NOT":
            input_a = st.checkbox("Input A", key="gate_a")
            input_b = None
            st.markdown("*NOT gate only requires one input*")
        else:
            input_a = st.checkbox("Input A", key="gate_a")
            input_b = st.checkbox("Input B", key="gate_b")
        
        # Calculate output
        if gate_type == "AND":
            output = input_a and input_b
        elif gate_type == "OR":
            output = input_a or input_b
        elif gate_type == "NOT":
            output = not input_a
        elif gate_type == "NAND":
            output = not (input_a and input_b)
        elif gate_type == "NOR":
            output = not (input_a or input_b)
        elif gate_type == "XOR":
            output = input_a != input_b
        elif gate_type == "XNOR":
            output = input_a == input_b
        
        # Display result
        output_color = "🟢" if output else "🔴"
        st.markdown(f"""
        **Gate Output:** {output_color} **{output}**
        
        **Current Configuration:**
        - Gate Type: {gate_type}
        - Input A: {"🟢 TRUE" if input_a else "🔴 FALSE"}
        {f"- Input B: {'🟢 TRUE' if input_b else '🔴 FALSE'}" if input_b is not None else ""}
        - Output: {"🟢 TRUE" if output else "🔴 FALSE"}
        """)
    
    with col2:
        # Logic gate truth table and visualization
        st.subheader(f"📊 {gate_type} Gate Analysis")
        
        # Generate truth table for selected gate
        if gate_type == "NOT":
            gate_data = []
            for a in [False, True]:
                out = not a
                gate_data.append({'A': a, 'Output': out})
            gate_df = pd.DataFrame(gate_data)
        else:
            gate_data = []
            for a, b in itertools.product([False, True], repeat=2):
                if gate_type == "AND":
                    out = a and b
                elif gate_type == "OR":
                    out = a or b
                elif gate_type == "NAND":
                    out = not (a and b)
                elif gate_type == "NOR":
                    out = not (a or b)
                elif gate_type == "XOR":
                    out = a != b
                elif gate_type == "XNOR":
                    out = a == b
                
                gate_data.append({'A': a, 'B': b, 'Output': out})
            gate_df = pd.DataFrame(gate_data)
        
        # Display styled truth table
        def highlight_cell(val):
            if isinstance(val, bool):
                return 'background-color: lightgreen; font-weight: bold' if val else 'background-color: lightcoral; font-weight: bold'
            return ''
        
        st.dataframe(gate_df.style.applymap(highlight_cell), use_container_width=True)
        
        # Logic gate applications
        if gate_type == "AND":
            st.markdown("""
            **AND Gate Applications:**
            - Security systems: Both keycard AND fingerprint required
            - Safety controls: Machine runs only if power ON AND safety switch engaged
            - Digital multiplication: Binary digit multiplication
            """)
        elif gate_type == "OR":
            st.markdown("""
            **OR Gate Applications:**
            - Alarm systems: Trigger if door opened OR window broken
            - Backup systems: Use primary power OR backup generator
            - Search engines: Find documents with term A OR term B
            """)
        elif gate_type == "XOR":
            st.markdown("""
            **XOR Gate Applications:**
            - Encryption: XOR operations in cryptographic algorithms
            - Error detection: Parity checking in data transmission
            - Toggle switches: Light switches in hallways
            """)
    
    # Circuit builder section
    st.markdown("---")
    st.subheader("🔧 Circuit Builder Challenge")
    
    challenge_type = st.selectbox("Choose a circuit challenge:", [
        "Home Security System",
        "Traffic Light Controller", 
        "Voting System"
    ])
    
    if challenge_type == "Home Security System":
        st.markdown("""
        **Design a Home Security System:**
        
        **Requirements:**
        - Alarm sounds if ANY door or window is opened
        - System can be disabled with master switch
        - Panic button always triggers alarm
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Set Input States:**")
            door = st.checkbox("Door opened (D)")
            window = st.checkbox("Window opened (W)")
            master = st.checkbox("Master switch ON (M)")
            panic = st.checkbox("Panic button pressed (P)")
        
        with col2:
            # Logic: Alarm = P OR ((D OR W) AND M)
            intrusion = door or window
            alarm = panic or (intrusion and master)
            
            st.markdown(f"""
            **Circuit Logic:**
            - Intrusion detected: D ∨ W = {intrusion}
            - System armed: M = {master}
            - Armed intrusion: (D ∨ W) ∧ M = {intrusion and master}
            - Panic override: P = {panic}
            - **Alarm output: P ∨ ((D ∨ W) ∧ M) = {alarm}**
            
            **Status:** {"🚨 ALARM!" if alarm else "✅ Secure"}
            """)

elif section == "🛠️ Physical Manipulatives":
    st.header("🛠️ Hands-On Activities & Physical Models")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔌 Circuit Boards", "🎲 Logic Games", "🃏 Set Theory Cards", "🕸️ Network Models"])
    
    with tab1:
        st.subheader("Electronic Circuit Building")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🔌 Physical Logic Gates:**
            1. **Breadboard circuits**: Build actual AND, OR, NOT gates
            2. **LED outputs**: Visual true/false indicators
            3. **Switch inputs**: Physical binary input controls
            4. **Logic IC chips**: 7400 series integrated circuits
            
            **🛠️ Required Materials:**
            - Breadboard and jumper wires
            - LEDs and resistors
            - Toggle switches
            - Logic gate IC chips (7408 AND, 7432 OR, 7404 NOT)
            - 9V battery and power supply
            """)
        
        with col2:
            st.markdown("""
            **🎯 Project Ideas:**
            
            **Beginner Level:**
            - Single logic gate testing
            - LED output indicators
            - Simple switch controls
            
            **Intermediate Level:**
            - Multi-gate combinations
            - Binary adder circuits
            - Decoder/encoder circuits
            
            **Advanced Level:**
            - Flip-flop memory circuits
            - Counter circuits
            - Simple calculator logic
            """)
    
    with tab2:
        st.subheader("Logic Reasoning Games")
        
        st.markdown("""
        **🎲 Boolean Algebra Games:**
        1. **Logic Dice**: Custom dice with T/F faces
        2. **Truth Table Bingo**: Complete tables to win
        3. **Circuit Cards**: Build logic circuits with cards
        4. **Boolean Battleship**: Use logic to find hidden ships
        
        **🏆 Competition Activities:**
        - Speed truth table completion
        - Logic gate identification challenges
        - Boolean simplification contests
        - Circuit design competitions
        """)
    
    with tab3:
        st.subheader("Set Theory Manipulatives")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎯 Physical Set Models:**
            1. **Venn Diagram Boards**: Moveable circles and objects
            2. **Color-Coded Objects**: Represent different sets
            3. **Sorting Trays**: Physical union/intersection activities
            4. **Magnetic Sets**: Classroom demonstration tools
            """)
        
        with col2:
            # Interactive Set Operations Demo
            st.markdown("**🔧 Set Operations Demo:**")
            
            set_a_input = st.text_input("Set A (comma-separated):", "1,2,3,4,5")
            set_b_input = st.text_input("Set B (comma-separated):", "4,5,6,7,8")
            
            try:
                set_a = set(item.strip() for item in set_a_input.split(',') if item.strip())
                set_b = set(item.strip() for item in set_b_input.split(',') if item.strip())
                
                union = set_a.union(set_b)
                intersection = set_a.intersection(set_b)
                diff_a_b = set_a.difference(set_b)
                diff_b_a = set_b.difference(set_a)
                
                st.markdown(f"""
                **Set Operations:**
                - **A**: {set_a}
                - **B**: {set_b}
                - **A ∪ B**: {union}
                - **A ∩ B**: {intersection}
                - **A - B**: {diff_a_b}
                - **B - A**: {diff_b_a}
                """)
            except:
                st.error("Please enter valid comma-separated values")
    
    with tab4:
        st.subheader("Graph Theory Networks")
        
        st.markdown("""
        **🕸️ Network Building:**
        1. **String and pins**: Create physical graphs
        2. **Social network mapping**: Student connections
        3. **Route planning**: Optimize paths and distances
        4. **Tree structures**: Hierarchical organizations
        
        **🎯 Graph Applications:**
        - Social Networks: Friendship connections
        - Infrastructure: Road networks and traffic flow
        - Internet topology and routing
        - Supply chain networks
        """)

elif section == "💻 Real-World Applications":
    st.header("💻 Real-World Applications of Discrete Structures")
    
    tab1, tab2, tab3, tab4 = st.tabs(["💻 Computer Science", "🔐 Cryptography", "📱 Digital Systems", "🌐 Networks"])
    
    with tab1:
        st.subheader("Computer Science Applications")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🖥️ Programming & Algorithms:**
            - Boolean expressions in if-then-else statements
            - Loop conditions: while loops and for loops
            - Data structures: Sets, trees, graphs
            - Database queries: SQL logic operations
            
            **🤖 Artificial Intelligence:**
            - Expert systems: Rule-based reasoning
            - Machine learning: Decision trees
            - Logic programming: Constraint satisfaction
            - Knowledge representation: Formal logic systems
            """)
        
        with col2:
            # Simple algorithm demonstration
            st.markdown("**🔧 Algorithm Logic Demo:**")
            
            numbers = st.text_input("Enter numbers (comma-separated):", "5,2,8,1,9")
            algorithm = st.selectbox("Choose algorithm:", ["Find Maximum", "Check Even/Odd", "Count Positives"])
            
            try:
                num_list = [int(x.strip()) for x in numbers.split(',') if x.strip()]
                
                if algorithm == "Find Maximum":
                    result = max(num_list) if num_list else None
                    st.write(f"Maximum value: {result}")
                    
                elif algorithm == "Check Even/Odd":
                    results = [(num, "Even" if num % 2 == 0 else "Odd") for num in num_list]
                    for num, parity in results:
                        st.write(f"{num}: {parity}")
                        
                elif algorithm == "Count Positives":
                    positive_count = sum(1 for num in num_list if num > 0)
                    st.write(f"Positive numbers: {positive_count}")
                    
            except ValueError:
                st.error("Please enter valid numbers")
    
    with tab2:
        st.subheader("Cryptography & Security")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🔐 XOR Encryption Demo:**
            
            XOR (Exclusive OR) is fundamental to many encryption methods.
            The key property: A ⊕ B ⊕ B = A
            """)
            
            message = st.text_input("Enter message to encrypt:", "HELLO")
            key = st.text_input("Enter encryption key:", "KEY")
            
            if message and key:
                # Simple XOR encryption
                encrypted_chars = []
                decrypted_chars = []
                
                for i, char in enumerate(message.upper()):
                    key_char = key[i % len(key)].upper()
                    # XOR the ASCII values
                    encrypted_val = ord(char) ^ ord(key_char)
                    encrypted_chars.append(chr(encrypted_val) if 32 <= encrypted_val <= 126 else f"[{encrypted_val}]")
                    # Decrypt by XORing again
                    decrypted_val = encrypted_val ^ ord(key_char)
                    decrypted_chars.append(chr(decrypted_val))
                
                encrypted_text = ''.join(encrypted_chars)
                decrypted_text = ''.join(decrypted_chars)
                
                st.markdown(f"""
                **Encryption Results:**
                - Original: {message.upper()}
                - Key: {key.upper()}
                - Encrypted: {encrypted_text}
                - Decrypted: {decrypted_text}
                """)
        
        with col2:
            st.markdown("""
            **🛡️ Security Applications:**
            - Access control: Boolean permission matrices
            - Authentication: Multi-factor logical verification
            - Network security: Firewall rule logic
            - Intrusion detection: Pattern matching algorithms
            
            **🔑 Cryptographic Methods:**
            - Block ciphers: Boolean function composition
            - Hash functions: One-way mathematical functions
            - Digital signatures: Mathematical proof of authenticity
            """)
    
    with tab3:
        st.subheader("Digital Systems & Hardware")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **⚡ Processor Design:**
            - ALU (Arithmetic Logic Unit): Boolean operations
            - Control units: State machines and logic
            - Memory systems: Address decoding logic
            - Cache design: Set-associative mapping
            """)
        
        with col2:
            # Binary calculator demo
            st.markdown("**🔢 Binary Calculator:**")
            
            calc_op = st.selectbox("Select operation:", ["AND", "OR", "XOR", "Addition"])
            bin_a = st.text_input("Binary number A:", "1010")
            bin_b = st.text_input("Binary number B:", "1100")
            
            try:
                # Convert to integers
                int_a = int(bin_a, 2)
                int_b = int(bin_b, 2)
                
                if calc_op == "AND":
                    result = int_a & int_b
                elif calc_op == "OR":
                    result = int_a | int_b
                elif calc_op == "XOR":
                    result = int_a ^ int_b
                elif calc_op == "Addition":
                    result = int_a + int_b
                
                result_bin = bin(result)[2:]  # Remove '0b' prefix
                
                st.markdown(f"""
                **Binary Calculation:**
                - A = {bin_a} (decimal: {int_a})
                - B = {bin_b} (decimal: {int_b})
                - A {calc_op} B = {result_bin} (decimal: {result})
                """)
                
            except ValueError:
                st.error("Please enter valid binary numbers (0s and 1s only)")
    
    with tab4:
        st.subheader("Networks & Communication")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🌐 Network Applications:**
            - Internet routing: Graph algorithms for packet delivery
            - DNS systems: Hierarchical tree structures
            - Load balancing: Graph theory for traffic distribution
            - Social networks: Friendship and influence mapping
            """)
        
        with col2:
            # Simple network analysis
            st.markdown("**🔗 Network Connectivity Analysis:**")
            
            nodes = st.slider("Number of nodes:", 3, 10, 5)
            connections = st.slider("Number of connections:", 2, 15, 7)
            
            # Simple network metrics
            max_connections = nodes * (nodes - 1) // 2
            connectivity_ratio = connections / max_connections if max_connections > 0 else 0
            
            # Estimate if network is connected
            min_for_connected = nodes - 1
            likely_connected = connections >= min_for_connected
            
            st.markdown(f"""
            **Network Analysis:**
            - Nodes: {nodes}
            - Edges: {connections}
            - Maximum possible edges: {max_connections}
            - Connectivity ratio: {connectivity_ratio:.2%}
            - Likely connected: {"✅ Yes" if likely_connected else "❌ Probably not"}
            """)

elif section == "📝 Problem Solving":
    st.header("📝 Real-World Problem Solving")
    
    problem_type = st.selectbox("Choose a problem category:", [
        "🏢 Database Design", 
        "🚦 Smart City Systems", 
        "🎮 Game Logic"
    ])
    
    if problem_type == "🏢 Database Design":
        st.subheader("Database Design with Set Theory")
        
        st.markdown("""
        **Problem:** Design a student enrollment system using set theory principles.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            # Sample data for demonstration
            students = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
            courses = {"Math 101", "Physics 201", "Computer Science 301", "Chemistry 101"}
            
            # Sample enrollments
            enrollments = {
                'Math 101': {'Alice', 'Bob', 'Charlie'},
                'Physics 201': {'Alice', 'Diana'},
                'Computer Science 301': {'Bob', 'Eve'},
                'Chemistry 101': {'Charlie', 'Diana', 'Eve'}
            }
            
            st.markdown("**Sample Data:**")
            st.write("Students:", students)
            st.write("Courses:", courses)
            
            for course, enrolled in enrollments.items():
                st.write(f"{course}: {enrolled}")
        
        with col2:
            # Set operations analysis
            math_students = enrollments['Math 101']
            physics_students = enrollments['Physics 201']
            
            union = math_students.union(physics_students)
            intersection = math_students.intersection(physics_students)
            difference =
