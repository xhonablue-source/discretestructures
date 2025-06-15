if problem_type == "🏢 Database Design":
        st.subheader("Database Design with Set Theory")
        
        st.markdown("""
        **Problem:** Design a student enrollment system for a university.
        We need to track students, courses, and their relationships using set theory principles.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Define Your Sets:**")
            
            # Student set
            student_input = st.text_area("Students (one per line):", 
                                       "Alice\nBob\nCharlie\nDiana\nEve")
            students = set(line.strip() for line in student_input.split('\n') if line.strip())
            
            # Course set
            course_input = st.text_area("Courses (one per line):", 
                                      "Math 101\nPhysics 201\nComputer Science 301\nChemistry 101")
            courses = set(line.strip() for line in course_input.split('\n') if line.strip())
            
            # Prerequisites (example of relations)
            st.markdown("**Course Prerequisites:**")
            prereq_course = st.selectbox("Course:", list(courses), key="prereq_course")
            prereq_req = st.selectbox("Requires:", list(courses), key="prereq_req")
            
            if st.button("Add Prerequisite"):
                if 'prerequisites' not in st.session_state:
                    st.session_state.prerequisites = set()
                st.session_state.prerequisites.add((prereq_course, prereq_req))
        
        with col2:
            st.markdown("**Enrollment Analysis:**")
            
            # Sample enrollments for demonstration
            enrollments = {
                'Math 101': {'Alice', 'Bob', 'Charlie'},
                'Physics 201': {'Alice', 'Diana'},
                'Computer Science 301': {'Bob', 'Eve'},
                'Chemistry 101': {'Charlie', 'Diana', 'Eve'}
            }
            
            # Set operations
            math_students = enrollments.get('Math 101', set())
            physics_students = enrollments.get('Physics 201', set())
            cs_students = enrollments.get('Computer Science 301', set())
            
            # Union: Students taking math OR physics
            math_or_physics = math_students.union(physics_students)
            
            # Intersection: Students taking BOTH math AND physics
            math_and_physics = math_students.intersection(physics_students)
            
            # Difference: Students in math but NOT in physics
            math_not_physics = math_students.difference(physics_students)
            
            st.markdown(f"""
            **Set Operations Results:**
            
            **Math 101 Students:** {math_students}
            **Physics 201 Students:** {physics_students}
            **CS 301 Students:** {cs_students}
            
            **Union (Math ∪ Physics):** {math_or_physics}
            *Students taking either Math OR Physics (or both)*
            
            **Intersection (Math ∩ Physics):** {math_and_physics}
            *Students taking BOTH Math AND Physics*
            
            **Difference (Math - Physics):** {math_not_physics}
            *Students in Math but NOT in Physics*
            
            **Analysis:**
            - Total unique students in Math/Physics: {len(math_or_physics)}
            - Students taking both courses: {len(math_and_physics)}
            - Math-only students: {len(math_not_physics)}
            """)
    
    elif problem_type == "🚦 Smart City Systems":
        st.subheader("Smart Traffic Light System")
        
        st.markdown("""
        **Problem:** Design a smart traffic light system that optimizes traffic flow
        based on real-time conditions using Boolean logic.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Traffic Sensors (Inputs):**")
            
            # Traffic sensor inputs
            north_traffic = st.checkbox("Heavy traffic from North")
            south_traffic = st.checkbox("Heavy traffic from South")
            east_traffic = st.checkbox("Heavy traffic from East")
            west_traffic = st.checkbox("Heavy traffic from West")
            
            # Special conditions
            emergency_vehicle = st.checkbox("Emergency vehicle detected")
            pedestrian_crossing = st.checkbox("Pedestrian crossing request")
            rush_hour = st.checkbox("Rush hour period")
            
            st.markdown("**System Configuration:**")
            priority_mode = st.selectbox("Priority Mode:", [
                "Normal Operation",
                "Emergency Override", 
                "Pedestrian Priority",
                "Rush Hour Optimization"
            ])
        
        with col2:
            st.markdown("**Traffic Light Logic:**")
            
            # Main traffic flows
            ns_traffic = north_traffic or south_traffic  # North-South traffic
            ew_traffic = east_traffic or west_traffic    # East-West traffic
            
            # Emergency override logic
            if emergency_vehicle:
                # Emergency vehicles get immediate green
                ns_green = True
                ew_green = False
                explanation = "Emergency override: All traffic yields"
                
            elif pedestrian_crossing:
                # Pedestrian crossing takes priority
                ns_green = False
                ew_green = False
                explanation = "Pedestrian crossing: All traffic stops"
                
            elif rush_hour and priority_mode == "Rush Hour Optimization":
                # During rush hour, prioritize the busier direction
                if ns_traffic and not ew_traffic:
                    ns_green = True
                    ew_green = False
                    explanation = "Rush hour: Prioritizing North-South flow"
                elif ew_traffic and not ns_traffic:
                    ns_green = False
                    ew_green = True
                    explanation = "Rush hour: Prioritizing East-West flow"
                else:
                    # Default alternating pattern
                    ns_green = True
                    ew_green = False
                    explanation = "Rush hour: Default North-South priority"
            else:
                # Normal operation - prioritize direction with more traffic
                if ns_traffic and not ew_traffic:
                    ns_green = True
                    ew_green = False
                    explanation = "Normal: North-South has priority"
                elif ew_traffic and not ns_traffic:
                    ns_green = False
                    ew_green = True
                    explanation = "Normal: East-West has priority"
                elif ns_traffic and ew_traffic:
                    # Both directions have traffic - use timer or default
                    ns_green = True
                    ew_green = False
                    explanation = "Both directions busy: Default North-South"
                else:
                    # No traffic detected
                    ns_green = False
                    ew_green = False
                    explanation = "No traffic: All red (standby mode)"
            
            # Display results
            ns_color = "🟢 GREEN" if ns_green else "🔴 RED"
            ew_color = "🟢 GREEN" if ew_green else "🔴 RED"
            
            st.markdown(f"""
            **Traffic Light Status:**
            - **North-South:** {ns_color}
            - **East-West:** {ew_color}
            
            **Logic Explanation:** {explanation}
            
            **Boolean Expression:**
            ```
            Emergency = {emergency_vehicle}
            Pedestrian = {pedestrian_crossing}
            NS_Traffic = {ns_traffic}
            EW_Traffic = {ew_traffic}
            
            NS_Green = Emergency ∨ (¬Pedestrian ∧ (NS_Traffic ∨ ¬EW_Traffic))
            EW_Green = ¬Emergency ∧ ¬Pedestrian ∧ EW_Traffic ∧ ¬NS_Traffic
            ```
            
            **System Benefits:**
            - Reduced wait times
            - Emergency vehicle priority
            - Pedestrian safety
            - Traffic flow optimization
            """)
    
    elif problem_type == "🎮 Game Logic":
        st.subheader("Video Game AI Decision Making")
        
        st.markdown("""
        **Problem:** Create an AI system for a strategy game character that makes decisions
        based on multiple game conditions using logical operators.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Game State (Inputs):**")
            
            # Player status
            health_low = st.checkbox("Health below 30%", key="health")
            mana_low = st.checkbox("Mana below 20%", key="mana")
            
            # Environment
            enemy_nearby = st.checkbox("Enemy within attack range", key="enemy")
            allies_nearby = st.checkbox("Allies within support range", key="allies")
            
            # Resources
            healing_potion = st.checkbox("Healing potion available", key="potion")
            powerful_spell = st.checkbox("Powerful spell available", key="spell")
            
            # Objectives
            objective_complete = st.checkbox("Primary objective complete", key="objective")
            treasure_nearby = st.checkbox("Treasure chest nearby", key="treasure")
            
            st.markdown("**AI Personality:**")
            ai_type = st.selectbox("AI Character Type:", [
                "Aggressive Fighter",
                "Defensive Support", 
                "Balanced Explorer",
                "Treasure Hunter"
            ])
        
        with col2:
            st.markdown("**AI Decision Logic:**")
            
            # Decision tree based on game state
            decisions = []
            
            # Critical health decision
            if health_low and healing_potion:
                decisions.append(("HEAL", "Critical health detected", "🏥"))
                primary_action = "HEAL"
                
            # Combat decisions
            elif enemy_nearby and not health_low:
                if powerful_spell and not mana_low:
                    decisions.append(("CAST_SPELL", "Enemy in range, spell available", "⚡"))
                    primary_action = "CAST_SPELL"
                else:
                    decisions.append(("ATTACK", "Enemy in range, engage in combat", "⚔️"))
                    primary_action = "ATTACK"
                    
            # Support decisions
            elif allies_nearby and not enemy_nearby:
                if mana_low:
                    decisions.append(("REST", "Recovering mana near allies", "😴"))
                    primary_action = "REST"
                else:
                    decisions.append(("SUPPORT", "Buffing nearby allies", "🛡️"))
                    primary_action = "SUPPORT"
                    
            # Exploration decisions
            elif treasure_nearby and not enemy_nearby:
                decisions.append(("COLLECT", "Safe treasure collection", "💰"))
                primary_action = "COLLECT"
                
            elif objective_complete:
                decisions.append(("RETURN", "Mission complete, heading home", "🏠"))
                primary_action = "RETURN"
                
            else:
                decisions.append(("EXPLORE", "Searching for objectives", "🔍"))
                primary_action = "EXPLORE"
            
            # Secondary considerations
            if health_low and not healing_potion:
                decisions.append(("RETREAT", "Low health, seeking safety", "🏃"))
                
            if mana_low and not enemy_nearby:
                decisions.append(("MEDITATE", "Restoring mana reserves", "🧘"))
            
            # Display AI decision
            primary_emoji = decisions[0][2] if decisions else "❓"
            st.markdown(f"""
            **AI Decision: {primary_emoji} {primary_action}**
            
            **Decision Process:**
            """)
            
            for i, (action, reason, emoji) in enumerate(decisions):
                priority = "Primary" if i == 0 else "Secondary"
                st.markdown(f"- {emoji} **{action}** ({priority}): {reason}")
            
            # Boolean logic explanation
            st.markdown(f"""
            
            **Boolean Logic Tree:**
            ```
            IF (HealthLow ∧ HealingPotion) THEN HEAL
            ELSE IF (EnemyNear ∧ ¬HealthLow ∧ PowerfulSpell ∧ ¬ManaLow) THEN CAST_SPELL
            ELSE IF (EnemyNear ∧ ¬HealthLow) THEN ATTACK
            ELSE IF (AlliesNear ∧ ¬EnemyNear ∧ ManaLow) THEN REST
            ELSE IF (AlliesNear ∧ ¬EnemyNear) THEN SUPPORT
            ELSE IF (TreasureNear ∧ ¬EnemyNear) THEN COLLECT
            ELSE IF ObjectiveComplete THEN RETURN
            ELSE EXPLORE
            ```
            
            **Current State Evaluation:**
            - Health critical: {health_low}
            - Combat ready: {enemy_nearby and not health_low}
            - Support mode: {allies_nearby and not enemy_nearby}
            - Exploration safe: {not enemy_nearby and not health_low}
            """)

elif section == "🌐 Graph Theory & Networks":
    st.header("🌐 Graph Theory & Network Analysis")
    
    st.markdown("""
    **Explore the mathematics of networks and connections!**
    Graph theory studies relationships between objects and has countless real-world applications.
    """)
    
    # Graph theory basics
    with st.expander("📋 Graph Theory Fundamentals"):
        st.markdown("""
        **Key Concepts:**
        - **Vertex (Node)**: A point or object in the graph
        - **Edge**: A connection between two vertices
        - **Degree**: Number of edges connected to a vertex
        - **Path**: A sequence of vertices connected by edges
        - **Cycle**: A path that starts and ends at the same vertex
        - **Connected Graph**: Every vertex can reach every other vertex
        - **Tree**: A connected graph with no cycles
        - **Complete Graph**: Every vertex connects to every other vertex
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔧 Network Builder")
        
        # Network configuration
        num_nodes = st.slider("Number of nodes:", 3, 10, 5)
        network_type = st.selectbox("Network type:", [
            "Social Network",
            "Transportation System", 
            "Computer Network",
            "Food Web"
        ])
        
        # Generate sample connections based on network type
        if network_type == "Social Network":
            st.markdown("""
            **Modeling friendships and social connections:**
            - Nodes: People
            - Edges: Friendship relationships
            - Analysis: Social influence, community detection
            """)
            sample_connections = [(0, 1), (1, 2), (2, 3), (0, 3), (1, 4)]
            
        elif network_type == "Transportation System":
            st.markdown("""
            **Modeling roads, routes, and transportation:**
            - Nodes: Cities or intersections
            - Edges: Roads or flight routes
            - Analysis: Shortest paths, traffic optimization
            """)
            sample_connections = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 2)]
            
        elif network_type == "Computer Network":
            st.markdown("""
            **Modeling internet and communication systems:**
            - Nodes: Computers or routers
            - Edges: Network connections
            - Analysis: Bandwidth, redundancy, failure tolerance
            """)
            sample_connections = [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)]
            
        else:  # Food Web
            st.markdown("""
            **Modeling ecological relationships:**
            - Nodes: Species
            - Edges: Predator-prey relationships
            - Analysis: Ecosystem stability, keystone species
            """)
            sample_connections = [(0, 1), (1, 2), (0, 2), (2, 3), (1, 4)]
        
        # Display connections
        st.markdown(f"""
        **Network Properties:**
        - Nodes: {num_nodes}
        - Edges: {len(sample_connections)}
        - Average degree: {2 * len(sample_connections) / num_nodes:.1f}
        """)
    
    with col2:
        st.subheader("📊 Network Analysis")
        
        # Create simple adjacency matrix
        adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        for i, j in sample_connections:
            if i < num_nodes and j < num_nodes:
                adj_matrix[i][j] = 1
                adj_matrix[j][i] = 1  # Undirected graph
        
        # Convert to DataFrame for display
        matrix_df = pd.DataFrame(adj_matrix, 
                               columns=[f'Node {i}' for i in range(num_nodes)],
                               index=[f'Node {i}' for i in range(num_nodes)])
        
        st.markdown("**Adjacency Matrix:**")
        st.dataframe(matrix_df)
        
        # Calculate basic graph properties
        degrees = [sum(row) for row in adj_matrix]
        max_degree = max(degrees) if degrees else 0
        min_degree = min(degrees) if degrees else 0
        
        # Check if graph is connected (simplified check)
        total_edges = sum(sum(row) for row in adj_matrix) // 2
        min_edges_connected = num_nodes - 1
        likely_connected = total_edges >= min_edges_connected
        
        st.markdown(f"""
        **Graph Analysis:**
        - **Degree sequence**: {degrees}
        - **Maximum degree**: {max_degree}
        - **Minimum degree**: {min_degree}
        - **Total edges**: {total_edges}
        - **Likely connected**: {'✅ Yes' if likely_connected else '❌ No'}
        - **Graph density**: {total_edges / (num_nodes * (num_nodes - 1) / 2):.2%}
        """)
    
    # Pathfinding demonstration
    st.markdown("---")
    st.subheader("🗺️ Shortest Path Finder")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Route Planning Problem:**")
        
        # Sample city network
        cities = ['New York', 'Chicago', 'Denver', 'Los Angeles', 'Miami']
        distances = {
            ('New York', 'Chicago'): 790,
            ('New York', 'Miami'): 1090,
            ('Chicago', 'Denver'): 920,
            ('Chicago', 'Miami'): 1190,
            ('Denver', 'Los Angeles'): 830,
            ('Miami', 'Los Angeles'): 2340
        }
        
        start_city = st.selectbox("Start city:", cities)
        end_city = st.selectbox("Destination city:", cities)
        
        if start_city != end_city:
            # Simple path finding (for demonstration)
            direct_path = (start_city, end_city)
            reverse_path = (end_city, start_city)
            
            direct_distance = distances.get(direct_path) or distances.get(reverse_path)
            
            if direct_distance:
                st.markdown(f"""
                **Direct Route Found:**
                - Distance: {direct_distance} miles
                - Path: {start_city} → {end_city}
                """)
            else:
                # Find path through intermediate cities
                possible_paths = []
                for intermediate in cities:
                    if intermediate != start_city and intermediate != end_city:
                        dist1 = distances.get((start_city, intermediate)) or distances.get((intermediate, start_city))
                        dist2 = distances.get((intermediate, end_city)) or distances.get((end_city, intermediate))
                        
                        if dist1 and dist2:
                            total_dist = dist1 + dist2
                            possible_paths.append((total_dist, f"{start_city} → {intermediate} → {end_city}"))
                
                if possible_paths:
                    shortest = min(possible_paths)
                    st.markdown(f"""
                    **Shortest Route via Intermediate City:**
                    - Distance: {shortest[0]} miles
                    - Path: {shortest[1]}
                    """)
                else:
                    st.markdown("**No route found in current network.**")
    
    with col2:
        st.markdown("**Network Optimization Applications:**")
        
        optimization_type = st.selectbox("Choose optimization problem:", [
            "Traveling Salesman",
            "Network Flow",
            "Minimum Spanning Tree",
            "Graph Coloring"
        ])
        
        if optimization_type == "Traveling Salesman":
            st.markdown("""
            **Traveling Salesman Problem (TSP):**
            - **Goal**: Visit all cities exactly once and return to start
            - **Objective**: Minimize total travel distance
            - **Applications**: Delivery routes, circuit board drilling, DNA sequencing
            - **Complexity**: NP-hard problem (very difficult for large networks)
            
            **Example**: A delivery truck must visit all 5 cities and return home.
            The challenge is finding the shortest possible route.
            """)
            
        elif optimization_type == "Network Flow":
            st.markdown("""
            **Maximum Flow Problem:**
            - **Goal**: Find maximum flow from source to sink
            - **Applications**: Traffic systems, data networks, supply chains
            - **Algorithm**: Ford-Fulkerson method
            
            **Example**: Water distribution system - maximize water flow
            from reservoir to city while respecting pipe capacity limits.
            """)
            
        elif optimization_type == "Minimum Spanning Tree":
            st.markdown("""
            **Minimum Spanning Tree (MST):**
            - **Goal**: Connect all nodes with minimum total edge weight
            - **Applications**: Network design, clustering, circuit design
            - **Algorithms**: Kruskal's, Prim's algorithm
            
            **Example**: Design electrical grid connecting all cities
            with minimum total cable length.
            """)
            
        else:  # Graph Coloring
            st.markdown("""
            **Graph Coloring Problem:**
            - **Goal**: Color vertices so no adjacent vertices share colors
            - **Objective**: Use minimum number of colors
            - **Applications**: Scheduling, frequency assignment, register allocation
            
            **Example**: Class scheduling - no student can have
            conflicting classes at the same time.
            """)

