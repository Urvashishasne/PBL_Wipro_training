import sys
if len(sys.argv) != 4:
    print("Please enter 3 strings separated by space.")
    print("Example: python student_happiness.py 3-1 5-7 1-5-3-8")
    sys.exit()
likes = sys.argv[1]
dislikes = sys.argv[2]
given = sys.argv[3]
like_list = likes.split("-")
dislike_list = dislikes.split("-")
given_list = given.split("-")
like_nums = []
for i in like_list:
    like_nums.append(int(i))
dislike_nums = []
for i in dislike_list:
    dislike_nums.append(int(i))
given_nums = []
for i in given_list:
    given_nums.append(int(i))
happiness = 0
for num in given_nums:
    if num in like_nums:
        happiness += 1
    elif num in dislike_nums:
        happiness -= 1
print(happiness)
