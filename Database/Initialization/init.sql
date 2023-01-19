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
    contnet text NOT NULL,
    created_at timestamp with time zone NOT NULL,
    price integer
);

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_fk FOREIGN KEY (author_id) REFERENCES public.users(id) ON DELETE SET NULL;