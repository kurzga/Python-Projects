from graphviz import Digraph

# NFA çizimi için Graphviz kullanıyoruz.
# Bu NFA, "11", "110", veya "101" ile biten dizileri kabul edecek şekilde tasarlanmıştır.

# Yeni bir yönlendirilmiş grafik oluşturuyoruz.
dot = Digraph()

# Durumları tanımlıyoruz
dot.attr(rankdir='LR')  # Left to right görünüm
dot.node('q0', 'q0 (Start)')
dot.node('q1', 'q1')
dot.node('q2', 'q2 (Accept for "11")')
dot.node('q3', 'q3')
dot.node('q4', 'q4')
dot.node('q5', 'q5 (Accept for "110")')
dot.node('q6', 'q6')
dot.node('q7', 'q7')
dot.node('q8', 'q8 (Accept for "101")')

# Geçişleri tanımlıyoruz
# "11" alt dizisi
dot.edge('q0', 'q1', label='1')
dot.edge('q1', 'q2', label='1')

# "110" alt dizisi
dot.edge('q0', 'q3', label='1')
dot.edge('q3', 'q4', label='1')
dot.edge('q4', 'q5', label='0')

# "101" alt dizisi
dot.edge('q0', 'q6', label='1')
dot.edge('q6', 'q7', label='0')
dot.edge('q7', 'q8', label='1')

# Grafiği çizdiriyoruz.
dot.render('C:/Users/Dell/Desktop/nfa_diagram.png')
