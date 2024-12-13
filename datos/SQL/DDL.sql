CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY,
    rut INT,
    contrasena VARCHAR(60)
);

CREATE TABLE usuarios_api(
    id_usuario_api int,
    PRIMARY key (id_usuario_api));

CREATE TABLE POSTS(
    id INT PRIMARY KEY,
    user_id INT,
    title varchar(80),
    body varchar(100),
    FOREIGN KEY (user_id) REFERENCES usuario_api(id_usuario_api)
    );

CREATE TABLE COMMENTS(
    post_id INT,
    id INT,
    name VARCHAR(100),
    email VARCHAR(40),
    body VARCHAR(100),
);