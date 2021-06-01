
def calc_bayes1(prob_H_and_E, prob_B):
    return prob_H_and_E / prob_B

def calc_bayes(prob_H, prob_E_dado_H, prob_notH, prob_E_dado_notH):
    return(prob_H * prob_E_dado_H) / ((prob_H * prob_E_dado_H) + (prob_notH * prob_E_dado_notH))

def main():
    prob_H = 1 / 100000
    prob_E_dado_H = 1
    prob_E_dado_notH = 10/99999
    prob_notH = 1 - prob_H
    
    prob_H_and_E = prob_H * prob_E_dado_H
    prob_E = (prob_H * prob_E_dado_H)+ (prob_notH * prob_E_dado_notH)
    
    prob_H_dado_E1 = calc_bayes1(prob_H_and_E, prob_E)
    prob_H_dado_E2 = calc_bayes(prob_H, prob_E_dado_H, prob_notH, prob_E_dado_notH)

    print(f'{prob_H_dado_E1} {prob_H_dado_E2} {1/11}')


if __name__ == '__main__':
    main()