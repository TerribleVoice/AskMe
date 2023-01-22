CREATE TABLE public.users
(
    id         uuid    NOT NULL,
    login      varchar NOT NULL,
    email      varchar NULL,
    "password" varchar NOT NULL,
    is_author   bool    NOT NULL,
    CONSTRAINT users_pk PRIMARY KEY (id)
);

CREATE TABLE public.posts (
    id uuid NOT NULL,
    author_id uuid NOT NULL,
    subscription_id uuid NOT NULL,
    content text NOT NULL,
    created_at timestamp without time zone NOT NULL,
    price integer
);

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_fk FOREIGN KEY (author_id) REFERENCES public.users(id) ON DELETE SET NULL;


INSERT INTO public.users (id,login,email,"password",is_author) VALUES
    ('a8681dd5-7a5a-4ae5-8237-583edfb2eedb','test','test@ya.ru','123',true),
    ('3560787e-4830-4fba-9673-9f47c9a3f8c8','reader','reader@ya.ru','123',false);

INSERT INTO public.posts (id,author_id,subscription_id,content,created_at,price) VALUES
    ('fbad2687-42f4-4cb3-8534-61c8936ec4a8','a8681dd5-7a5a-4ae5-8237-583edfb2eedb','4dcde46f-6f38-4400-bd1e-e495f148afdd','Всем привет, это первый пост автоматически сгенерированный при создании БД. Если вы его видите, то подключение к бд работает хорошо','2023-01-19 23:00:00+05',NULL);