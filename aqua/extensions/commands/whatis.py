# Copyright 2021 Guilherme-Vasconcelos
# This file is part of Aqua.
#
# Aqua is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Aqua is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Aqua.  If not, see <https://www.gnu.org/licenses/>.

import logging
from re import sub
from urllib import parse

import requests
from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.checks import authorize, ensure_context_number_args
from aqua.utils import logged_send_message

WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"


@authorize
@ensure_context_number_args(1, "min")
def whatis(update: Update, context: CallbackContext) -> None:
    try:
        page_to_search = " ".join(context.args)

        # Instead of directly using the user's input to search the page, first use OpenSearch
        # to find out the exact page's name. This allows case insensitive search.
        open_search_params = {
            "action": "opensearch",
            "search": page_to_search,
            "utf8": "",
            "limit": "1",
            "format": "json",
        }

        open_search_response = requests.get(WIKIPEDIA_API_URL, open_search_params)
        page_title = open_search_response.json()[1][0]

        user_search_params = {
            "action": "query",
            "format": "json",
            "utf8": "",
            "prop": "extracts",
            "explaintext": "1",
            "exintro": "1",
            "titles": page_title,
        }

        response = requests.get(WIKIPEDIA_API_URL, user_search_params)

        data = response.json()

        msg = sub(r"\n+", "\n", list(data["query"]["pages"].values())[0]["extract"])
        while len(msg) > 0 and msg[-1] == "\n":
            msg = msg[:-2]
        msg = msg.replace("\n", "\n\n")

        if len(msg) == 0:
            raise Exception("Message has length 0, page must be invalid.")

        msg += (
            "\n\nThis search was performed on Wikipedia: "
            f"https://en.wikipedia.org/wiki/{parse.quote(page_title)}"
        )

        logged_send_message(update, context, msg)

    except Exception as e:
        logging.error(e)
        logged_send_message(
            update,
            context,
            f"Sorry! An error ocurred when looking for information about {page_to_search}.\n\n"
            "It may be the case that you misspelled it.",
        )
