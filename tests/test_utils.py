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

import pytest

import aqua.utils as u

# PREFIX SUBSTRINGS


def test_that_empty_string_has_zero_prefix_substrings():
    assert len(u.prefix_substrings("")) == 0


def test_that_a_string_with_three_letters_has_exactly_three_prefix_substrings():
    assert len(u.prefix_substrings("bar")) == 3


def test_that_aqua_has_prefix_substrings_a_aq_aqu_aqua():
    assert set(u.prefix_substrings("aqua")) == {"a", "aq", "aqu", "aqua"}


# SAFE RANDINT


def test_that_after_100_randints_between_0_and_10_they_are_all_between_0_and_10():
    numbers = [u.safe_randint(0, 10) for _ in range(100)]
    assert not any(number < 0 or number > 10 for number in numbers)


def test_that_randint_between_5_and_5_will_always_return_5():
    numbers = [u.safe_randint(5, 5) for _ in range(100)]
    assert all(number == 5 for number in numbers)


def test_that_randint_when_lower_bound_is_greater_than_upper_bound_raises_exception():
    with pytest.raises(Exception):
        u.safe_randint(10, 5)
