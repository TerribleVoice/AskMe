CREATE TABLE public.users
(
    id         uuid    NOT NULL,
    login      varchar NOT NULL,
    email      varchar NULL,
    "password" varchar NOT NULL,
    qiwi_token varchar NULL,
    "description" text NULL,
    links text NULL,
    CONSTRAINT users_pk PRIMARY KEY (id)
);

CREATE TABLE public.posts (
    id uuid NOT NULL,
    author_id uuid NOT NULL,
    subscription_id uuid NOT NULL,
    title varchar(300) NOT NULL,
    content text NOT NULL,
    created_at timestamp without time zone NOT NULL
);

CREATE TABLE public.tokens (
    author_id uuid NOT NULL,
    token varchar(500) NOT NULL
);

CREATE TABLE public.bills (
    bill_id uuid NOT NULL,
    sender varchar(30),
    receiver uuid NOT NULL,
    comment varchar(500),
    amount integer NOT NULL
);

CREATE TABLE public.subscriptions (
	id uuid NOT NULL,
	author_id uuid NOT NULL,
	price int NOT NULL,
	name varchar NOT NULL,
	description varchar NOT NULL,
	parent_subscription_id uuid NULL,
	CONSTRAINT subscriptions_pk PRIMARY KEY (id),
	CONSTRAINT subscriptions_fk FOREIGN KEY (author_id) REFERENCES public.users(id)
);

CREATE TABLE public.bought_subscriptions (
	id uuid NOT NULL,
	user_id uuid NOT NULL,
	subscription_id uuid NOT NULL,
	CONSTRAINT bought_subscriptions_pk PRIMARY KEY (id),
	CONSTRAINT bought_subscriptions_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE SET NULL,
	CONSTRAINT bought_subscriptions_fk_1 FOREIGN KEY (subscription_id) REFERENCES public.subscriptions(id)
);


ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_fk FOREIGN KEY (author_id) REFERENCES public.users(id) ON DELETE SET NULL;

ALTER TABLE ONLY public.tokens
    ADD CONSTRAINT tokens_fk FOREIGN KEY (author_id) REFERENCES public.users(id) ON DELETE CASCADE;

ALTER TABLE ONLY public.bills
    ADD CONSTRAINT bill_fk FOREIGN KEY (receiver) REFERENCES public.users(id) ON DELETE CASCADE;


INSERT INTO public.users (id,login,email,"password",qiwi_token) VALUES
    ('a8681dd5-7a5a-4ae5-8237-583edfb2eedb','test','test@ya.ru','123',NULL),
    ('3560787e-4830-4fba-9673-9f47c9a3f8c8','reader','reader@ya.ru','123',NULL);

INSERT INTO public.posts (id,author_id,subscription_id,title,content,created_at) VALUES
    ('fbad2687-42f4-4cb3-8534-61c8936ec4a8','a8681dd5-7a5a-4ae5-8237-583edfb2eedb','4dcde46f-6f38-4400-bd1e-e495f148afdd','Всем привет','Всем привет, это первый пост автоматически сгенерированный при создании БД. Если вы его видите, то подключение к бд работает хорошо','2023-01-19 23:00:00+05');
