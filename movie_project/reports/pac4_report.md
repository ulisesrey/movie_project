# Global report

In this project we worked on the Movie Database (TMDB) to get some insights about more than 159.000 tv shows.

In summary:
## 0. Uncompressing and reading the data
We have written code to uncompress and read the data from the TMBD.
## 1. Processing the data
We have seen the top shows with most days in air:
| id | name | days_on_air |
|:---:|:---:|:---:|
| 637 | CBS Evening News | 30043 days |
| 215684 | Neujahrskonzert der Wiener Philharmoniker | 29950 days |
| 71494 | Golden Globe Awards | 28845 days |
| 23393 | BBC Proms | 27762 days |
| 4496 | Meet the Press | 27555 days |
| 5730 | Macy's Thanksgiving Day Parade | 27027 days |
| 26183 | The BAFTA Awards | 26929 days |
| 28464 | The Emmy Awards | 26893 days |
| 1770 | ABC World News | 26805 days |
| 66550 | Sanremo Music Festival | 26311 days |


We have seen some entries with the links to their posters:

| shows | poster URL |  |
|---|---|---|
| Game of Thrones | http://www.hbo.com/game-of-thrones/1XS1oqL89opfnbLl8WnZY1O1uJx.jpg |
| Money Heist | https://www.netflix.com/title/80192098/reEMJA1uzscCbkpeRJeTT2bjqUp.jpg |
| Stranger Things | https://www.netflix.com/title/80057281/49WJfeN0moxb9IPfGn8AIqMGskD.jpg |
| The Walking Dead | http://www.amc.com/shows/the-walking-dead--1002293/n7PVu0hSz2sAsVekpOIoCnkWlbn.jpg |
| Lucifer | https://www.netflix.com/title/80057918/ekZobS8isE6mA53RAiGDG93hBxL.jpg |

(* *Most of the links have expired already*)

## Filtering the data
We have applied some filters to see the movies in english language related to mystery or crime, which are many and are not all are shown here, but some:
Breaking Bad, The Act, Sherlock, Marvel's Daredevil, The Mentalist, Gotham, etc.


We have listed the shows which started on 2023 and have been already cancelled:
| id | name | first_air_date | status |
|:---:|:---:|:---:|:---:|
| 1983 | Lockwood & Co. | 2023-01-27 | Canceled |
| 2206 | The Idol | 2023-06-04 | Canceled |
| 3003 | Gotham Knights | 2023-03-14 | Canceled |
| 4443 | True Lies | 2023-03-01 | Canceled |
| 4601 | Sky High: The Series | 2023-03-17 | Canceled |
| 5396 | High Desert | 2023-05-16 | Canceled |
| 5876 | Grease: Rise of the Pink Ladies | 2023-04-06 | Canceled |
| 5880 | The Watchful Eye | 2023-01-30 | Canceled |
| 5908 | The Company You Keep | 2023-02-19 | Canceled |
| 6227 | Dear Edward | 2023-02-02 | Canceled |
| 6734 | City on Fire | 2023-05-11 | Canceled |
| 7362 | The Head of Joaquín Murrieta | 2023-02-17 | Canceled |
| 8488 | Freeridge | 2023-02-02 | Canceled |
| 9002 | Up Here | 2023-03-24 | Canceled |
| 13253 | A Town Called Malice | 2023-03-16 | Canceled |
| 17265 | Slip | 2023-04-21 | Canceled |
| 19918 | The Low Tone Club | 2023-02-22 | Canceled |
| 20460 | Monster Factory | 2023-03-16 | Canceled |
| 20852 | @Gina Yei: #WithAllMyHeartAndMore | 2023-01-11 | Canceled |
| 21691 | Bling Empire: New York | 2023-01-20 | Canceled |

We have seen some the shows which have japanese as language, with their original name and their networks and production companies, for example:

"Naruto Shippūden", "ナルト 疾風伝", "TV Tokyo", "TV Tokyo, Pierrot, Sound Box"

## Plotting
Fianlly we have produced some plots to get more insights into the data See 
```
movie_project/movie_project/reports/figures
```

1. We have seen that the number of TVs shows has increased exponenitally:

2. We have analysed the types of shows for the las decades:

We can see that the distribution has changed throughout the years. To highlight are the increase of Miniseries (specially in the 70s and 80s), of Documentaris, and of Reality shows (this in particular since the 2000s).
We can also see that News were important in the 40s but not any longer. In general the relative increase of Miniseries, Realities and Documentaries has been to the expense of scripted shows.

3. We generated a general overview of the shows per genre. Dominating genres are Comedy, Sci-Fi, Drama and Action.

### Other/Extra:
A part from the beforementioned, we have generated a full python package, using an IDE (VSCode), using version control (git), generated unit tests, and checked for lint using pylint, and coverage using coverage.

### Bibliography/Resources:
[VSCode](https://code.visualstudio.com/)

[Git](https://git-scm.com/) and [GitHub](https://github.com/ulisesrey)

[PyLint](https://pypi.org/project/pylint/)

[Coverage](https://coverage.readthedocs.io/en/7.4.1/)

[Unit Test](https://docs.python.org/3/library/unittest.html)
