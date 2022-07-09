import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('merge_generator')

class MergeGenerator:
    def __init__(self, *iterables):
        self.iterables = iterables
        logger.debug(f'An Iterable of size {len(self.iterables)}')

    def gen_merge(self):
        logger.debug(f'Begin of generation of lists from a list(2D Array) ')
        for iter in self.iterables:
            yield iter
        logger.debug(f'End of generation of lists from a list(2D Array) ')

    def gen_main(self):
        ans = self.gen_merge()
        res = []
        try:
            logger.debug(f'Generating of the next list in the generator')
            while True:
                res = res + next(ans)
        except StopIteration as stopIteration:
            logger.debug(f'Generator function was successful')
            return sorted(res)

if __name__ == '__main__':
    list1 = [1, 5, 9]
    list2 = [2, 5]
    list3 = [1, 6, 10, 11]
    list4 = [8, 7, 4, 15]

    sol = MergeGenerator(list1, list2, list3, list4)

    print(sol.gen_main())