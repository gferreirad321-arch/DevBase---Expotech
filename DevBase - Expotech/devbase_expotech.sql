USE devbase;


-- MySQL dump 10.13 Distrib 8.0.45, for Win64 (x86_64) -- -- Host: 127.0.0.1 Database: devbase_expotech -- ------------------------------------------------------ -- Server version 8.0.45 /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
-- -- Table structure for table tbl_acesso_diario 
DROP TABLE IF EXISTS tbl_acesso_diario;
CREATE TABLE tbl_acesso_diario ( id_acesso_diario int NOT NULL AUTO_INCREMENT, dt_acesso_acesso_diario datetime DEFAULT CURRENT_TIMESTAMP, pontuacao_dia_acesso_diario int NOT NULL DEFAULT '0', id_usuario int NOT NULL, PRIMARY KEY (id_acesso_diario), KEY id_usuario (id_usuario), CONSTRAINT tbl_acesso_diario_ibfk_1 FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id_usuario) ON DELETE CASCADE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_acesso_diario 
LOCK TABLES tbl_acesso_diario WRITE;
UNLOCK TABLES;
-- -- Table structure for table tbl_comentario 
DROP TABLE IF EXISTS tbl_comentario;
CREATE TABLE tbl_comentario ( id_comentario int NOT NULL AUTO_INCREMENT, texto_comentario text NOT NULL, dt_criacao_comentario datetime DEFAULT CURRENT_TIMESTAMP, id_usuario int NOT NULL, id_topico int NOT NULL, PRIMARY KEY (id_comentario), KEY id_topico (id_topico), KEY idx_comentario_usuario (id_usuario), CONSTRAINT tbl_comentario_ibfk_1 FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id_usuario) ON DELETE CASCADE, CONSTRAINT tbl_comentario_ibfk_2 FOREIGN KEY (id_topico) REFERENCES tbl_topico (id_topico) ON DELETE CASCADE ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_comentario 
LOCK TABLES tbl_comentario WRITE;
UNLOCK TABLES;
-- -- Table structure for table tbl_curtida 
DROP TABLE IF EXISTS tbl_curtida;
CREATE TABLE tbl_curtida ( id_curtida int NOT NULL AUTO_INCREMENT, id_usuario int NOT NULL, id_topico int DEFAULT NULL, id_comentario int DEFAULT NULL, PRIMARY KEY (id_curtida), UNIQUE KEY uq_usuario_topico (id_usuario,id_topico), UNIQUE KEY uq_usuario_comentario (id_usuario,id_comentario), UNIQUE KEY id_usuario (id_usuario,id_topico), UNIQUE KEY id_usuario_2 (id_usuario,id_comentario), KEY id_topico (id_topico), KEY id_comentario (id_comentario), CONSTRAINT tbl_curtida_ibfk_1 FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id_usuario) ON DELETE CASCADE, CONSTRAINT tbl_curtida_ibfk_2 FOREIGN KEY (id_topico) REFERENCES tbl_topico (id_topico) ON DELETE CASCADE, CONSTRAINT tbl_curtida_ibfk_3 FOREIGN KEY (id_comentario) REFERENCES tbl_comentario (id_comentario) ON DELETE CASCADE, CONSTRAINT chk_curtida CHECK ((((id_topico is not null) and (id_comentario is null)) or ((id_topico is null) and (id_comentario is not null)))) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_curtida 
LOCK TABLES tbl_curtida WRITE;
UNLOCK TABLES;
-- -- Table structure for table tbl_feedback 
DROP TABLE IF EXISTS tbl_feedback;
CREATE TABLE tbl_feedback ( id_feedback int NOT NULL AUTO_INCREMENT, msg_feedback text NOT NULL, dt_feedback datetime DEFAULT CURRENT_TIMESTAMP, id_usuario int NOT NULL, PRIMARY KEY (id_feedback), KEY id_usuario (id_usuario), CONSTRAINT tbl_feedback_ibfk_1 FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id_usuario) ON DELETE CASCADE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_feedback 
LOCK TABLES tbl_feedback WRITE;
UNLOCK TABLES;
-- -- Table structure for table tbl_notificacao 
DROP TABLE IF EXISTS tbl_notificacao;
CREATE TABLE tbl_notificacao ( id_notificacao int NOT NULL AUTO_INCREMENT, msg_notificacao text NOT NULL, lida_notificacao tinyint(1) DEFAULT '0', dt_notificacao datetime DEFAULT CURRENT_TIMESTAMP, id_usuario int NOT NULL, PRIMARY KEY (id_notificacao), KEY id_usuario (id_usuario), CONSTRAINT tbl_notificacao_ibfk_1 FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id_usuario) ON DELETE CASCADE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_notificacao 
LOCK TABLES tbl_notificacao WRITE;
UNLOCK TABLES;
-- -- Table structure for table tbl_perfil 
DROP TABLE IF EXISTS tbl_perfil;
CREATE TABLE tbl_perfil ( id_perfil int NOT NULL AUTO_INCREMENT, bio_perfil varchar(350) DEFAULT NULL, nivel_perfil varchar(20) DEFAULT NULL, area_interesse_perfil varchar(100) DEFAULT NULL, id_usuario int DEFAULT NULL, avatar_perfil varchar(255) DEFAULT NULL, PRIMARY KEY (id_perfil), UNIQUE KEY id_usuario (id_usuario), CONSTRAINT fk_perfil_usuario FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id_usuario) ON DELETE CASCADE, CONSTRAINT tbl_perfil_chk_1 CHECK ((nivel_perfil in (_utf8mb4'iniciante',_utf8mb4'intermediario',_utf8mb4'avancado'))) ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_perfil 
LOCK TABLES tbl_perfil WRITE;
INSERT INTO tbl_perfil VALUES (1,NULL,NULL,NULL,1,'avatar2');
UNLOCK TABLES;
-- -- Table structure for table tbl_projeto 
DROP TABLE IF EXISTS tbl_projeto;
CREATE TABLE tbl_projeto ( id_projeto int NOT NULL AUTO_INCREMENT, titulo_projeto varchar(150) NOT NULL, descricao_projeto text NOT NULL, link_projeto varchar(350) DEFAULT NULL, dt_criacao_projeto date DEFAULT (curdate()), id_usuario int NOT NULL, PRIMARY KEY (id_projeto), KEY id_usuario (id_usuario), CONSTRAINT tbl_projeto_ibfk_1 FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id_usuario) ON DELETE CASCADE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_projeto 
LOCK TABLES tbl_projeto WRITE;
UNLOCK TABLES;
-- -- Table structure for table tbl_recuperacao_senha 
DROP TABLE IF EXISTS tbl_recuperacao_senha;
CREATE TABLE tbl_recuperacao_senha ( id_recuperacao_senha int NOT NULL AUTO_INCREMENT, token_recuperacao_senha varchar(255) NOT NULL, expira_em_recuperacao_senha datetime NOT NULL DEFAULT ((now() + interval 1 hour)), usado_recuperacao_senha tinyint(1) DEFAULT '0', id_usuario int NOT NULL, PRIMARY KEY (id_recuperacao_senha), UNIQUE KEY token_recuperacao_senha (token_recuperacao_senha), KEY id_usuario (id_usuario), CONSTRAINT tbl_recuperacao_senha_ibfk_1 FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id_usuario) ON DELETE CASCADE ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_recuperacao_senha 
LOCK TABLES tbl_recuperacao_senha WRITE;
UNLOCK TABLES;
-- -- Table structure for table tbl_topico 
DROP TABLE IF EXISTS tbl_topico;
CREATE TABLE tbl_topico ( id_topico int NOT NULL AUTO_INCREMENT, titulo_topico varchar(150) NOT NULL, dt_criacao_topico datetime DEFAULT CURRENT_TIMESTAMP, tipo_topico enum('duvida','discussao','projeto','dica','aviso') NOT NULL, id_usuario int NOT NULL, PRIMARY KEY (id_topico), KEY id_usuario (id_usuario), CONSTRAINT tbl_topico_ibfk_1 FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id_usuario) ON DELETE CASCADE ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_topico 
LOCK TABLES tbl_topico WRITE;
INSERT INTO tbl_topico VALUES (1,'Como esse site pode me ajudar?','2026-04-29 19:41:27','duvida',1);
UNLOCK TABLES;
-- -- Table structure for table tbl_usuario 
DROP TABLE IF EXISTS tbl_usuario;
CREATE TABLE tbl_usuario ( id_usuario int NOT NULL AUTO_INCREMENT, nome_usuario varchar(150) NOT NULL, email_usuario varchar(200) NOT NULL, senha_usuario varchar(255) DEFAULT NULL, data_criacao_usuario datetime DEFAULT CURRENT_TIMESTAMP, ativo tinyint(1) DEFAULT '1', tipo_usuario enum('user','admin') NOT NULL DEFAULT 'user', dt_atualizacao datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, sexo_usuario enum('masculino','feminino') DEFAULT NULL, PRIMARY KEY (id_usuario), UNIQUE KEY email_usuario (email_usuario) ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
-- -- Dumping data for table tbl_usuario 
LOCK TABLES tbl_usuario WRITE;
INSERT INTO tbl_usuario VALUES (1,'Gabriel Ferreira Dias','gferreirad321@gmail.com','18040802','2026-04-29 19:20:13',1,'user',NULL,'masculino');
UNLOCK TABLES;
-- Dump completed on 2026-05-01 16:47:49


