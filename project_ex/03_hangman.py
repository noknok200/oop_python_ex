"""
Title       행맨
Reference   나만의 Python Game 만들기 Chapter 9 p.139
Author      kadragon
Date        2018.08.22
"""

# Generate pseudo-random numbers
import random

# ASCII Art
HANGMAN_PICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========

''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========

''', '''

  +---+
  |   |
  0   |
  |   |
      |
      |
=========

''', '''

  +---+
  |   |
  0   |
 /|   |
      |
      |
=========

''', '''

  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========

''', '''

  +---+
  |   |
  0   |
 /|\  |
  |   |
      |
=========

''', '''

  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========

''', '''

  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========

''']

# 행맨으로 맞출 문자열을 띄어쓰기로 구분하여 입력하고, split()을 이용하여 분할, 리스트로 저장
words = 'people history way art world information map tow family government health system computer meat year thanks music person reading method data food understanding theory law bird literature problem software control knowlegde power ability economics love internet television science library nature fact product idae temperature investment area society'.split()


def get_random_word(word_list):
    """
    맞출 대상이 되는 문자열들의 리스트에서 임의의 단어 하나를 선택하여 반환한다.
    :param word_list: target words list
    :return: random words
    """
    # https://docs.python.org/ko/3/library/functions.html?highlight=len#len
    # len() 객체의 길이를 반환함.
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


def display_board():
    """
    행맨이 진행되고 있는 상태를 ASCII Art 를 활용하여 보여주는 함수.
    """
    print(HANGMAN_PICS[len(missed_letters)])    # 틀린 횟수 만큼, 행맨 ASCII Arts 를 진행한다.

    print('Missed letters:', end=' ')           # end= 를 활용하면, 줄 바꿈 대신 다른 표기 방법을 활용 할 수 있다.
    for letter in missed_letters:               # 틀린 문자열을 한개씩 띄어쓰기로 구분하여 출력
        print(letter, end=' ')
    print()

    for k in range(len(secret_word)):           # 맞춘 문자를 참고하여, _ _ a _ _ 와 같이 출력하기
        print(secret_word[k] if secret_word[k] in correct_letters else '_', end=' ')
    print()


def get_guess(already_guessed):
    """
    사용자에게 문자 1개를 입력 받아, 한 글자 입력 받았는지, 입력했던 것인지, 영어 소문자인지 확인
    :param already_guessed: 사용자가 지금까지 입력 했던 문자열
    :return: 검증된 문자 하나
    """
    while True:
        user_guess = input('Guess a letter: ').lower()      # lower 모든 케이스 문자가 소문자로 변환된 문자열의 복사본을 돌려줌.
        if len(user_guess) != 1:                            # 한글자가 아니면 다시 입력하게 하기
            print('Please enter a single letter.')
        elif user_guess in already_guessed:                 # already_guessed list (이미 입력했던 목록) 에 user_guess 가 있는지 확인
            print('You have already guessed that letter. Choose again.')
        elif user_guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return user_guess


def play_again():
    """
    사용자가 게임을 다시 시작할 것인지를 문의하는 프로그램
    :return: True or False

    아래 구문은 사용자로 부터 값을 입력 > 소문자로 변환 > 만약 'y' 로 시작하는 문자열이라면 True, 아니면 False
    https://docs.python.org/ko/3/library/stdtypes.html?highlight=startswith#str.startswith
    """
    return input('Do you want to play again? (yes or no): ').lower().startswith('y')


missed_letters = ''        # 사용자가 입력하여 틀린 문자들을 저장하는 공간
correct_letters = ''       # 사용자가 입력하여 맞춘 문자들을 저장하는 공간
secret_word = get_random_word(words)    # 사용자가 맞출 임의의 문자를 선택
game_is_done = False

print('=' * 80)
print('H A N G M A N')
print('=' * 80)

while True:
    display_board()

    guess = get_guess(missed_letters + correct_letters)     # 이미 입력한 것을 확인하기 위하여, 틀린것과 맞춘 문자를 연결하여 보냄

    if guess in secret_word:                            # 사용자로부터 입력 받은 문자 하나가, 맞춰야할 문자열내에 있는지 확인
        correct_letters = correct_letters + guess       # 있다면, 맞춘 문자열을 저장하는 공간에 추가

        # 정답을 맞췄는지 확인하는 로직 시작
        found_all_letters = True                        # 일단 맞췄다고 표기

        for i in range(len(secret_word)):               # 맞춰야할 문자열을 한개씩 확인하여, 맞춘 문자열에 모두 있는지 확인
            if secret_word[i] not in correct_letters:
                found_all_letters = False               # 만약 없다면, found_all_letters 를 False 처리하여 게임이 종료 X
                break

        if found_all_letters:                           # 게임 종료
            display_board()
            print('Yes! The secret word is %s! You have won!' % secret_word)
            game_is_done = True
    else:
        missed_letters = missed_letters + guess         # 틀린 문자열에 추가

    if len(missed_letters) == len(HANGMAN_PICS) - 1:    # 행맨의 목숨이 남아 있는지 확인하여 남아 있지 않으면 게임 종료
        display_board()
        print('You have run out of guesses!\n After %d missed guesses and %d correct guesses, the word was %s' % (len(missed_letters), len(correct_letters), secret_word))
        game_is_done = True

    if game_is_done:
        if play_again():                                # 게임을 다시 할지 사용자로 부터 입력 받아
            missed_letters = ''                        # 값들을 초기화
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break
