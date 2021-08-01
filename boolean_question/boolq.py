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

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from boolean_question.utils import get_model, set_seed, device
from collections import OrderedDict


class BoolQ:
    """Boolean question model

    Predict answer as "True" or "False" by providing text 
    passage and a question related to the text passage 
    to the model. 

    Also, get the confidence for both "True" and "False"
    answer using `prediction_details` method. Else use just 
    `predict` method to get the most confident answer."""

    def __init__(self, model: str = None, confidence: float = None, seed: int = 26):
        """Initialise the BoolQ model to predict question from text passage.

        Args:
            model (str): Give path to the transformer model. By default \
                              is None.
            confidence (float): Give confidence level between (0.1 - 1.0) of \
                                the answer.By default is None, means will \
                                return the answer with maximum confidence.
            seed (int): Change seed for reproducibility. By default is 26.        
        """
        # Use a GPU if you have one available (Runtime -> Change runtime type -> GPU)
        model = model or get_model()

        # Set seeds for reproducibility
        set_seed(seed)

        self.tokenizer = AutoTokenizer.from_pretrained(model)
        self.model = AutoModelForSequenceClassification.from_pretrained(model)
        self.model.to(device=device())

        self._conf = confidence

    def predict(self, passage: str, question: str):
        """Predict if the given question is true or false from the passage.

        Args:
            passage (str): Give an input text passage.
            quesion (str): Give a question related to the given text passage.

        Returns:
            Boolean: Either True for correct question or False for wrong question."""

        self.passage = passage
        self.question = question

        sequence = self.tokenizer.encode_plus(
            question, passage, return_tensors="pt")['input_ids'].to(device())

        logits = self.model(sequence)[0]
        probabilities = torch.softmax(logits, dim=1).detach().cpu().tolist()[0]
        self.probability = OrderedDict()
        self.probability[True] = round(probabilities[1], 2)
        self.probability[False] = round(probabilities[0], 2)

        self.answer = [k for k, v in self.probability.items(
        ) if v == max(self.probability.values())][0]
        if self._conf is None or self._conf <= self.answer:
            return self.answer
        return None

    def prediction_details(self):
        """Get complete prediction details"""
        if getattr(self, 'probability', None) is None:
            raise RuntimeError(
                "No answer prediction found. Please run predict first")
        data = {}
        data['passage'] = self.passage
        data['question'] = self.question
        data['confidence'] = self._conf
        data['true confidence'], data['false confidence'] = list(
            self.probability.values())
        data['answer'] = self.answer
        return data
