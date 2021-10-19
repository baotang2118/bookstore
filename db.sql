DROP TABLE discounts;
DROP TABLE reviews;
DROP TABLE order_items;
DROP TABLE books;
DROP TABLE authors;
DROP TABLE orders;
DROP TABLE categories;
DROP TYPE star;

CREATE TABLE categories
(
id bigint PRIMARY KEY,
category_name varchar(120),
category_desc varchar(255)
);

CREATE TABLE authors
(
id bigint PRIMARY KEY,
author_name text,
author_bio text
);

CREATE TABLE orders
(
id bigint PRIMARY KEY,
order_date timestamp,
order_amount decimal(8,2) CHECK (order_amount > 0)
);

CREATE TABLE books
(
id bigint PRIMARY KEY,
category_id bigint CHECK (category_id > 0),
author_id bigint CHECK (author_id > 0),
book_title text,
book_summary text,
book_price  decimal(5,2) CHECK (book_price > 0),
book_cover_photo varchar(20),
    FOREIGN KEY (category_id)
        REFERENCES categories (id),
    FOREIGN KEY (author_id)
        REFERENCES authors (id)
);

CREATE TYPE star AS ENUM ('1','2','3','4','5');

CREATE TABLE reviews
(
id bigint PRIMARY KEY,
book_id bigint CHECK (book_id > 0),
review_title varchar(120),
review_details text,
review_date timestamp,
rating_star star,
    FOREIGN KEY (book_id)
        REFERENCES books (id)
);

CREATE TABLE discounts
(
id bigint PRIMARY KEY,
book_id bigint  CHECK (book_id > 0),
discounts_start_date date,
discounts_end_date date,
discount_price decimal(5,2) CHECK (discount_price > 0),
    FOREIGN KEY (book_id)
        REFERENCES books (id)
);

CREATE TABLE order_items
(
id bigint PRIMARY KEY,
order_id bigint CHECK (order_id > 0),
book_id bigint CHECK (book_id > 0),
quantity smallint CHECK (quantity > 0),
price decimal(5,2) CHECK (price > 0),
    FOREIGN KEY (order_id)
        REFERENCES orders (id),
    FOREIGN KEY (book_id)
        REFERENCES books (id)
);

INSERT INTO categories(id, category_name, category_desc)
VALUES (1, 'Categories #1', 'Category description 1');

INSERT INTO categories(id, category_name, category_desc)
VALUES (2, 'Categories #2', 'Category description 2');

INSERT INTO categories(id, category_name, category_desc)
VALUES (3, 'Categories #3', 'Category description 3');

INSERT INTO authors(id, author_name, author_bio)
VALUES ('1', 'Author name 1', 'Author bio 1');

INSERT INTO authors(id, author_name, author_bio)
VALUES ('2', 'Author name 2', 'Author bio 2');

INSERT INTO authors(id, author_name, author_bio)
VALUES ('3', 'Author name 3', 'Author bio 3');

INSERT INTO orders(id, order_date, order_amount)
VALUES (1, '1/1/2021', 1);

INSERT INTO orders(id, order_date, order_amount)
VALUES (2, '1/1/2021', 2);

INSERT INTO orders(id, order_date, order_amount)
VALUES (3, '1/1/2021', 3);

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (1, 1, 1, 'book_title 1', 'book_summary 1', 2, 'book_cover_photo 1');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (2, 2, 2, 'book_title 2', 'book_summary 2', 3, 'book_cover_photo 2');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (3, 3, 3, 'book_title 3', 'book_summary 3', 5, 'book_cover_photo 3');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (4, 1, 1, 'book_title 4', 'book_summary 4', 7, 'book_cover_photo 4');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (5, 2, 2, 'book_title 5', 'book_summary 5', 11, 'book_cover_photo 5');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (6, 3, 3, 'book_title 6', 'book_summary 6', 13, 'book_cover_photo 6');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (7, 1, 1, 'book_title 7', 'book_summary 7', 17, 'book_cover_photo 7');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (8, 2, 2, 'book_title 8', 'book_summary 8', 19, 'book_cover_photo 8');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (9, 3, 3, 'book_title 9', 'book_summary 9', 23, 'book_cover_photo 9');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (10, 1, 1, 'book_title 10', 'book_summary 10', 27, 'book_cover_photo 10');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (11, 2, 2, 'book_title 11', 'book_summary 11', 31, 'book_cover_photo 11');

INSERT INTO books(id, category_id, author_id, book_title, book_summary, book_price, book_cover_photo)
VALUES (12, 3, 3, 'book_title 12', 'book_summary 12', 37, 'book_cover_photo 12');

INSERT INTO reviews(id, book_id, review_title, review_details, review_date, rating_star)
VALUES (1, 1, 'review title 1', 'review_details 1', '1/1/2021', '2');

INSERT INTO reviews(id, book_id, review_title, review_details, review_date, rating_star)
VALUES (2, 1, 'review title 2', 'review_details 2', '2/1/2021', '3');

INSERT INTO reviews(id, book_id, review_title, review_details, review_date, rating_star)
VALUES (3, 1, 'review title 3', 'review_details 3', '3/1/2021', '4');

INSERT INTO reviews(id, book_id, review_title, review_details, review_date, rating_star)
VALUES (4, 1, 'review title 4', 'review_details 4', '4/1/2021', '5');

INSERT INTO reviews(id, book_id, review_title, review_details, review_date, rating_star)
VALUES (5, 1, 'review title 5', 'review_details 5', '5/1/2021', '5');

INSERT INTO discounts(id, book_id, discounts_start_date, discounts_end_date, discount_price)
VALUES (1, 1, '1/1/2021', '1/11/2021', 1);

INSERT INTO discounts(id, book_id, discounts_start_date, discounts_end_date, discount_price)
VALUES (2, 2, '1/1/2021', '1/11/2021', 1);

INSERT INTO discounts(id, book_id, discounts_start_date, discounts_end_date, discount_price)
VALUES (3, 3, '1/1/2021', '1/11/2021', 1);

INSERT INTO order_items(id, order_id, book_id, quantity, price)
VALUES (1, 1, 1, 1, 5);

INSERT INTO order_items(id, order_id, book_id, quantity, price)
VALUES (2, 2, 1, 1, 5);

INSERT INTO order_items(id, order_id, book_id, quantity, price)
VALUES (3, 3, 1, 1, 5);