from django.core.management.base import BaseCommand, CommandError
import statistics

class Command(BaseCommand):

    help = 'Process to find the median of an array of numbers'

    def add_arguments(self, parser):
      parser.add_argument('Amount', nargs='+', type=int, help='Amount of Iterations')

    def handle(self, *args, **kwargs):

        quantity = kwargs['quantity']
        n = [];
        for unit in range(quantity[0]):
            try:

                data = (input("Enter Action and Number: "))
                value = data.split()

                if value[0] == 'a':
                    n.append(int(value[1]))

                if value[0] == 'r':
                    if int(value[1]) not in n:
                        self.stdout.write('Wrong!')
                    if int(value[1]) in n:
                        n.remove(int(value[1]))

                if len(n):
                    median = statistics.median(n)
                    self.stdout.write('Value Median: %s' % median)

            except:
                self.stdout.write('The second parameter must be a number')
