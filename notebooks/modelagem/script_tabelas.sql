/* brModelo: */

CREATE TABLE filial (
    cod_filial INTEGER PRIMARY KEY,
    desc_filial VARCHAR
);

/* brModelo: */

CREATE TABLE brick (
    cod_brick INTEGER PRIMARY KEY,
    desc_brick VARCHAR
);

/* brModelo: */

CREATE TABLE dim_filial_brick (
    cod_brick INTEGER,
    cod_filial INTEGER,
    PRIMARY KEY (cod_filial, cod_brick)
);
 
ALTER TABLE dim_filial_brick ADD CONSTRAINT FK_dim_filial_brick_1
    FOREIGN KEY (cod_filial)
    REFERENCES filial (cod_filial);
 
ALTER TABLE dim_filial_brick ADD CONSTRAINT FK_dim_filial_brick_2
    FOREIGN KEY (cod_brick)
    REFERENCES brick (cod_brick);


/* brModelo: */



/* brModelo: */

CREATE TABLE produto (
    cod_produto_catarinense VARCHAR(20),
    desc_produto_catarinense VARCHAR(100),
    ean VARCHAR(20),
    id_produto VARCHAR(20) PRIMARY KEY,
    UNIQUE (cod_produto_catarinense, ean)
);



/* brModelo: */

CREATE TABLE fact_vendas_iqvia (
    val_concorrente_indep DECIMAL,
    val_concorrente_rede DECIMAL,
    val_marca_pp DECIMAL,
    fk_cod_brick INTEGER,
    fk_ean VARCHAR(20) UNIQUE,
    id_fact_vendas_iqvia INTEGER PRIMARY KEY,
    fk_cod_filial INTEGER
);

ALTER TABLE fact_vendas_iqvia ADD CONSTRAINT FK_fact_dim_filial_brick
    FOREIGN KEY (fk_cod_filial, fk_cod_brick)
    REFERENCES dim_filial_brick (cod_filial, cod_brick);

ALTER TABLE produto ADD CONSTRAINT UQ_produto_ean UNIQUE (ean);

ALTER TABLE fact_vendas_iqvia ADD CONSTRAINT FK_fact_produto_ean
    FOREIGN KEY (fk_ean)
    REFERENCES produto (ean);