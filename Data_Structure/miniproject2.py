def runner_up(score:list):
    largest=max(score)
    n=len(score)
    runner_up=0
    for i in range(n):
        if score[i]<largest and score[i]>runner_up:
            runner_up=score[i]
    return runner_up
print(runner_up([2,3,4,5,6]))
    