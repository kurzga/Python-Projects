from graphviz import Digraph
dfa_dot = Digraph()

# NFA'nın durum kümelerine göre DFA'nın durumlarını tanımlıyoruz
dfa_states = {
    'q0': {'q0'},                      # Başlangıç durumu
    'q1': {'q0', 'q1'},                 # İlk 1 görüldüğünde
    'q2': {'q2'},                       # "11" kabul durumu
    'q3': {'q0', 'q3'},                 # İlk 1 (110 dizisi için) görüldüğünde
    'q4': {'q0', 'q4'},                 # 110 tamamlandığında
    'q5': {'q5'},                       # "110" kabul durumu
    'q6': {'q0', 'q6'},                 # İlk 1 (101 dizisi için) görüldüğünde
    'q7': {'q0', 'q7'},                 # 10 görüldüğünde
    'q8': {'q8'}                        # "101" kabul durumu
}

# DFA'daki durumları ve kabul durumlarını belirliyoruz
dfa_dot.node('q0', 'q0 (Start)', shape='circle')
dfa_dot.node('q2', 'q2 (Accept "11")', shape='doublecircle')
dfa_dot.node('q5', 'q5 (Accept "110")', shape='doublecircle')
dfa_dot.node('q8', 'q8 (Accept "101")', shape='doublecircle')

# DFA geçişleri
# DFA, deterministik olduğu için her durumdan belirli geçişler tanımlıyoruz
dfa_transitions = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q3', '1': 'q2'},
    'q3': {'0': 'q4', '1': 'q5'},
    'q4': {'0': 'q0', '1': 'q1'},
    'q5': {'0': 'q4', '1': 'q5'},
    'q6': {'0': 'q7', '1': 'q8'},
    'q7': {'0': 'q0', '1': 'q8'},
}

# DFA geçişlerini çiziyoruz
for state, transitions in dfa_transitions.items():
    for symbol, target in transitions.items():
        dfa_dot.edge(state, target, label=symbol)

dfa_dot.render('C:/Users/Dell/Desktop/dfa_diagram.png')