# Educational Standards and Resources Section
st.markdown("---")
st.header("📋 Educational Standards & Cognitive Development")

# Common Core Standards breakdown
with st.expander("📚 Common Core Standards Alignment"):
    st.markdown("""
    ### High School Mathematics Standards:
    
    **A-CED (Creating Equations):**
    - A-CED.A.3: Represent constraints by systems of equations and inequalities
    - A-CED.A.4: Rearrange formulas to highlight a quantity of interest
    
    **F-BF (Building Functions):**
    - F-BF.A.1: Write a function that describes a relationship between two quantities
    - F-BF.B.3: Identify the effect of transformations on graphs of functions
    
    **S-CP (Conditional Probability and Rules of Probability):**
    - S-CP.A.1: Describe events as subsets and use set operations
    - S-CP.A.2: Understand independence and conditional probability
    
    **Mathematical Practices:**
    - MP1: Make sense of problems and persevere in solving them
    - MP2: Reason abstractly and quantitatively  
    - MP3: Construct viable arguments and critique reasoning of others
    - MP4: Model with mathematics
    - MP5: Use appropriate tools strategically
    - MP6: Attend to precision
    - MP7: Look for and make use of structure
    - MP8: Look for and express regularity in repeated reasoning
    
    ### Computer Science Standards (CSTA):
    
    **Algorithms and Programming:**
    - 3A-AP-09: Create algorithms that use variables, expressions, and control structures
    - 3A-AP-10: Use algorithms to solve problems and understand their limitations
    - 3A-AP-13: Create prototypes that use algorithms to solve computational problems
    
    **Data and Analysis:**
    - 3A-DA-09: Translate data between different representation formats
    - 3A-DA-10: Use data analysis tools and techniques
    - 3A-DA-11: Create interactive data visualizations
    
    **Computing Systems:**
    - 3A-CS-01: Explain how abstractions hide implementation details
    - 3A-CS-02: Compare and contrast levels of abstraction in computing systems
    """)

