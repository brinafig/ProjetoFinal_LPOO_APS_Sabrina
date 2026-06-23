

CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    matricula VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100)
);

CREATE TABLE professor(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    titulo VARCHAR(50)
);


CREATE TABLE disciplina(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    total_aulas INTEGER,
    professor_id INTEGER REFERENCES professor(id) ON DELETE SET NULL
);


CREATE TABLE matricula (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER REFERENCES aluno(id) ON DELETE CASCADE,
    disciplina_id INTEGER REFERENCES disciplina(id) ON DELETE CASCADE,
    presencas INTEGER DEFAULT 0,
    status VARCHAR(20)
);


CREATE TABLE avaliacao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    peso NUMERIC(5,2) NOT NULL,
    data VARCHAR(20),
    disciplina_id INTEGER REFERENCES disciplina(id) ON DELETE CASCADE
);


CREATE TABLE nota (
    id SERIAL PRIMARY KEY,
    valor NUMERIC(5,2) NOT NULL,
    avaliacao_id INTEGER REFERENCES avaliacao(id) ON DELETE CASCADE,
    matricula_id INTEGER REFERENCES matricula(id) ON DELETE CASCADE
);