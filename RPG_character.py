#!/usr/bin/env python3

# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   RPG_character.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/05 15:00:50 by mny-aro-            #+#    #+#            #
#   Updated: 2026/10/05 15:00:50 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):

    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    stats = [strength, intelligence, charisma]

    for stat in stats:
        if not isinstance(stat, int):
            return "All stats should be integers"
    for stat in stats:
        if stat < 1:
            return "All stats should be no less than 1"
    for stat in stats:
        if stat > 4:
            return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"

    return (
        f"{name}\n"
        f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
        f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
        f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    )
