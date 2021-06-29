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
#
# CREDITS:
# Thanks lipsum.com (by James Wilson) for the sentences.
# Check it out his website: https://lipsum.com/

from secrets import choice

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.checks import authorize, ensure_context_number_args
from aqua.utils import logged_send_message, safe_randint

lorem_sentences = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Etiam ac nisi vitae nunc finibus tempor ac a nibh.",
    "Fusce facilisis ligula ipsum, vitae tincidunt dui volutpat non.",
    "Proin varius dapibus sollicitudin.",
    "Donec id urna sit amet dolor euismod lobortis.",
    "Nullam tempus scelerisque purus, sed mattis elit condimentum nec.",
    "Curabitur vestibulum aliquet interdum",
    "Sed tempor, magna vitae ultricies ornare, lacus nisl interdum ipsum, id rutrum sem eros id eros.",
    "Curabitur non justo varius nibh pellentesque sagittis vitae gravida enim.",
    "Phasellus sed ligula est.",
    "Nullam non massa blandit, dignissim turpis ac, luctus lorem.",
    "Donec ullamcorper magna non fringilla auctor.",
    "Nulla laoreet aliquet libero, vitae consectetur erat placerat sit amet.",
    "Praesent placerat felis non augue viverra faucibus.",
    "Pellentesque in leo auctor tortor consequat porta hendrerit nec nibh.",
    "Vestibulum dapibus ultricies volutpat.",
    "Maecenas condimentum, sem eget faucibus vulputate, mauris ante tempus nunc, nec dictum tortor nunc sed orci.",
]


@authorize
@ensure_context_number_args(0, "exact")
def lorem(update: Update, context: CallbackContext) -> None:
    paragraph = ""
    number_of_sentences = safe_randint(6, 12)
    for i in range(number_of_sentences):
        if i == 0:
            sentence = lorem_sentences[0]
        else:
            sentence = choice(lorem_sentences)
        paragraph += sentence + " "

    logged_send_message(update, context, paragraph)
