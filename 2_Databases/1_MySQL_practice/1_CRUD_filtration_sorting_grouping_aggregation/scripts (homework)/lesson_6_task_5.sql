-- Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети. Будем определять активность по кол-ву постов из таблицы posts

select concat(name, ' ', lastname) as name, id,
(select count(profile_id) from posts where profile_id = profiles.id) as count_of_posts
from profiles
order by count_of_posts limit 10;

/* как мы видим, определить 10 пользователей с наименьшей активностью по постам затруднительно, 
т.к. существует более 10 пользователей, которые не оставили не написали ни одного поста. Такая же ситуация наблюдается, например, в таблице messages */