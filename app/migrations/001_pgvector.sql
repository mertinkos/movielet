CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS items (
    id bigserial PRIMARY KEY,
    embedding vector(3)
);