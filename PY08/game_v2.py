'''
Игра угадай число.
Комрьютер сам загадывает и укадывает число.

'''

import numpy as np

def random_predict(number: int=1) -> int:
    """
    PC generets random number and guesses it

    Args:
        number (int, optional): maked number . Defaults to 1.

    Returns:
        int: number of attempts
    """
    
    count = 0
    
    while True:
        count +=1
        predict_number = np.random.randint(1, 500)
        if number == predict_number:
            break
    return count

def score_game(random_predict) -> int:
    """For how many attempts 
    on average out of 1000 approaches 
    does our algorithm guess

    Args:
        random_predict ([type ): guessing function

    Returns:
        int: average number of attempts
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

 
if __name__ == '__main__':
    score_game(random_predict)
    
# score_game(random_predict)