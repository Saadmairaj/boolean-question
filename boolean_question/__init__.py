#                       Copyright 2021 Saad Mairaj

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
Get accurate answer prediction for True or False question using this
python pytorch model. The model takes a passage and question as 
input and returns either "True" or "False" as predicted answer.
"""

__author__ = "Saad Mairaj"
__version__ = "0.0.2"

from boolean_question.boolq import BoolQ
