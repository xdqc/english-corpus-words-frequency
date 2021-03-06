# english-corpus-words-frequency

Compare English corpora by measuring differences between words lists ordered by frequency.

## Corpora

- [Twitter corpus](https://github.com/xdqc/tweet-trends) - `twit`

- [Norvig Natural Language Corpus](https://github.com/colinscape/norvig-frequencies/tree/master/data) - `norv`

- [Google's Ngram Corpus](https://github.com/hackerb9/gwordlist) - `ngra`

- [Wikipedia Word Frequency](https://github.com/IlyaSemenov/wikipedia-word-frequency) - `wiki`

- [Google 10000 English](https://github.com/first20hours/google-10000-english) - `goog`

- [Corpus of Contemporary American English](https://github.com/oyrx/word_frequency) - `coca`

- [Open Subtitle](http://opus.nlpl.eu/index.php) - `subt`

## Dictionaries

- [Oxford](https://github.com/DevangMstryls/Oxford-English-Dictionary-41K-words-) `dict_oxford.txt`

- [Webster](https://github.com/matthewreagan/WebstersEnglishDictionary) `dict_webster.txt`

- [English words](https://github.com/dwyl/english-words) `dict_alpha.txt`

## Terms

#### Similarity

**Similarity** of two corpus depends on both of _percentage of common words_ and _average word distance_ in two corpus.

#### Word distance

**Distance** indicates how far away a word position of the frequency ranking in different corpus. Distance has sign (can be negative).

_distance_ = _ln(indexofWordInSecondCorpus)_ - _ln(indexofWordInFirstCorpus)_

#### Comparison size

Each of the two-corpora-pair is compared using same size of N most common words. Typically, top 10000 common words cover 97% of the entire corpus; top 20000 common words conver more than 99% of the entire corpus.

#### Dictionary filter

Dictionaries are served as masks to inner join corpus for standarization.

## Comparisons

### Results

one of the results using _all-dictionary mask_ and _10000 compare size_. ![alt text](https://raw.githubusercontent.com/xdqc/english-corpus-words-frequency/master/results/t-all-10000.PNG 'dictinary mask=dict_all, compare size=10000')

![alt text](https://raw.githubusercontent.com/xdqc/english-corpus-words-frequency/master/results/g-all-10000.PNG 'dictinary mask=dict_all, compare size=10000')

`norv` and `ngra` have 99.9% words in common, and 100x similarity value to other corpora, thus can be considered the same. *Of course they are! https://norvig.com/ngrams/*

### Common words comparison

Lists of words with more than doubled distances ( |_distance_| > `2` ) which are common in both corpus (unfiltered, 20000 size), ordered by |_distance_|:

|          |        **coca**         |        **norv**        |         **twit**          |         **wiki**          |       **goog**        |         **subt**          |
|----------|:-----------------------:|:----------------------:|:-------------------------:|:-------------------------:|:---------------------:|:-------------------------:|
| **coca** |                         |  90's[#](#coca-norv)   |    00's[#](#coca-twit)    | colloquial[#](#coca-wiki) | media[#](#coca-goog)  |  politics[#](#coca-subt)  |
| **norv** |  [#](#coca-norv)paper   |                        | literature[#](#norv-twit) |   infer[#](#norv-wiki)    |  ibid[#](#norv-goog)  | scientific[#](#norv-subt) |
| **twit** |  [#](#coca-twit)vulgar  | [#](#norv-twit)playful |                           |    life[#](#twit-wiki)    | buzzy[#](#twit-goog)  |    news[#](#twit-subt)    |
| **wiki** | [#](#coca-wiki)document |  [#](#norv-wiki)event  |    [#](#twit-wiki)note    |                           | story[#](#wiki-goog)  |    fact[#](#wiki-subt)    |
| **goog** |   [#](#coca-goog)web    |  [#](#norv-goog)info   |    [#](#twit-goog)site    |    [#](#wiki-goog)sale    |                       |    file[#](#goog-subt)    |
| **subt** |   [#](#coca-subt)tell   |  [#](#norv-subt)call   |   [#](#twit-subt)drama    |  [#](#wiki-subt)feeling   | [#](#goog-subt)chatty |                           |

---

#### coca-norv

> wo unidentified yeah mr clinton ca iraq saddam bush ok kids guys dr iraqi inc tonight larry atlanta hussein guy gore

> s fig de vol lord labour x cent chapter shall o und y god centre der anti pre b appendix op

---

#### coca-twit

> percent toward began iraq soviet seemed iraqi bush programs environmental ca correspondent studies wo although moreover nodded

> trump u cant im ive fuck porn wont isnt youre fucking pussy youtube shes shit thats id x uk ass facebook o s heres bitch th anti yo wouldnt pre via ya whos dude followers couldnt wasnt t y fake check sa youve n ex whats anal videos cute kinda download hate info theres update awesome nude labour nah cock damn god google miss congratulations ill racist theyre mueller suck putin follow honestly com email streaming posting deserve click thread blog lord fr trans eu allah stan hd rip sucks weve please birthday watch stats wow love wa amazing bullshit excited blessed til w cos bless chat re centre alright video

---

#### coca-wiki

> yeah yes maybe you thank ok think ca says oh your unidentified really sure thing we know myself why somebody me guess my everybody yourself sorry guys yesterday something want talking knew anybody kids ago our shook lot looked tonight say anything stuff things clinton eyes absolutely certainly tell else gotten here doing saddam seemed looks mom percent pretty anyway hey nobody hi whatever mean bush nothing tomorrow everything obviously going moment looking npr nice ask what hear please door getting mr do might donaldson trying kind ourselves happen ought walked

> centre de railway album uk township located genus km census featured theatre released league refer founded regiment royal award australian county competed district defeated fort squadron labour born debut appointed wales recorded university province played following club named kingdom awards cricket served aired awarded melbourne singles saint academy october river february borough matches lord australia festival division avenue hosted august bbc median mount village championship december due episode junction notable january won republic championships zealand november institute castle formed emperor infantry brigade september

---

#### coca-goog

> wo unidentified mr clinton says yeah knew nodded toward seemed herself stared shook republicans stood everybody

> x email click info ebay re s pm download copyright uk web n directory shipping posted y online reserved reviews dvd z search links forums password o contact user t listing archive forum e page subscribe edit website u mar posts porn server de centre blog jan hotels updated c privacy reply powered accessories b pdf advertise poker id thread zip register post anal ie seller pussy url item pre google mail hosting rentals listings date d p compare link fax q site r isbn f nude mon cd m index cart tx teen browser anti file quote en map archives gallery fl hp java rating mobile incest mailing k sub chat comments software update blogs submit newsletter free profile dvds travel check tel ltd mini select sorted printer ar com sellers review releases cock g registered os h accommodation sa mi nc sony address updates feedback product inn add logo wa code lyrics shopping calendar navigation ne pc ny payment print est auctions null usa description photo

---

#### coca-subt

> ca wo clinton participants percent programs economic democrats unidentified environmental republicans officials cnn students factors consumers democratic administration bush development significantly researchers toward iraq political republican congress iraqi vs education organizations groups rates institutions significant strategies curriculum variables communities gon growth cultural ethnic atlanta national attitudes policies gore legislation companies responses economy largely schools educational areas social studies individuals saddam teachers author senate washington

> don uh bye haven fuck alright um fucking sighs okay em hurry whoa dude mmm ooh huh grunts ma lord excuse hmm sir god eh y hey damn majesty goodbye shut miss you o papa darling bitch shit cheers cos hello er dare forgive swear bastard wait doc ya ah asshole idiot aw congratulations dear beg sweetie grandma daddy kidding calm yo ha till s nah mommy outta bullshit listen yep crap screw ass please sorry buddy colonel fuckin relax mama lieutenant mummy babe dad bet wow suck drink ringing hi

---

#### norv-twit

> fig thus considerable obtained observed therefore upon latter chapter variable characteristics structure et indicated moreover der however regarded surface provisions object nevertheless methods method cent although derived shall equation literature factors ii particular relation examination subsequent remained described sufficient manner functions instance function subject proportion various processes density vessels generally vol occur occurs output studies established und principle forms general extent velocity composition among began necessary doctrine readily subjects frequency observations distribution containing thereby formation measurement large procedure regard elements respectively examined effect frequently relatively experimental

> dont cant im fuck shit fucking gonna ur cute wow videos gotta bitch fake video ass guys awesome amazing wont album yo fans hey lets ya birthday u dm http teen stan congratulations tonight vs nude bc info thank ht weekend hate racist ok honestly yeah damn please via download weird xxx rn fan win pm ig hello super anymore kids thanks guy literally funny mom boyfriend tomorrow update fun tickets suck ji photos hi bout email website okay crazy movie streaming watch amazon annoying disgusting football etc trash app deserve debut stupid gym happy dumb likes aug followers girlfriend everyone sorry rip www posting sad wh online biggest rt chat idiot reminder winner someone rap favorite fbi episode dj hurts movies celebrate proud pizza hiring liked watching nice idol af check kid babe wins trailer friday swear bio wait th team excited mv hopefully stuff today rep dick celebrating democrats game hug gorgeous w updates vote gaming stop uk mad song tag bet soccer posted listen joke

---

#### norv-wiki

> fig shall self your non anti our you we chapter know me cent myself think re thou ought my yes pre et say suppose vol ourselves thy might

> album championship debut football released tournament season featured league municipality awards hockey team won stadium games film award medal club renamed scored career player located played basketball song featuring episode teams awarded champions br festival bbc coach game born st band station video census currently guitar township cricket matches soccer surname district cup inc studio olympic airport fc tour named website actress wrestling uk australian winner players titled athletics county jr

---

#### norv-goog

> himself ibid thus fig

> info pm email online download jan website posted privacy search click hotels teen web poker accessories reviews video forum sep jul links videos oct copyright password listings url linux nov site feb shipping photos dec aug page nude advertise news apr jun archive movies shopping cart rating logo posts contact powered games software listing zip wed casino subscribe eur lyrics buy uk directory photo updated phones newsletter comments reserved pc please internet audio sports mail trademarks chat teens thread cd electronics hp html az user digital tickets tx item quote keywords jewelry map hotel inc album mar message toys amazon fax phone incest profile eg seller tech update wireless usa browser updates announcements movie gallery microsoft link kb sellers keyword travel items mb releases fucking cds feedback www mailing upgrade dev edit store re mobile vegas auto mon featured xxx cameras golf gay lesbian paperback automotive searches xml add tips dj free mini desktop shop tv date calendar gaming list ie clips ads brands networking apparel rental latest home register

---

#### norv-subt

> fig latter thus development economic et chapter factors processes obtained non derived various anti growth ii defined however distribution variables observed subsequent increased generally social pre characteristic output analysis associated cent individual frequently iii method per characteristics doctrine values institutions consequently therefore states requirements der upon examples political agricultural self function value extent structure contrast considerable described similarly readily required income groups und university organizations largely functions regarded methods index rates data authors studies established quoted example length emphasis existing categories introduction journal reduction de large education among continued addition conditions proportion ratio provided consists volume its educational summary external management attitudes persons effect relation which publication observations concepts co

> don gonna yeah uh hey okay huh gotta hello fuck fucking wow shit guys sighs ok you sorry oh bitch laughs um mom dad guy haven thank goodbye cute tonight hi buddy bye damn anymore idiot girlfriend weird congratulations crazy boyfriend kid mum eh please bastard cops nice awesome won scared daddy cheers ass ya excuse thanks tomorrow hurry sweetheart cop wait yo maybe stupid listen grandpa funny apologize darling honey ls worry aw kill swear bet boss hell yes mister danny somebody screams ah killer stuff cheering guess grab screaming hurts bucks grandma lied fake madam amazing kids goin relax lucky chef i shoot anyway detective suck screwed em liar anybody babe joking shut hang aye everybody forgive birthday stole fun jerk l luck pal charlie panting hate disgusting mama stop forgot laughing mess kick eddie yelling tommy yours marty pizza scare ringing talking kiss bother knock phone baby hurt pants worried steal nobody got bike

---

#### twit-wiki

> im trump shit fuck thank ass please gonna wanna your bitch you porn damn yeah guys wow sorry me hi my yourself ok twitter hey yesterday hate deserve yes mom awesome tomorrow lets check maybe yo guess why want myself think th amazing really ya oh sure glad know tonight stupid happy anti wait sad excited imagine forget remember everyone yours dumb listen sexy info putin liked feel thanks proud thing fake nice bless lil click dear anymore crying pre swear appreciate stuff dad watch hello tired our say pretty watching deserves racist anyone we definitely smile tell funny talking weird reminder kids id look someone nude govt ill absolutely rt hear fun nobody am hope af looks ask thread follow tf lovely getting wrong scared worry wish get let em crazy re laugh birthday literally everything app somebody guy hillary doing need hell followers anything trash cry pray sex update looking enjoy shame aug happening how got something ugly happen reply sleep laughing likes going ready anyway else lately wonder cool loving hurt here understand wonderful mad remind bad self just closet welcome rip awful talk ridiculous scary everybody nothing trying anybody buy luck joke teen cares anal beautiful excuse expect non mean hiring chat eat bunch love things mccain whoever realize lot shout thinking dem loved grab incredible babe bet knows wants feeling agree mess stop quote favorite stan ignore try streaming horrible tickets ago ignorant wit forever truly daddy ji grateful keep listening bjp baby believe pretend genuinely do complain bored emails always sick

> census located february january began december founded april species population median township became district established university remained village railway biography notable parish density operated situated television province formed households march river served approximately renamed however originally known formerly described railroad administrative several october appeared century division association included born county commonly aircraft constructed returned although region william initially metres produced ii including respectively battalion lieutenant later subsequent incorporated appointed consists naval continued various geography soviet station primarily awarded institute refer noted november northern include developed metropolitan composed named united emperor buildings contains studied additionally states recorded championships borough surname film demographics performed area addition derived represented settlement eastern municipal royal transferred which built references numerous expedition route acquired east appearances fleet formation succeeded council national cemetery german thus released starred designated command previously structure units north during career championship regarded zealand footballer

---

#### twit-goog

> trump hes dont ive cant im didnt doesnt isnt theres shit followers thats omg gonna lol wanna ppl wont literally pls tho ur bro putin bitch honestly racist gotta liked ill fake congrats wtf hate deserve damn excited whats crying sad comeback mueller gop cuz crypto dm swear bullshit playlist mccain dems tonight bitches dude fuck https fuckin ig stan tomorrow rts okay lets hillary amazing yo woke fam haha guys dumb proud govt watching cute ji deserves happy bout likes plz congratulations fav anymore kinda ya thank todays tired birthday hey wait thankful scared app wow someone everyone jin imagine bless genuinely fucking yeah pathetic stupid liar boyfriend democrats ht fans cry lil everytime saying hurts

> copyright directory search jan reserved web hotels forums fax yahoo site apr privacy january software dvd index page categories links login information reviews forum user poker item contact browse url rentals electronics cart accessories mail html cd dec ebay map downloads seller feb navigation archive services view product items file description listings computers eur products rating keywords linux listing cnet subject publications pages nokia archives advertise february contents password printer december advanced mailing kb select catalog interface disclaimer database format dvds availability modified systems telephone pdf rss eg equipment email accommodation category hardware terms section oct lcd management sites variable domain click ipod manufacturer searches hotel mar resources computer components price inn nov publisher gallery sellers files tools prices tue requirements estate overview output pm compare thu java newsletter

---

#### twit-subt

> lol trump im ive youre dont hes cant twitter ur tweet didnt vs thats via theres u bc pic anti pre democrats ht followers app youtube w videos ft uk eu niggas wont whats streaming mueller haha liberals obama porn video teen republicans lil hardcore added update ny july trans bs fr etc cnn democrat nigga racism nude co humidity fans album iphone non nba stats racist hillary hype stream bias bio pm hoe media porno thread usa iconic updates sm supporters download cuz

> didn isn doesn don haven sighs ain lieutenant uh colonel whoa sergeant narrator majesty madame ln ooh gentlemen l ringing mmm um detective huh madam lt upstairs laughs ow applause announcer darling hurry

---

#### wiki-goog

> became won played born debut later municipality league railway began founded named defeated notable politician championship released renamed season known served genus squadron village appeared championships remained former regiment medal appearances died aired population elected formed album subsequently billboard career appointed scored located eventually station moved graduated species emperor promoted province soviet early opened during infantry married century constituency army

> click info ebay re email please pm page your privacy search copyright web contact password item directory add buy reply forums yahoo cart porn reserved thread you jan compare hotels accessories comments oct dec nov aug our seller check quote message am mail non feb download downloads price shipping online photo wed my jun posts yes feedback send pre teen mon user ass posted anti forum prices nude map view items hi discount poker newsletter mailing we customer pages comment ok edit links phone photos az here tx free pdf sellers sex chat id index multi tips file topic blog profile anal nokia news details cheap auctions product printer fi read sexy mar information xml address server listings kb menu welcome pc shall php ipod mb thank html shopping submit jewelry select payment zip stuff log update me browser us date link reviews fuck gifts teens announcements find th toys mortgage apparel archive dev rating searches xp usb software logged motorola dvd products spam guide

---

#### wiki-subt

> located album featured january population february october september december university november founded district subsequently included include series league debut published including july county national championships season august united released awarded international established june province biography during states australian development championship uk awards railway format situated features rural association st march appointed refer includes produced consists announced regional administrative various historic region former districts originally april however stated its also ii singles canadian continued elected initially northern featuring award density species formerly zealand commonly division latter became described primarily subsequent several ranked currently addition formed served career participated european albums widely following attended numerous km member began education australia south rugby operated derived programs netherlands performed century represented southern areas constructed western contemporary composed references eastern pennsylvania remained british recorded associated approximately versions expanded largely sciences state listed played north scoring noted municipal institute football typically election title wales referred publication based borough provides organizations which resulting members resulted scored prominent parliament american production communities born edition appeared overall version de vocals by schools largest canada west aircraft area central olympics incorporated average additional episodes conservation received film known adjacent geography launched via refers br males premier soundtrack consecutive parish billboard appearances tournament generally held replaced developed academic east guitarist assembly completed ireland between historical bc feature history city independent females titles seasons services universities provincial income agricultural economic

> you yeah gonna oh hey sorry yes thank don ok shit please hi maybe fuck hello your me mom damn know guys dad ain wanna excuse yourself worry guess wow yours sure ah wait bitch think listen my ass nice want tomorrow em why tell we somebody let stupid laughs glad scared forget myself anyway yesterday anybody dear remember bastard tonight forgive swear anymore everybody here daddy relax stuff laughing really what afraid look bye thing anything talking mean hell cops hear nobody thanks haven pretty ask guy wrong cheers crazy gentlemen say darling lovely ya weird got suppose everything fool understand something doing hurt kid awesome awful else sit honey hate dare feel talk do crying hang grab goodbye nothing tired happen yo apologize ringing funny screaming hungry ridiculous sweetheart get happened whatever appreciate imagine figured come deserve calm go worried careful silly nonsense absolutely smell eat beg happening laughter bet mama drink mess going laugh looks knows luck check welcome screams pretend definitely am upstairs talked wonderful cop shut ourselves dumb lately somewhere whoever shouting ready er happy lucky buddy sleep horrible bless bit ha knew lied breathe sake kids terrible sick happens majesty exactly knock expect pity gotten remind thinking asleep anyone bunch fix everyone believe surely wish baby right fault bathroom shame rid honest waiting sooner lot amazing scary mistake dinner promise pull fun cares stay slept wants pardon cool need looking stop smile getting papa try our pants babe bag drunk mister quiet phone obviously trouble how ought someone sad ladies thinks joke wonder bad kill kind telling worse admit busy ago gone supposed mad awake scare everywhere shall door cry fine boss shower things proud mind checked highness stole blame bloody totally mummy trying lunch loved bucks pills shoot boring asking anywhere answer just sort ate bed

---

#### goog-subt

> copyright ebay user pm reviews web directory email links page forum click categories index info products software listing site rating online jan accessories x comments yahoo posts hotels services uk download items reserved shipping format users search january product dvd privacy review pc topics usa view website mar prices sony posted management archive item policy category updated ny teen feedback sites seller development digital server select powered non resource pre information blog data e requirements available ca summary contact sellers cd features advertise rates c solutions edit anti hosting applications featured n re programs thread b articles pages r post reply md audio rated electronics p w author add java ie rights resources health incest fax content topic domain international free compare sponsored price archives v provides december additional include link accommodation policies mail wireless ip design releases description gallery related education listed default co includes version edition printer consumer interface technologies authors map k publication logo university network offers marketing ibm catalog brands teens previous systems internet application profile terms websites register f announcements guides updates searches stores tools z advanced ft tel november service password manufacturer quotes navigation retail guidelines rd by entries regional canada february google wed networks vs output news nude statistics fitness settings october quote abstract sports loans documentation provided cart list provider anal inc overall video activities canon research components guide details journal county technology integrated g reference results current installation section outdoor jun ltd finance h hardware manufacturers environmental sciences sales program developer update pic organizations ratings courses lyrics member required september database comprehensive bondage videos dvds submit recommendations contents wholesale title games existing calendar community payment

> don okay uh gonna yeah huh hey ooh sir excuse hurry gotta laughs alright dad kidding haven wanna sorry oh gentlemen um bastard mmm won darling hmm shit forgive scared bye swear madam marry you damn narrator ah goodbye worry happened shut somebody afraid laughing sweetheart ow shouting wait kill applause hell bullshit fuckin anymore uncle upstairs idiot mum ringing hello pardon honey owe dude everybody lieutenant screaming bitch yep tomorrow hurt tonight cops crying beg stole guys worried lied sergeant calm eh daddy asshole colonel anybody apologize mommy jealous nobody maybe mom detective boyfriend mama mister sit supposed thank ruined downstairs killed guy murdered liar come ridiculous bloody aunt stupid telling majesty slept knocking fool laughter bro cop upset talking lying hang father kid girlfriend ashamed hungry hurts got goin shoot grandma dare bother guess asleep smell crazy knock nope terrible knew sake dear boss madame listen mess hiding clears whoever careful told pretend brother nonsense forget mean yourselves congratulations alive tell let knows talked tired lie captain breathe promise mistake screwed nothing cousin anything glad thinks pity relax sick doing fault wrong anyway figured hear broke weird lucky yours papa ruin thief eat jail sing husband miss smells guts pissed happen
