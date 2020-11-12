import abc


class Weights:
    __slots__ = ('weights', )

    def __init__(self, weights):
        self.weights = weights


class ProposedWeights:
    __slots__ = ('weights', 'vote_accuracy', 'test_accuracy', 'vote')

    def __init__(self):
        self.weights = None
        self.vote_accuracy = 0
        self.test_accuracy = 0
        self.vote = False


class MachineLearningInterface(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str:
        """
        Returns the name of the MLInterface
        """
        pass

    @abc.abstractmethod
    def train_model(self) -> Weights:
        """
        Trains the model. This function may block. Returns new weights.
        """
        pass

    @abc.abstractmethod
    def stop_training(self):
        """
        Stops the training of the model.
        """
        pass

    @abc.abstractmethod
    def clone(self):
        """
        Returns a copy of the MLInterface
        """
        pass

    @abc.abstractmethod
    def test_model(self, weights: Weights = None) -> ProposedWeights:
        """
        Tests the proposed weights and fills in the rest of the fields
        """

    @abc.abstractmethod
    def accept_weights(self, weights: Weights):
        """
        Updates the model with the proposed set of weights
        :param weights: The new weights
        """
        pass

    @abc.abstractmethod
    def evaluate_model(self, eval_config: dict) -> dict:
        """
            Evaluate the model on testset, using the metrics specified in eval_config.
            eval_config = {
                "name": lambda y_true, y_pred
            }
        """
        pass
