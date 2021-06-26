# Aqua
Aqua is a Telegram bot that provides you a collection of personal utilities.

### Available commands
All commands below can be abbreviated (e.g. you can use `/lo` instead of `/lorem`) as long as your
abbreviation is not ambiguous.

- `/lorem`: generates one paragraph of Lorem Ipsum text. 
- `/remindme <time> <time_unit> <message>`: reminds you about \<message> after the given amount of
time. Example: `/remindme 10 minute Get pizza in the oven` will remind you about the pizza in
about 10 minutes.
- `/sort <list of elements>`: sorts your list. If all the elements are numbers, they will be sorted
numerically, else alphabetically. Example: `/sort 5 2 1` or `/sort myword1 second_word`.
- `/start`: sends a "welcome" message. This can be useful to check if you have set up everything
correctly.
- `/whatis <search query>`: Gives you a brief summary about your search. Example: `/whatis linux kernel`.

More commands will be added soon!

### Documentation
For documentation (installation, development instructions and more) please check the [docs directory](docs/).

### License
Copyright 2021 Guilherme-Vasconcelos

Aqua is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Aqua is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Aqua.  If not, see <https://www.gnu.org/licenses/>.
