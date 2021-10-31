create table category
(
    id               integer primary key,
    name             varchar(255),
    is_base_activity boolean,
    aliases          text
);

create table activity
(
    id          integer primary key,
    name        varchar(255),
    amount      int,
    created     datetime,
    category_id integer,
    raw_text    text,
    FOREIGN KEY (category_id) REFERENCES category (id)
);

insert into category (id, name, is_base_activity, aliases)
values (1, "sport", true, "gym, swimming pool, spa, sauna"),
       (2, "business", true, "investment, cryptocurrency"),
       (3, "improvment", true, "java, angular, english"),
       (4, "work", false, "new-feature, bug-fix, meet-up"),
       (5, "other", true, "");