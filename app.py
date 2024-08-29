import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

# Criar tabela de pacientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    genero TEXT,
    endereco TEXT,
    telefone TEXT,
    email TEXT,
    historico_medico TEXT
)
''')

# Função para adicionar um novo paciente
def adicionar_paciente(nome, idade, genero, endereco, telefone, email, historico_medico):
    cursor.execute('''
    INSERT INTO pacientes (nome, idade, genero, endereco, telefone, email, historico_medico)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nome, idade, genero, endereco, telefone, email, historico_medico))
    conn.commit()

# Função para listar todos os pacientes
def listar_pacientes():
    cursor.execute('SELECT * FROM pacientes')
    return cursor.fetchall()

# Função para buscar um paciente pelo ID
def buscar_paciente(id):
    cursor.execute('SELECT * FROM pacientes WHERE id = ?', (id,))
    return cursor.fetchone()

# Função para atualizar informações de um paciente
def atualizar_paciente(id, nome, idade, genero, endereco, telefone, email, historico_medico):
    cursor.execute('''
    UPDATE pacientes
    SET nome = ?, idade = ?, genero = ?, endereco = ?, telefone = ?, email = ?, historico_medico = ?
    WHERE id = ?
    ''', (nome, idade, genero, endereco, telefone, email, historico_medico, id))
    conn.commit()

# Função para deletar um paciente
def deletar_paciente(id):
    cursor.execute('DELETE FROM pacientes WHERE id = ?', (id,))
    conn.commit()

# Exemplo de uso
adicionar_paciente('João Silva', 30, 'Masculino', 'Rua A, 123', '123456789', 'joao@example.com', 'Histórico de asma')
pacientes = listar_pacientes()
print(pacientes)

# Fechar a conexão
conn.close()
