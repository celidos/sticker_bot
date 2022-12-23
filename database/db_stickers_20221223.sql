--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: stickers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stickers (
    sticker_id integer NOT NULL,
    descr text,
    file_id text,
    sticker_set_name text,
    file_unique_id text,
    __ts_vector__ tsvector GENERATED ALWAYS AS (to_tsvector('english'::regconfig, descr)) STORED
);


ALTER TABLE public.stickers OWNER TO postgres;

--
-- Data for Name: stickers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.stickers (sticker_id, descr, file_id, sticker_set_name, file_unique_id) FROM stdin;
1	press f to pay respect	CAACAgIAAxkBAAEbPkdjo9VPgobt6YMQs5jiI1sW-WIdtQACrwADTptkAoftMsdli6fnLAQ	FforRespect	AgADrwADTptkAg
2	умри	CAACAgQAAxkBAAEbPlJjo9a9VV_VUeT7tB9bMOBFH-vAswACAwEAAsr2HwAB1eghT_eKyHEsBA	neonoteka_by_fStikBot	AgADAwEAAsr2HwAB
3	die	CAACAgQAAxkBAAEbPlJjo9a9VV_VUeT7tB9bMOBFH-vAswACAwEAAsr2HwAB1eghT_eKyHEsBA	neonoteka_by_fStikBot	AgADAwEAAsr2HwAB
\.


--
-- Name: stickers stickers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stickers
    ADD CONSTRAINT stickers_pkey PRIMARY KEY (sticker_id);


--
-- Name: TABLE stickers; Type: ACL; Schema: public; Owner: postgres
--


--
-- PostgreSQL database dump complete
--

