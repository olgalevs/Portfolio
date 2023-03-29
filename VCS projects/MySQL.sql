-- Visiems :)
-- 1. atvaizduoti visus miestus kurių country_id mažiau už 10.
select city from city
where country_id<10 ;

-- 2. atvaizduoti visus miestus, kurių šalis kanada.
select city from city
where country_id=(
select country_id from country where country="canada");

-- 3. kiek pinigų iš viso išleido customer kurio id = 7;
select sum(amount) as suma
from payment
where customer_id=7;

-- 4. koks customer id kurio vardas MICHEAL o pavardė FORMAN
select customer_id
from customer
where first_name="Micheal" and last_name="Forman";

-- 5. kuris aktorius (jo id) vaidino daugiausiai filmų?
select actor_id, count(actor_id) as film_qty
from film_actor
group by actor_id
order by film_qty desc
limit 1;


-- 6. Patikrinti ar VISI film lentelėje esantys pavadinimai ir aprašymai (title, description) atitinka pateiktus pavadinimus ir aprašymus film_text lentelėje?
-- film ir film_text
select film.film_id, film.title,
case 
when film.description=film_text.description then "True"
else "False"
end as result
from film
join film_text on film.film_id=film_text.film_id
having result="false"
order by result desc;


-- Papildomi dėl rekomendacijų :)
-- e1. kurios kategorijos filmuose daugiausiai nusifilmavo aktorius kurio id = 5?
select film_category.category_id, category.name, count(film_category.category_id) as qty
from film_actor
join film_category on film_actor.film_id=film_category.film_id
join category on category.category_id=film_category.category_id
where actor_id=5
group by film_category.category_id, category.name
order by qty desc
limit 1;

-- e2 kurių aktorių filmai sugeneravo daugiausiai pajamų nuomuojant filmus kiekviename nuomos punkte? atvaizduoti du įrašus.
-- pirmą stulpelį pavadinkite "parduotuve". pirmoje eilutėje bus žodis "pirma". antroje eilutėje "antra". Kiti stulpeliai:
-- aktoriaus id, vardas, pavardė, ir kiek pajamų sugeneduota nuomuojant filmus kuriuose šis vaidino.-- 
(select 
case 
when staff.store_id=1 then "pirma"
else "antra"
end as parduotuve,
actor.actor_id, actor.first_name, actor.last_name, sum(payment.amount) as total_amount
from actor
join film_actor on actor.actor_id=film_actor.actor_id
join inventory on film_actor.film_id=inventory.film_id
join Nuoma on inventory.inventory_id=Nuoma.inventory_id
join payment on Nuoma.rental_id=payment.rental_id
join staff on payment.staff_id=staff.store_id
where staff.store_id=1
group by parduotuve,actor.actor_id, actor.first_name, actor.last_name
order by parduotuve desc, total_amount desc
limit 1)

union

(select 
case 
when staff.store_id=1 then "pirma"
else "antra"
end as parduotuve,
actor.actor_id, actor.first_name, actor.last_name, sum(payment.amount) as total_amount
from actor
join film_actor on actor.actor_id=film_actor.actor_id
join inventory on film_actor.film_id=inventory.film_id
join Nuoma on inventory.inventory_id=Nuoma.inventory_id
join payment on Nuoma.rental_id=payment.rental_id
join staff on payment.staff_id=staff.store_id
where staff.store_id=2
group by parduotuve,actor.actor_id, actor.first_name, actor.last_name
order by parduotuve desc, total_amount desc
limit 1);