# Cognitive Abilities Development
with st.expander("🧠 Cognitive Abilities Development"):
    st.markdown("""
    ### Logical-Mathematical Intelligence:
    - **Deductive Reasoning**: Drawing valid conclusions from premises
    - **Inductive Reasoning**: Identifying patterns and making generalizations
    - **Boolean Logic**: Understanding truth values and logical operations
    - **Set Theory**: Organizing and categorizing information systematically
    
    ### Abstract Thinking:
    - **Symbolic Representation**: Using symbols to represent complex relationships
    - **Formal Logic**: Working with abstract logical systems
    - **Graph Abstraction**: Visualizing relationships as network structures
    - **Algorithmic Thinking**: Breaking problems into step-by-step procedures
    
    ### Problem-Solving Strategies:
    - **Systematic Analysis**: Methodical examination of complex problems
    - **Pattern Recognition**: Identifying recurring structures and relationships
    - **Optimization Thinking**: Finding best solutions under constraints
    - **Proof Construction**: Building logical arguments and verification
    
    ### Computational Thinking:
    - **Decomposition**: Breaking complex problems into manageable parts
    - **Abstraction**: Focusing on essential features while ignoring details
    - **Pattern Recognition**: Identifying similarities and regularities
    - **Algorithm Design**: Creating step-by-step solution procedures
    
    ### Critical Thinking Skills:
    - **Logic Evaluation**: Assessing validity of arguments and reasoning
    - **Truth Analysis**: Determining accuracy of statements and claims
    - **System Analysis**: Understanding how components interact in networks
    - **Decision Making**: Using logical criteria to choose between alternatives
    
    ### Spatial and Network Intelligence:
    - **Graph Visualization**: Understanding network structures and relationships
    - **Topological Thinking**: Reasoning about connectivity and spatial relationships
    - **Network Analysis**: Identifying key nodes, paths, and structures
    - **System Design**: Creating efficient and robust network architectures
    """)

