import settings

from utils import parse_args

from operator import itemgetter

from stemming.porter2 import stem


def main():
    args = parse_args()
    app = MousePredictionModel(args=args)
    app.run()
    pass


class MousePredictionModel:

    def __init__(self, args):
        self._filename = args.input
        self._sentences = []

    def run(self):

        self._read_file()
        for sentence in self._sentences:
            result = []
            for predict_model_key in settings.MOUSE_PREDICTION_MODEL.keys():
                percentage = self._predict_model(sentence, settings.MOUSE_PREDICTION_MODEL[predict_model_key])
                result.append((predict_model_key, percentage))
            print(max(result, key=itemgetter(1))[0])

        pass

    def _read_file(self):
        with open(self._filename, 'r+') as content:
            number_of_elems = content.readline().rstrip('\n')
            # Checking if number is digit. If so, convert it to integer.
            if number_of_elems.isdigit():
                number_of_elems = int(number_of_elems)
                for line_number in range(number_of_elems):
                    self._sentences.append(content.readline().rstrip('\n'))

    def _predict_model(self, sentence, dict):
        tokens = [stem(x).lower().rstrip('.') for x in sentence.split(" ")]
        existing_stems = [x for x in tokens if x in dict]
        return format(len(existing_stems) / len(tokens), '.5f')


if __name__ == "__main__":
    main()
