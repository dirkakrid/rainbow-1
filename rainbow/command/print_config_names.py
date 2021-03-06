# ----------------------------------------------------------------------
# rainbow, a terminal colorizer - https://github.com/nicoulaj/rainbow
# copyright (c) 2010-2017 rainbow contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import os


class PrintConfigNamesCommand(object):
    def __init__(self, paths=None):
        self.paths = paths or []

    def run(self):
        for path in self.paths:
            if path and os.path.isdir(path):
                for file in os.listdir(path):
                    if os.path.isfile(os.path.join(path, file)):
                        print(os.path.splitext(file)[0])
        return 0