# Educational Resource Links
with st.expander("🔗 Educational Resources & Practice"):
    st.markdown("""
    ### Khan Academy Resources:
    
    **Logic and Set Theory:**
    - [Introduction to Logic](https://www.khanacademy.org/computing/computer-science/algorithms/intro-to-algorithms/v/what-are-algorithms)
    - [Set Theory Basics](https://www.khanacademy.org/math/statistics-probability/probability-library/basic-set-ops/v/intersection-and-union-of-sets)
    - [Boolean Algebra](https://www.khanacademy.org/computing/computer-science/algorithms)
    - [Graph Theory Introduction](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/v/representing-graphs)
    
    **Computer Science Applications:**
    - [Algorithms and Data Structures](https://www.khanacademy.org/computing/computer-science/algorithms)
    - [Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography)
    - [Database Design](https://www.khanacademy.org/computing/intro-to-programming/programming/sql-basics/v/intro-to-sql)
    
    ### IXL Practice Modules:
    
    **Logic and Reasoning:**
    - [Logical Reasoning](https://www.ixl.com/math/grade-8/logical-reasoning)
    - [Set Operations](https://www.ixl.com/math/algebra-2/set-operations)
    - [Truth Tables](https://www.ixl.com/math/precalculus/truth-tables)
    
    **Discrete Mathematics:**
    - [Combinatorics](https://www.ixl.com/math/precalculus/permutations-and-combinations)
    - [Graph Theory](https://www.ixl.com/math/precalculus/graph-theory)
    - [Boolean Functions](https://www.ixl.com/math/algebra-2/evaluate-functions)
    
    ### The Organic Chemistry Tutor (YouTube):
    
    **Discrete Mathematics Videos:**
    - [Logic and Truth Tables](https://www.youtube.com/watch?v=qV_wAroC5M8) - Comprehensive introduction to propositional logic
    - [Set Theory Operations](https://www.youtube.com/watch?v=tyDKR4FG3Yw) - Union, intersection, and complement operations
    - [Boolean Algebra Simplification](https://www.youtube.com/watch?v=59BbncMjL8I) - Simplifying boolean expressions
    - [Graph Theory Basics](https://www.youtube.com/watch?v=LFKZLXVO-Dg) - Introduction to graphs and networks
    - [Combinatorics Problems](https://www.youtube.com/watch?v=iKy-d8y8sQ8) - Permutations and combinations
    
    **Computer Science Applications:**
    - [Digital Logic Design](https://www.youtube.com/watch?v=gI-qXk7XojA) - Logic gates and circuit design
    - [Algorithm Analysis](https://www.youtube.com/watch?v=__vX2sjlpXU) - Big O notation and complexity
    
    ### McGraw Hill Connect & ALEKS:
    
    **Textbook Resources:**
    - **McGraw Hill Discrete Mathematics**: Comprehensive coverage of all discrete math topics
    - **McGraw Hill Computer Science**: Programming and algorithmic thinking
    - **McGraw Hill Statistics**: Probability and combinatorics applications
    
    **ALEKS Modules:**
    - Logic and Set Theory
    - Boolean Algebra and Digital Logic
    - Graph Theory and Networks
    - Combinatorics and Counting
    - Discrete Probability
    
    **Connect Assignments:**
    - Interactive logic gate simulators
    - Truth table construction exercises
    - Graph theory problem sets
    - Set theory application problems
    
    ### Additional Educational Resources:
    
    **Technology Integration:**
    - **Logisim**: Digital logic circuit simulator
    - **Gephi**: Network analysis and visualization software
    - **Wolfram Alpha**: Discrete mathematics computations
    - **GraphOnline**: Interactive graph theory tools
    - **Truth Table Generator**: Online logic table creators
    
    **Programming Platforms:**
    - **Scratch**: Visual programming for logical thinking
    - **Python**: Discrete mathematics libraries (NetworkX, SymPy)
    - **R**: Statistical computing and graph analysis
    - **MATLAB**: Mathematical computation and visualization
    
    **Professional Development:**
    - **CSTA (Computer Science Teachers Association)**: Discrete math in CS education
    - **SIGCSE**: Computer science education research and practice
    - **Mathematical Association of America**: Discrete mathematics resources
    - **National Council of Teachers of Mathematics**: Logic and reasoning standards
    """)

