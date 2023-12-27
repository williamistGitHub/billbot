#     billbot - a very random discord bot
#     Copyright (C) 2023  williamist
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

# this script is ran by the live server to set things up.
# please don't modify!

import os

import billbot

if "BOT_TOKEN" not in os.environ:
    with open("SECRET_token.txt") as token_file:
        os.environ["BOT_TOKEN"] = token_file.read()

if "DEV_SERVER" not in os.environ:
    with open("SECRET_devserv.txt") as id_file:
        os.environ["DEV_SERVER"] = id_file.read()

billbot.go()
