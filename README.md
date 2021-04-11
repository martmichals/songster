## Inspiration
Arguably, one of the greatest lyrical albums of all time is Graduation by Kanye West (we can debate this later). Sadly, his more recent releases have been less than stellar, leaving a collective hole in fans' hearts. Another album, "In the Aeroplane Over the Sea" by Neutral Milk Hotel, is widely regarded as a monumental recording - but the band chose to disappear after its releasse. 

For fans longing for more content that an artist can't or won't provide, a solution has been conspicuously absent... until now. 

## What it does
Songster takes in an artist and number of songs, and trains a model off of that artist's most popular songs. It then generates a small verse of lyrics based on the training data that resembles the style of the artist. This tool is presented in the form of a user-friendly webpage. 

## How we built it
We leveraged Flask to create a clean user-interface through a web page to allow the user to input an artist name and song limit. We wrote everything in Python and used the PyCharm IDE for most of our development. We used the Genius API to download song lyrics from a specified artist to create a corpus of songs. Then, we used the corpus of songs to create a transition matrix specifying word pairs and their next most probable word, allowing us to create a Markov chain to create lyrics of a given length.

## Challenges we ran into
We bit off more than we could chew at the beginning. Our inital NLP model used a LSTM Reccurent Neural Network trained one song at a time. The model would require at least 1 hour per song, and given our time constraints, we would have only been able to train 5 songs: not enough for our purposes.

We have an issue where some lyrics would lead to a loop of the same lyrics over and over again, and this is an issue where a steady-state word pair is reached, meaning that the transition matrix applied to the word leads to the same word. 

## Accomplishments that we're proud of
We found it very satisfying to utilize linear algebra to generate text in a more simpler fashion than with a neural network. The creation of a transition matrix that stored word pairs with the most probable next words is a very simple way to generate lyrics that are decently coherent through a Markov chain. 

## What we learned
In the process of creating Songster, we explored multiple algorithms in the field of Natural Language Processing (NLP). These algorithms included Recurrent Neural Networks, Markov Matrices, TF-IDF, and more. We explored the pros and cons of each, in terms of implementation difficulty, accuracy, and versatility. 

Additionally, as early-stage software developers, we greatly developed our skills in Full-Stack development, using tools including Flask, NumPy, TensorFlow, and REST APIs. 

## What's next for Songster
**Recurrent Neural Network:** Our algorithm functions off of a transition matrix Markov Chain. A more powerful word-prediction technique would be Deep Learning, using Tensorflow and Keras to create a neural network. We have an elementary implementation of an RNN working at the moment, but in its current state, the Markov matrix outputs more desirable results. 

**Part-of-speech Tagging:** Our algorithm serves to find consequent words, but does not necessarily enforce subject-verb-agreement and proper grammar in its current state. Using Part-of-speech tagging, we can force the lyrics generation into forming more coherent thoughts, which would make it more realistic and human-like in its writing. 

**Genre-based Generation:** In its current state, Songster only trains off of songs from a particular artist. With genre-based generation, we can create more generic songs, or songs that have more diverse influence and are less apparently generated off of one particular writer. 

**Lyrical Comparison:** Using the Term Frequency - Inverse Document Frequency (TF-IDF) algorithm, we can compare the frequency of words and phrases between two categories (album to album, artist to artist, song to song, genre to genre). This algorithm can serve two purposes for the future of Songster. First, we can use this to provide more unique lyric generation for a certain artist, or to exclude certain training data from generation. Additionally, we can create a secondary tool for Songster where users can analyze common phrases and distinct lyrics used by certain artists or in certain collections of songs. Applications of this include plagiarism detection, lyrical analysis, and visualizations. 
