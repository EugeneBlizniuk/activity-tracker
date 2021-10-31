create table category
(
    name            varchar(255) primary key,
    is_base_expense boolean,
    aliases         text
);

create table activity
(
    id                integer primary key,
    name              varchar(255),
    created           datetime,
    category_codename integer,
    FOREIGN KEY (category_codename) REFERENCES category (name)
);

insert into category (codename, name, is_base_expense, aliases)
values ("sport", true, "gym, swimming pool, spa, sauna, тренжерный зал, бассейн, баня, сауна"),
       ("food", true, "food, grocery, еда, продукты, вода"),
       ("transport", false, "taxi, subway, bus, trolleybus, такси, метро, автобус, троллейбус"),
       ("apartment", false,
        "apartment, house, home, utilities, internet, квартира, дом, коммунальные платежи, интернет"),
       ("subscription", false, "phone, spotify"),
       ("other", true, "");