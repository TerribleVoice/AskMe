CREATE TABLE public.users
(
    id         uuid    NOT NULL,
    login      varchar NOT NULL,
    email      varchar NULL,
    "password" varchar NOT NULL,
    is_autor   bool    NOT NULL,
    CONSTRAINT users_pk PRIMARY KEY (id)
);