# Assessment and Progress Tracking
with st.expander("📊 Assessment & Progress Tracking"):
    st.markdown("""
    ### Formative Assessment Strategies:
    - **Logic Puzzles**: Daily brain teasers and reasoning challenges
    - **Truth Table Quizzes**: Quick logical operation assessments
    - **Set Theory Sorting**: Physical and digital categorization activities
    - **Graph Drawing**: Network visualization and analysis exercises
    - **Boolean Simplification**: Algebraic manipulation practice
    
    
    ### Differentiation Strategies:
    - **Visual Learners**: Graph diagrams, Venn diagrams, logic gate symbols, network visualizations
    - **Kinesthetic Learners**: Physical logic gates, hands-on circuit building, network construction activities
    - **Analytical Learners**: Formal proofs, algebraic manipulations, algorithm analysis, complexity theory
    - **Creative Learners**: Game design projects, artistic network layouts, storytelling with logic puzzles
    - **English Language Learners**: Visual logic symbols, multilingual programming concepts, collaborative projects
    
    ### Technology-Enhanced Assessment:
    - **Logic Simulators**: Digital circuit testing and verification
    - **Graph Analysis Software**: Network metrics and visualization tools
    - **Programming Environments**: Algorithm implementation and testing
    - **Interactive Proof Systems**: Automated theorem proving and verification
    - **Virtual Reality Networks**: Immersive graph theory exploration
    
    ### Real-World Performance Metrics:
    - **Problem-Solving Efficiency**: Time to solve logical reasoning problems
    - **Circuit Design Accuracy**: Correctness of digital logic implementations
    - **Network Analysis Skills**: Ability to extract insights from complex networks
    - **Algorithm Development**: Quality and efficiency of computational solutions
    - **Transfer Learning**: Application of discrete math concepts to novel domains
    
    ### Progress Monitoring Tools:
    - **Logic Mastery Progression**: From basic operations to complex proofs
    - **Graph Theory Skill Development**: Network analysis and optimization abilities
    - **Computational Thinking Assessment**: Algorithm design and implementation skills
    - **Cross-Curricular Application**: Integration with computer science, physics, and engineering
    - **Portfolio Development**: Collection of projects demonstrating discrete math mastery
    """)

