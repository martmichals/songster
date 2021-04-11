## Inspiration
Pre-pandemic we would often enjoy music with the company of others. We would sing along to artists like *Taylor Swift* and *Kanye*. Since then, however, we have been confined inside with seemingly endless Zoom meeting and classes. Seldom could we find a meaningful way to enjoy music with other virtually. This is why we created Songster. By creating a novel way to enjoy music, we have found a way to ease the physical distance between our family and friends: **a way to rekindle connections.** 

## What it does
A web-app to create lyrics based on a given artist's name and database of songs sourced from Genius.

## How we built it

## Challenges we ran into
We bit off more than we could chew at the beginning. Our inital NLP model used a LSTM Reccurent Neural Network trained one song at a time. The model would require at least 1 hour per song, and given our time constraints, we would have only been able to train 5 songs: not enough for our purposes.

## Accomplishments that we're proud of
We found it very satisfying to utilize linear algebra to generate text in a more simpler fashion than with a neural network. The creation of a transition matrix that stored word pairs with the most probably word pair.

## What we learned

## What's next for Songster
