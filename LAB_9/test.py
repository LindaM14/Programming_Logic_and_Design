# print out lyrics with """ quotes (can collapse to not view, but still exists)
lyrics = """ 
One AM, eyes closed, I'm slowly falling
To the music and the atmosphere
Now and then, I feel lights fading softly
All over me and I remember last year

When I was alone in my bed
With all these thoughts in my head
And living silently inside

It's so late in the night, my mind is drifting away
Then I dream about times I wished for a new, happier day
If a hand could reach out right now and save my life somehow
I'll face the sun again as soon as this dreary night ends

Don't wanna go down like this
My head's in a place that I don't miss
So ugly, so grumpy
Sleepin' in the meantime, just stay comfy
Once everything's said and done
I know I'll be okay, I will overcome
I'm hoping, I'm coping, I'm here
I remember last year

When I was alone in my bed
Unhappy thoughts in my head
And living silently inside (Inside)
Just keeping all to myself
Wished I could be somewhere else
Back when I could only hide

It's so late in the night, my mind is drifting away
Then I dream about times I wished for a new, happier day
If a hand could reach out right now and save my life somehow
I'll face the sun again as soon as this dreary night ends
(End, end, end, end, end, end, end...)

(It's so late in the night, my mind is) drifting away
Then I dream about times I wished for a new, happier day
If a hand could reach out right now and save my life somehow
I'll face the sun again as soon as this dreary night ends

(I'll face the sun again as soon as this dreamy night ends)
"""

# write lyrics down in lowercase
lyrics = lyrics.lower()

# replacing special characters with 'spaces'
invalid_characters = ['(', ')', ',', '.','\'',]
for character in invalid_characters:
    lyrics = lyrics.replace(character,' ')
print(lyrics)

# # split, how many words in lyrics
# words = clean_lyrics.split()
# print(words)
# print()
# print(f'Total word count: {len(words)}')
# print()
# # split, how many lines in lyrics
# lines = clean_lyrics.splitlines()
# print(lines)
# print()
# print(f'Total line count: {len(lines)}')
# print()
# # # word frequency, how many times does each word appear in the song
# frequencies = {}
# for word in words:
#     if word not in frequencies:
#         frequencies[word] = 1
#     else:
#         frequencies[word] += 1
# print(f'Total words without being repeated: {len(frequencies)}')
# print()
# # printing out words and frequency
#
# list_key = []
# print(f'Word      Frequency')
# print()
# for key, value, in frequencies.items():
#     print(f'{key:<12}{value:<12}')
#
#
#
#
#
#
#