# Professional Development and Advanced Resources
with st.expander("👨‍🎓 Professional Development & Advanced Resources"):
    st.markdown("""
    ### Teacher Professional Development:
    
    **Organizations & Conferences:**
    - **CSTA Annual Conference**: Computer Science Teachers Association events and workshops
    - **SIGCSE Technical Symposium**: Computer science education research and teaching methods
    - **MAA MathFest**: Mathematical Association of America discrete mathematics sessions
    - **NCTM Conference**: Integrating discrete math with traditional mathematics curriculum
    - **IEEE Computer Society**: Professional development in digital systems and logic design
    
    **Graduate Programs & Specializations:**
    - **M.Ed. in Mathematics Education**: Discrete mathematics and computer science integration
    - **M.S. in Computer Science Education**: Computational thinking and algorithmic reasoning
    - **Educational Technology Programs**: Digital tools for mathematical reasoning
    - **STEM Education Certificates**: Interdisciplinary approaches to discrete mathematics
    
    **Research and Publications:**
    - **Journal of Educational Computing Research**: Technology integration in discrete math education
    - **Computers & Education**: Digital tools for logical reasoning and problem solving
    - **Mathematical Thinking and Learning**: Cognitive aspects of discrete mathematical reasoning
    - **Computer Science Education**: Pedagogical approaches to discrete structures
    
    ### Advanced Mathematical Connections:
    
    **Higher Mathematics Integration:**
    - **Abstract Algebra**: Group theory and algebraic structures
    - **Number Theory**: Prime numbers, modular arithmetic, and cryptographic applications
    - **Combinatorial Optimization**: Advanced algorithms and complexity theory
    - **Formal Methods**: Mathematical verification and proof systems
    
    **Computer Science Applications:**
    - **Artificial Intelligence**: Logic programming and knowledge representation
    - **Machine Learning**: Graph neural networks and discrete optimization
    - **Cryptography**: Advanced encryption methods and security protocols
    - **Database Theory**: Relational algebra and query optimization
    
    **Engineering Connections:**
    - **Digital Signal Processing**: Boolean functions and discrete transforms
    - **Control Systems**: State machines and discrete event systems
    - **VLSI Design**: Circuit optimization and hardware description languages
    - **Network Engineering**: Protocol design and network topology optimization
    
    ### Industry Partnerships and Applications:
    
    **Technology Companies:**
    - **Software Development**: Algorithm design and data structure implementation
    - **Cybersecurity Firms**: Cryptographic protocol development and analysis
    - **Telecommunications**: Network optimization and routing algorithms
    - **Social Media Platforms**: Graph analysis and recommendation systems
    
    **Research Institutions:**
    - **Academic Computer Science Departments**: Collaborative research opportunities
    - **National Laboratories**: Discrete mathematics in scientific computing
    - **Think Tanks**: Policy analysis using network theory and game theory
    - **Military Research**: Secure communications and strategic planning
    
    **Educational Technology:**
    - **EdTech Companies**: Development of discrete mathematics learning platforms
    - **Gaming Industry**: Educational game design incorporating logical reasoning
    - **Simulation Software**: Network modeling and discrete event simulation tools
    - **Assessment Companies**: Computerized testing for mathematical reasoning
    
    ### Emerging Trends and Technologies:
    
    **Artificial Intelligence Integration:**
    - **Automated Theorem Proving**: AI-assisted mathematical reasoning
    - **Intelligent Tutoring Systems**: Personalized discrete mathematics instruction
    - **Machine Learning Applications**: Pattern recognition in logical structures
    - **Natural Language Processing**: Automated analysis of mathematical proofs
    
    **Quantum Computing Connections:**
    - **Quantum Logic Gates**: Extension of classical boolean algebra
    - **Quantum Algorithms**: Discrete optimization in quantum systems
    - **Quantum Cryptography**: Advanced security protocols and key distribution
    - **Quantum Networks**: Graph theory in quantum communication systems
    
    **Data Science and Analytics:**
    - **Big Data Graph Analysis**: Social networks and recommendation systems
    - **Network Analytics**: Infrastructure optimization and failure analysis
    - **Discrete Optimization**: Resource allocation and scheduling problems
    - **Combinatorial Data Mining**: Pattern discovery in large datasets
    """)

st.markdown("---")
st.markdown("""
### 🎯 Learning Extensions:
- **Build Logic Circuits**: Create working digital systems using breadboards and logic chips
- **Network Analysis Projects**: Study real social networks, transportation systems, or biological networks
- **Programming Applications**: Implement discrete algorithms in Python, Java, or other languages
- **Cryptography Exploration**: Design and analyze simple encryption/decryption systems
- **Game Theory Applications**: Model strategic decision-making in competitive scenarios
- **Database Design**: Create relational databases using set theory and logical relationships

### 🔧 Advanced Project Ideas:
- **Smart Home Automation**: Design logic systems for automated household controls
- **Social Network Analysis**: Analyze friendship patterns and influence networks in school
- **Traffic Optimization**: Model and optimize traffic light systems for reduced congestion
- **Recommendation Systems**: Build simple algorithms for suggesting movies, books, or music
- **Cybersecurity Simulation**: Create secure communication protocols using cryptographic methods
- **Graph Algorithm Visualization**: Develop interactive tools for teaching shortest path and spanning tree algorithms

### 💻 Career Pathway Connections:
- **Software Engineering**: Algorithm design, data structures, and system architecture
- **Cybersecurity Specialist**: Cryptographic analysis and secure system design
- **Data Scientist**: Network analysis, pattern recognition, and optimization
- **Computer Systems Engineer**: Digital logic design and hardware-software integration
- **Operations Research Analyst**: Optimization problems and decision support systems
- **Game Developer**: Logic systems, AI behavior trees, and procedural generation

### 🌐 Cross-Curricular Integration:
- **Computer Science**: Programming, algorithms, and computational thinking
- **Engineering**: Digital systems, control theory, and optimization
- **Physics**: Boolean algebra in quantum mechanics and digital electronics
- **Biology**: Network analysis in ecological systems and neural networks
- **Economics**: Game theory, market analysis, and resource optimization
- **Social Studies**: Social network analysis and information propagation

*MathCraft modules are designed to meet rigorous academic standards while fostering deep conceptual understanding through hands-on exploration and real-world applications. This discrete structures module connects abstract mathematical concepts to concrete applications in technology, providing students with essential skills for the digital age.*
""")
    import streamlit as st
