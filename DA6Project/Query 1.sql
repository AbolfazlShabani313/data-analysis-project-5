SELECT
    actor.actor_id,
    actor.first_name,
    actor.last_name,
    count(film_category.category_id),
    category.name
FROM
    actor
    left join film_actor on film_actor.actor_id =  actor.actor_id
    left join film on film.film_id = film_actor.film_id
    left join film_category on film.film_id = film_category.film_id
    left join category on film_category.category_id = category.category_id

group by actor.actor_id, actor.first_name, actor.last_name, category.name