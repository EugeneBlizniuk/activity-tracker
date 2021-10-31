create table category
(
    name             varchar(255) primary key,
    is_base_activity boolean,
    aliases          text
);

create table activity
(
    id            integer primary key,
    name          varchar(255),
    created       datetime,
    category_name integer,
    FOREIGN KEY (category_name) REFERENCES category (name)
);

insert into category (name, is_base_activity, aliases)
values ("sport", true, "gym, swimming pool, spa, sauna, тренжерный зал, бассейн, баня, сауна"),
       ("business", true, "investment, cryptocurrency, инвестирование, криптовалюта"),
       ("improvment", true, "java, angular, english"),
       ("work", false, "new-feature, bug-fix, meet-up, новый функционал, исправление бага, встреча"),
       ("other", true, "");