import numpy as np
import pandas as pd
import itertools

# Configure matplotlib for Streamlit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('default')

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
        
        # Style the dataframe
        def highlight_true(val):
            return 'background-color: lightgreen' if val else 'background-color: lightcoral'
        
        styled_df = df.style.applymap(highlight_true)
        st.dataframe(styled_df, use_container_width=True)
        
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
        
        # Style and display truth table
        def highlight_output(val):
            return 'background-color: lightgreen; font-weight: bold' if val else 'background-color: lightcoral; font-weight: bold'
        
        def highlight_inputs(val):
            return 'background-color: lightblue' if val else 'background-color: lightgray'
        
        styled_gate_df = gate_df.style.applymap(highlight_output, subset=['Output'])
        if gate_type != "NOT":
            styled_gate_df = styled_gate_df.applymap(highlight_inputs, subset=['A', 'B'])
        else:
            styled_gate_df = styled_gate_df.applymap(highlight_inputs, subset=['A'])
        
        st.dataframe(styled_gate_df, use_container_width=True)
        
        # Logic gate applications
        st.markdown(f"""
        **{gate_type} Gate Applications:**
        """)
        
        if gate_type == "AND":
            st.markdown("""
            - **Security systems**: Both keycard AND fingerprint required
            - **Safety controls**: Machine runs only if power ON AND safety switch engaged
            - **Digital multiplication**: Binary digit multiplication
            """)
        elif gate_type == "OR":
            st.markdown("""
            - **Alarm systems**: Trigger if door opened OR window broken
            - **Backup systems**: Use primary power OR backup generator
            - **Search engines**: Find documents with term A OR term B
            """)
        elif gate_type == "NOT":
            st.markdown("""
            - **Inverters**: Convert positive voltage to negative
            - **Signal processing**: Invert digital signals
            - **Logic circuits**: Create opposite conditions
            """)
        elif gate_type == "XOR":
            st.markdown("""
            - **Encryption**: XOR operations in cryptographic algorithms
            - **Error detection**: Parity checking in data transmission
            - **Toggle switches**: Light switches in hallways
            """)
    
    # Circuit builder section
    st.markdown("---")
    st.subheader("🔧 Circuit Builder Challenge")
    
    challenge_type = st.selectbox("Choose a circuit challenge:", [
        "Home Security System",
        "Traffic Light Controller", 
        "Voting System",
        "Calculator Logic"
    ])
    
    if challenge_type == "Home Security System":
        st.markdown("""
        **Design a Home Security System:**
        
        **Requirements:**
        - Alarm sounds if ANY door or window is opened
        - System can be disabled with master switch
        - Panic button always triggers alarm
        
        **Available inputs:**
        - Door sensor (D)
        - Window sensor (W)  
        - Master switch (M)
        - Panic button (P)
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
            
            st.markdown("""
            **📋 Activity Steps:**
            1. **Design**: Plan circuit on paper first
            2. **Build**: Connect components on breadboard
            3. **Test**: Try all input combinations
            4. **Verify**: Compare with truth table
            5. **Expand**: Combine gates for complex logic
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
            
            **🔍 Learning Objectives:**
            - Understand voltage = true/false
            - See logic gates in action
            - Connect theory to practice
            - Troubleshoot circuit problems
            """)
    
    with tab2:
        st.subheader("Logic Reasoning Games")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎲 Boolean Algebra Games:**
            1. **Logic Dice**: Custom dice with T/F faces
            2. **Truth Table Bingo**: Complete tables to win
            3. **Circuit Cards**: Build logic circuits with cards
            4. **Boolean Battleship**: Use logic to find hidden ships
            
            **🃏 Card-Based Activities:**
            - **Logic Poker**: Hands based on truth tables
            - **Boolean Bridge**: Partner logic reasoning
            - **Set Logic**: Find logical relationships
            - **Proof Construction**: Build valid arguments
            """)
        
        with col2:
            st.markdown("""
            **🏆 Competition Activities:**
            
            **Logic Races:**
            - Speed truth table completion
            - Logic gate identification challenges
            - Boolean simplification contests
            
            **Team Challenges:**
            - Circuit design competitions
            - Logic puzzle tournaments
            - Proof construction races
            
            **Assessment Games:**
            - Logic concept review games
            - Error detection challenges
            - Application scenario games
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
            
            **📦 DIY Materials:**
            - Colored geometric shapes
            - Hula hoops for large Venn diagrams
            - Index cards for element labels
            - Sticky notes for dynamic sets
            """)
        
        with col2:
            st.markdown("""
            **🔍 Investigation Activities:**
            
            **Set Operations:**
            - Physical union and intersection
            - Complement demonstration
            - Subset relationships
            - Disjoint set identification
            
            **Real-World Sets:**
            - Student characteristics (grade, sport, hobby)
            - Food categories and dietary restrictions
            - Technology preferences and usage
            - Academic subjects and career interests
            """)
    
    with tab4:
        st.subheader("Graph Theory Networks")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🕸️ Network Building:**
            1. **String and pins**: Create physical graphs
            2. **Social network mapping**: Student connections
            3. **Route planning**: Optimize paths and distances
            4. **Tree structures**: Hierarchical organizations
            
            **🎮 Interactive Models:**
            - **Human graphs**: Students as vertices, connections as edges
            - **Rope networks**: Physical network traversal
            - **Building layouts**: Floor plans as graphs
            - **Transportation maps**: Bus/subway networks
            """)
        
        with col2:
            st.markdown("""
            **🎯 Graph Applications:**
            
            **Social Networks:**
            - Friendship connections
            - Communication patterns
            - Influence mapping
            - Community detection
            
            **Infrastructure:**
            - Road networks and traffic flow
            - Internet topology
            - Power grid connections
            - Supply chain networks
            
            **Optimization:**
            - Shortest path problems
            - Network flow analysis
            - Spanning tree construction
            - Graph coloring applications
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
            - **Boolean expressions**: if-then-else statements
            - **Loop conditions**: while loops and for loops
            - **Data structures**: Sets, trees, graphs
            - **Database queries**: SQL logic operations
            
            **🤖 Artificial Intelligence:**
            - **Expert systems**: Rule-based reasoning
            - **Machine learning**: Decision trees
            - **Logic programming**: Prolog and constraint satisfaction
            - **Knowledge representation**: Formal logic systems
            """)
        
        with col2:
            st.markdown("""
            **📊 Software Engineering:**
            - **Requirements specification**: Formal logic
            - **Testing**: Logical test case generation
            - **Verification**: Proving program correctness
            - **Design patterns**: Graph-based architectures
            
            **🔍 Search & Optimization:**
            - **Search algorithms**: Graph traversal methods
            - **Optimization problems**: Combinatorial solutions
            - **Path finding**: GPS and routing algorithms
            - **Resource allocation**: Set cover and matching
            """)
    
    with tab2:
        st.subheader("Cryptography & Security")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🔐 Encryption Methods:**
            - **XOR encryption**: Bitwise exclusive OR operations
            - **Block ciphers**: Boolean function composition
            - **Hash functions**: One-way mathematical functions
            - **Digital signatures**: Mathematical proof of authenticity
            
            **🛡️ Security Protocols:**
            - **Access control**: Boolean permission matrices
            - **Authentication**: Multi-factor logical verification
            - **Network security**: Firewall rule logic
            - **Intrusion detection**: Pattern matching algorithms
            """)
        
        with col2:
            # Interactive XOR encryption demo
            st.markdown("**🔧 XOR Encryption Demo:**")
            
            message = st.text_input("Enter message to encrypt:", "HELLO")
            key = st.text_input("Enter encryption key:", "KEY")
            
            if message and key:
                # Simple XOR encryption
                encrypted = ""
                decrypted = ""
                
                for i, char in enumerate(message.upper()):
                    key_char = key[i % len(key)].upper()
                    # XOR the ASCII values
                    encrypted_val = ord(char) ^ ord(key_char)
                    encrypted += chr(encrypted_val) if 32 <= encrypted_val <= 126 else f"[{encrypted_val}]"
                    # Decrypt by XORing again
                    decrypted_val = encrypted_val ^ ord(key_char)
                    decrypted += chr(decrypted_val)
                
                st.markdown(f"""
                **Encryption Process:**
                - Original: {message.upper()}
                - Key: {key.upper()}
                - Encrypted: {encrypted}
                - Decrypted: {decrypted}
                
                **XOR Property:** A ⊕ B ⊕ B = A
                """)
    
    with tab3:
        st.subheader("Digital Systems & Hardware")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **⚡ Processor Design:**
            - **ALU (Arithmetic Logic Unit)**: Boolean operations
            - **Control units**: State machines and logic
            - **Memory systems**: Address decoding logic
            - **Cache design**: Set-associative mapping
            
            **📱 Digital Devices:**
            - **Smartphone logic**: Touch screen processing
            - **Digital cameras**: Image processing algorithms
            - **Gaming consoles**: Graphics and physics engines
            - **IoT devices**: Sensor data processing
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
            **🌐 Internet & Web:**
            - **Routing protocols**: Graph algorithms for packet delivery
            - **DNS systems**: Hierarchical tree structures
            - **Load balancing**: Graph theory for traffic distribution
            - **CDN networks**: Optimization and caching strategies
            
            **📡 Communication Networks:**
            - **Cell tower placement**: Graph coloring problems
            - **Satellite networks**: Constellation optimization
            - **Wireless protocols**: Boolean logic for error correction
            - **Network topology**: Redundancy and fault tolerance
            """)
        
        with col2:
            # Network analysis demo
            st.markdown("**🔗 Network Connectivity Analysis:**")
            
            nodes = st.slider("Number of nodes:", 3, 10, 5)
            connections = st.slider("Number of connections:", 2, 15, 7)
            
            # Simple network metrics
            max_connections = nodes * (nodes - 1) // 2
            connectivity_ratio = connections / max_connections
            
            # Estimate if network is connected (rough approximation)
            min_for_connected = nodes - 1
            likely_connected = connections >= min_for_connected
            
            st.markdown(f"""
            **Network Analysis:**
            - Nodes: {nodes}
            - Edges: {connections}
            - Maximum possible edges: {max_connections}
            - Connectivity ratio: {connectivity_ratio:.2%}
            - Minimum edges for connectivity: {min_for_connected}
            - Likely connected: {"✅ Yes" if likely_connected else "❌ Probably not"}
            
            **Applications:**
            - Social network analysis
            - Infrastructure planning
            - Communication reliability
            - Resource optimization
            """)

elif section == "📝 Problem Solving":
    st.header("📝 Real-World Problem Solving")
    
    problem_type = st.selectbox("Choose a problem category:", [
        "🏢 Database Design", 
        "🚦 Smart City Systems", 
        "🎮 Game Logic", 
        "📊 Data Analysis"
    ])
