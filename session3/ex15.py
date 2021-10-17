"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""

x = input('')
lowecase = x.lower()

vowel_counts = {}


for vowel in 'aeiou':
    count = lowecase.count(vowel)
    vowel_counts[vowel]= count
print(vowel_counts)

counts = vowel_counts.values()
total_vowels = sum(counts)
print(total_vowels)


