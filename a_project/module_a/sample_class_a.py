class SampleA:
    """
    Documentation sample.
    It's a fake class.
    """
    def __init__(self):
        self.range=list(range(10))

    def get_cumulative_sum(self) -> int:
        """
        A cumulative sum calculator for the range class parameter.

        :return: The cumulative sum of the range param
        """
        accumulator = 0
        for x in self.range:
            accumulator += x
        return accumulator
