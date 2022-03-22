import random

"""
Program that asks the user to enter two integers representing the start and the end of the range.
Program generate a random number within this range and ask the user to guess numbers until they guess the 
randomly generated number.  
"""


class AbstractGame:
    def start(self):
        while True:
            start = input('Would you like to play? ')
            if start.lower() == 'yes' or start.lower() == 'no':
                break

        if start.lower() == 'yes':
            self.play()
        else:
            self.end()

    @staticmethod
    def end():
        print('The game has ended.')

    def play(self):
        raise NotImplementedError('You must implement play()')


class RandomNumberGuesser(AbstractGame):
    def play(self):
        first_number = input('Enter the start of the range: ')
        while not first_number.isdigit():
            print('Please enter a valid number. \n')
            first_number = input('Enter the start of the range: ')

        second_number = input('Enter the end of the range: ')
        while not second_number.isdigit() or int(second_number) < int(first_number):
            print('Please enter a valid number. \n')
            second_number = input('Enter the end of the range: ')

        random_number = random.randint(int(first_number), int(second_number))
        attempts = 0
        guess = None

        while guess != random_number:
            guessed_number = input('Guess a number: ')
            if not guessed_number.isdigit():
                print('Please enter a valid number')
                continue

            attempts += 1
            guess = int(guessed_number)

        suffix = ''
        if attempts > 1:
            suffix = 's'

        print(f'You guessed the number in {attempts} attempt{suffix}.')

        self.end()


game = RandomNumberGuesser()
game.start()
