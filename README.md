# Boolean Question

[![PyPI](https://img.shields.io/pypi/v/boolean_question)](https://pypi.org/project/boolean_question)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FSaadmairaj%2Fboolean-question&count_bg=%23A389F1&title_bg=%23555555&icon=pytorch.svg&icon_color=%23E7E7E7&title=welcomed&edge_flat=false)](https://hits.seeyoufarm.com)
[![CodeFactor](https://www.codefactor.io/repository/github/saadmairaj/boolean-question/badge/master)](https://www.codefactor.io/repository/github/saadmairaj/boolean-question/overview/master)
[![Downloads](https://pepy.tech/badge/boolean_question)](https://pepy.tech/project/boolean_question)

Get accurate answer prediction for True / False question using this python pytorch model. The model takes a passage and question as input and returns either "True" or "False" as predicted answer. Model used is [RoBERTa](https://arxiv.org/abs/1907.11692) that is further trained on [BoolQ](https://arxiv.org/abs/1905.10044) dataset.

## Installation

Install it with python package installer pip

```bash
pip install boolean_question
```

or install the latest master branch

```bash
pip install git+https://github.com/Saadmairaj/boolean-question
```

## Usage

The usage is simple and straight forward, import `BoolQ` class model and pass arguments to the `BoolQ.predict(passage: str, question: str)` method to predict the boolean answer "True" or "False"

```python
import pprint
from boolean_question import BoolQ

bq = BoolQ()

passage = """
A red dwarf is the smallest and coolest kind of star on the main sequence.
Red dwarfs are by far the most common type of star in the Milky Way, at
least in the neighborhood of the Sun, but because of their low luminosity,
individual red dwarfs cannot be easily observed."""

question = "Coolest star in the Milky way is a Red dwarf"

# Predict the answer from the passage and the question
ans = bq.predict(passage, question)
print(ans)

# After prediction extra details of the prediction can be seen with the below command
pprint.pprint(bq.prediction_details())
```

<details>
<summary>View output</summary>
<p>

    True
    {'answer': True,
    'confidence': None,
    'false confidence': 0.01,
    'passage': '\n'
                'A red dwarf is the smallest and coolest kind of star on the main '
                'sequence. Red dwarfs are by far the most common type of star in \n'
                'the Milky Way, at least in the neighborhood of the Sun, but '
                'because of their low luminosity, individual red dwarfs cannot '
                'be \n'
                'easily observed.',
    'question': 'Coolest star in the Milky way is a Red dwarf',
    'true confidence': 0.99}

</p>
</details>
