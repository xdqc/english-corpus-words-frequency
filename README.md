# english-corpus-words-frequency
Compare various English corpus by measuring differences between words frequency lists.

## Corpus

- [My Twitter Curpus](https://github.com/xdqc/tweet-trend-everyday) - `twit`

- [Norvig Natural Language Corpus](https://github.com/colinscape/norvig-frequencies/tree/master/data) - `norv`

- [Google's Ngram Corpus](https://github.com/hackerb9/gwordlist) - `ngra`

- [Wikipedia Frequency Lookup](https://github.com/prabhakar267/wikipedia-frequency-lookup) - `wiki`

- [Google 10000 English](https://github.com/first20hours/google-10000-english) - `goog`

- [Corpus of Contemporary American English](https://github.com/oyrx/word_frequency) - `coca`

- [Open Subtitle](http://opus.nlpl.eu/index.php) - `subt`

## Dictionary

- [Oxford](https://github.com/DevangMstryls/Oxford-English-Dictionary-41K-words-) `dict_oxford.txt`

- [Webster](https://github.com/matthewreagan/WebstersEnglishDictionary) `dict_webster.txt`

- [English words](https://github.com/dwyl/english-words) `dict_alpha.txt`


## How to compare corpus?

#### Similarity

**Similarity** of two corpus depends on *percentage of common words* and *average word distance* in two corpus.

#### Word distance

**Distance** means how far away a word position of the frequency ranking in different corpus. Distance has sign (can be negative).

*distance* = *ln(indexofWordInSecondCorpus)* - *ln(indexofWordInFirstCorpus)*


#### Compare size

Two corpus are compared by same size of N most common words. Typically, most 10000 common words cover 97% of entire corpus; most 20000 common words conver more than 99% of entire corpus.

#### Dictionary filter

Use dictionaries as masks to mitigate criteriary differences when generating these corpus.


## Comparison

### Results

one of the results using *all-dictionary mask* and *10000 compare size*.
![alt text](https://raw.githubusercontent.com/xdqc/english-corpus-words-frequency/master/results/t-all-10000.PNG "dictinary mask=dict_all, compare size=10000")

![alt text](https://raw.githubusercontent.com/xdqc/english-corpus-words-frequency/master/results/g-all-10000.PNG "dictinary mask=dict_all, compare size=10000")

`norv` and `ngra` have 99.9% words in common, and 100x similarity value to other corpus, thuns can be considered the same.

### Common words comparison

Words with distance > 2 common in both corpus (unfiltered, 20000 size), each ordered by absolute distance:

|          | **coca**  | **norv**  | **twit**  |**wiki**| **goog**  | **subt**  |
| ---------|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| **coca** |               |[#](#coca-norv)|[#](#coca-twit)|[#](#coca-wiki)|[#](#coca-goog)|[#](#coca-subt)|
| **norv** |[#](#coca-norv)|               |[#](#norv-twit)|[#](#norv-wiki)|[#](#norv-goog)|[#](#norv-subt)|
| **twit** |[#](#coca-twit)|[#](#norv-twit)|               |[#](#twit-wiki)|[#](#twit-goog)|[#](#twit-subt)|
| **wiki** |[#](#coca-wiki)|[#](#norv-wiki)|[#](#twit-wiki)|               |[#](#wiki-goog)|[#](#wiki-subt)|
| **goog** |[#](#coca-goog)|[#](#norv-goog)|[#](#twit-goog)|[#](#wiki-goog)|               |[#](#goog-subt)|
| **subt** |[#](#coca-subt)|[#](#norv-subt)|[#](#twit-subt)|[#](#wiki-subt)|[#](#goog-subt)|               |


----
#### coca-norv

>wo
unidentified
yeah
mr
clinton
ca
iraq
saddam
bush
ok
kids
guys
dr
iraqi
inc
tonight
larry
atlanta
hussein
guy
gore
sept
says
denver
weekend
movie
houston
sawyer
maybe
basketball
lot
republicans
cbs
democrats
nbc
hey
caller
chris
thank
mike
mrs
somebody
baseball
biggest
players
jeff
kid
tv
fans
championship


>s
fig
de
vol
lord
labour
x
cent
chapter
shall
o
und
y
god
centre
der
anti
pre
b
appendix
op
en
n
sub
self
t
behaviour
thy
ibid
majesty
vi
thou
re
present
relation
med
induced
c
following
z
ex
la
ml
le
ion
act
thee
d
viii
english
thereof
specified
unto
u
owing
ne
upon
iv
bibliography


----
#### coca-twit

>percent
toward
began
iraq
soviet
seemed
iraqi
bush
programs
environmental
ca
correspondent
studies
wo
although
moreover
nodded
thus
among
characteristics
relatively
indicated
participants
television
particularly
factors
mixture
differences
considerable
washington
conventional
gore
hussein
mr
subjects
however
several
literature
telephone
recalls
instance
nevertheless
significant
economic
kuwait
larry
perceptions
cultural
eight
larger

>trump
u
cant
im
ive
fuck
porn
wont
isnt
youre
fucking
pussy
youtube
shes
shit
thats
id
x
uk
ass
facebook
o
s
heres
bitch
th
anti
yo
wouldnt
pre
via
ya
whos
dude
followers
couldnt
wasnt
t
y
fake
check
sa
youve
n
ex
whats
anal
videos
cute
kinda
download
hate
info
theres
update
awesome
nude


----
#### coca-wiki

>

>


----
#### coca-goog

>

>


----
#### coca-subt

>

>

----
#### norv-twit

>

>


----
#### norv-wiki

>fig
shall
self
your
non
anti
our
you
we
chapter
know
me
cent
myself
think
re
thou
ought
my
yes
pre
et
say
suppose
vol
ourselves
thy
might
seemed
sure
looked
why
eds
let
nothing
yourself
mind
thing
indeed
surely
dear
knew
unto
should
figure
god
question
certainly
table
hardly

>album
championship
debut
football
released
tournament
season
featured
league
municipality
awards
hockey
team
won
stadium
games
film
award
medal
club
renamed
scored
career
player
located
played
basketball
song
featuring
episode
teams
awarded
champions
br
festival
bbc
coach
game
born
st
band
station
video
census
currently
guitar
township
cricket
matches
soccer


----
#### norv-goog

>

>


----
#### norv-subt

>

>


----
#### twit-wiki

>

>


----
#### twit-goog

>

>


----
#### twit-subt

>lol
trump
im
ive
youre
dont
hes
cant
twitter
ur
tweet
didnt
vs
thats
via
theres
u
bc
pic
anti
pre
democrats
ht
followers
app
youtube
w
videos
ft
uk
eu
niggas
wont
whats
streaming
mueller
haha
liberals
obama
porn
video
teen
republicans
lil
hardcore
added
update
ny
july
trans
bs
fr
etc
cnn

>didn
isn
doesn
don
haven
sighs
ain
lieutenant
uh
colonel
whoa
sergeant
narrator
majesty
madame
ln
ooh
gentlemen
l
ringing
mmm
um
detective
huh
madam
lt
upstairs
laughs
ow
applause
announcer
darling
hurry
chatter
lf
you
mister
bastard
inspector
sir
yeah
hmm
downstairs
clears
siren
annie
telephone
marty
uncle
coughing


----
#### wiki-goog

>became
won
played
born
debut
later
municipality
league
railway
began
founded
named
defeated
notable
politician
championship
released
renamed
season
known
served
genus
squadron
village
appeared
championships
remained
former
regiment
medal
appearances
died
aired
population
elected
formed
album
subsequently
billboard
career
appointed
scored
located
eventually
station
moved
graduated
species
emperor
promoted

>click
info
ebay
re
email
please
pm
page
your
privacy
search
copyright
web
contact
password
item
directory
add
buy
reply
forums
yahoo
cart
porn
reserved
thread
you
jan
compare
hotels
accessories
comments
oct
dec
nov
aug
our
seller
check
quote
message
am
mail
non
feb
download
downloads
price
shipping
online


----
#### wiki-subt

>

>


----
#### goog-subt

>copyright
ebay
user
pm
reviews
web
directory
email
links
page
forum
click
categories
index
info
products
software
listing
site
rating
online
jan
accessories
x
comments
yahoo
posts
hotels
services
uk
download
items
reserved
shipping
format
users
search
january
product
dvd
privacy
review
pc
topics
usa
view
website
mar
prices
sony
posted

>don
okay
uh
gonna
yeah
huh
hey
ooh
sir
excuse
hurry
gotta
laughs
alright
dad
kidding
haven
wanna
sorry
oh
gentlemen
um
bastard
mmm
won
darling
hmm
shit
forgive
scared
bye
swear
madam
marry
you
damn
narrator
ah
goodbye
worry
happened
shut
somebody
afraid
laughing
sweetheart
ow
shouting
wait
kill


