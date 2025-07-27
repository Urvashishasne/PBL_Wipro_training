def ispalindrome(name):
    name = name.replace(" ", "")  
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = sum(1 for ch in name if ch in vowels)
    print(f"No of vowels: {count}")

def frequency_of_letters(name):
    freq = {}
    for ch in name:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1
    print("Frequency of letters:", end=" ")
    print(", ".join([f"{k}-{v}" for k, v in freq.items()]))
