## Inspiration
Pre-pandemic we would often enjoy music with the company of others. We would sing along to artists like *Taylor Swift* and *Kanye*. Since then, however, we have been confined inside with seemingly endless Zoom meeting and classes. Seldom could we find a meaningful way to enjoy music with other virtually. This is why we created Songster. By creating a novel way to enjoy music, we have found a way to ease the physical distance between our family and friends: **a way to rekindle connections.** 

## What it does
A web-app that creates lyrics based on a given artist's name and database of songs sourced from Genius.

## How we built it
We leveraged Flask to create a clean user-interface through a web page to allow the user to input an artist name and song limit. We wrote everything in Python and used the PyCharm IDE for most of our development. We used the Genius API to download song lyrics from a specified artist to create a corpus of songs. Then, we used the corpus of songs to create a transition matrix specifying word pairs and their next most probable word, allowing us to create a Markov chain to create lyrics of a given length.

## Challenges we ran into
We bit off more than we could chew at the beginning. Our inital NLP model used a LSTM Reccurent Neural Network trained one song at a time. The model would require at least 1 hour per song, and given our time constraints, we would have only been able to train 5 songs: not enough for our purposes.

We have an issue where some lyrics would lead to a loop of the same lyrics over and over again, and this is an issue where a steady-state word pair is reached, meaning that the transition matrix applied to the word leads to the same word. 

## Accomplishments that we're proud of
We found it very satisfying to utilize linear algebra to generate text in a more simpler fashion than with a neural network. The creation of a transition matrix that stored word pairs with the most probable next words is a very simple way to generate lyrics that are decently coherent through a Markov chain. 

## What we learned

## What's next for Songster
