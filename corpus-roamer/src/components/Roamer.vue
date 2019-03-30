<template>
  <div class="hello" onblur="window.focus();">
    <div style="position: absolute; left: 50%; width:100%; height:150%;">
      <iframe :src="iframe_src" class="word-image" frameborder="0" allowtransparency="true"></iframe>
    </div>
    <!-- <h3>{{msg}}</h3> -->
    <!-- <p>
      Press
      <code>J</code> and
      <code>K</code> to go up and down; Press
      <code>SPACE</code> to toggle auto scroll.
    </p>-->
    <div>
      <input type="number" v-model="cursor" :max="WL_size" min="-1" step="1">
      <button @click="speakStemWords(cursor, sayingPi)">{{ sayingPi ? 'Stop' : 'Start' }}</button>
      <button @click="speakPi(cursor, sayingPi)">{{ sayingPi ? 'Shut up' : 'Say pi' }}</button>
      <input type="text" v-model="search" placeholder="search" @change="searchWord()">
    </div>
    <ul>
      <li v-for="(w,i) in word_list" :key="i" :id="`word-list-${i}`">
        <div id="word-list">
          <a
            :href="'https://www.google.com/search?tbm=isch&tbs=itp:clipart&q='+w.word"
            target="_blank"
          >
            <span
              :class="{ 'current-cursor': (cursor<c_offset ? cursor==i : i==c_offset)}"
              v-show="cursor>=0"
            >
              <!-- <span v-show="cursor>0" class="cursor">{{ cursor }}</span>
             圆周率 π 第{{(word-1)*10000+1}} ~ {{ (word) * 10000 }}位 -->
              <span v-show="cursor>6" class="cursor">{{ cursor-6 }}</span>
              {{ typeof wl[cursor] == 'string' ? wl[cursor] : wl[cursor].word }}
            </span>
          </a>
          <div v-if="(cursor<c_offset ? cursor==i : i==c_offset)">
            <div v-if="true && cursor>6" id="for-general-corpus-roaming">
              <div>
                <p v-show="false" class="def-lang">
                  <!-- <span class="def-label">[FR]</span> -->
                  {{ translation[w.word]['ja'] || ' ' }}
                </p>
                <p class="def-lang def-zh">
                  <!-- <span class="def-label">[中]</span> -->
                  {{ translation[w.word]['zh'] || ' ' }}
                </p>
                <p v-show="false" class="def-lang">
                  <!-- <span class="def-label">[DE]</span> -->
                  {{ translation[w.word]['de'] || ' ' }}
                </p>
              </div>
              <div v-if="true">
                <div>
                  <p class="def-lang def-us">
                    <!-- <span class="def-label">[DEF]</span> -->
                    {{ translation[w.word]['us'] != w.word ? translation[w.word]['us'] : ' ' }}
                  </p>
                </div>
                <div v-show="translation[w.word]['gre']">
                  <p class="def-lang def-gre">
                    <span class="def-label">[GRE]</span>
                    {{ translation[w.word]['gre'] || ' ' }}
                  </p>
                </div>
                <div v-show="translation[w.word]['tfl']">
                  <p class="def-lang def-gre">
                    <span class="def-label">[TOEFL]</span>
                    {{ translation[w.word]['tfl'] || ' ' }}
                  </p>
                </div>
                <div v-show="translation[w.word]['ils']">
                  <p class="def-lang def-gre">
                    <span class="def-label">[IELTS]</span>
                    {{ translation[w.word]['ils'] || ' ' }}
                  </p>
                </div>
              </div>

              <table v-if="false" id="for-multilingual">
                <tr>
                  <td>{{ translation[word]['zh'] || word }}</td>
                  <td>{{ translation[word]['fr'] || word }}</td>
                  <td>{{ translation[word]['hi'] || word }}</td>
                </tr>
                <tr>
                  <td>{{ translation[word]['ja'] || word }}</td>
                  <td>{{ translation[word]['es'] || word }}</td>
                  <td>{{ translation[word]['bn'] || word }}</td>
                </tr>
                <tr>
                  <td>{{ translation[word]['ko'] || word }}</td>
                  <td>{{ translation[word]['pt'] || word }}</td>
                  <td>{{ translation[word]['ar'] || word }}</td>
                </tr>
                <tr>
                  <td>{{ translation[word]['vi'] || word }}</td>
                  <td>{{ translation[word]['it'] || word }}</td>
                  <td>{{ translation[word]['tr'] || word }}</td>
                </tr>
                <tr>
                  <td>{{ translation[word]['ms'] || word }}</td>
                  <td>{{ translation[word]['de'] || word }}</td>
                  <td>{{ translation[word]['ru'] || word }}</td>
                </tr>
              </table>
            </div>

            <div v-if="true && cursor>6" id="for-stem-corpus-roaming">
              <table v-if="word_stem[w.stem]">
                <div
                  v-for="(morph, index) in word_stem[w.stem].slice(0,max_morph(word_stem[w.stem]))"
                  :key="`${Object.keys(morph)[0]}_${index}`"
                >
                  <tr>
                    <td class="stem-lang">{{Object.entries(morph)[0][0]}}</td>
                    <td class="stem-lang stem-zh">{{Object.entries(morph)[0][1]}}</td>
                    <td
                      v-if="index+max_morph(word_stem[w.stem])<word_stem[w.stem].length"
                      class="stem-lang"
                    >{{Object.entries(word_stem[w.stem][index+max_morph(word_stem[w.stem])])[0][0]}}</td>
                    <td
                      v-if="index+max_morph(word_stem[w.stem])<word_stem[w.stem].length"
                      class="stem-lang stem-zh"
                    >{{Object.entries(word_stem[w.stem][index+max_morph(word_stem[w.stem])])[0][1]}}</td>
                    <td
                      v-if="index+max_morph(word_stem[w.stem])*2<word_stem[w.stem].length"
                      class="stem-lang"
                    >{{Object.entries(word_stem[w.stem][index+max_morph(word_stem[w.stem])*2])[0][0]}}</td>
                    <td
                      v-if="index+max_morph(word_stem[w.stem])*2<word_stem[w.stem].length"
                      class="stem-lang stem-zh"
                    >{{Object.entries(word_stem[w.stem][index+max_morph(word_stem[w.stem])*2])[0][1]}}</td>
                  </tr>
                </div>
              </table>
            </div>

            <div v-if="false" id="for-zhCN-pi-million-roaming">
              <img id="pi-talk-img" src="../assets/pi-talk.gif" alt="pi">
              <table>
                <tr>
                  <td>
                    <p id="speech-content" class="def-us">
                      <span id="speech-tracker" class="trail"></span>
                      <span v-for="(c,j) in word_dict[word]" :key="j" class="pi-block">
                        <span class="pi-digits">{{pi[word].substr(10*j,10)}}</span>
                        {{ c }}
                      </span>
                    </p>
                  </td>
                </tr>
              </table>
            </div>

            <div v-if="false && cursor >= 0" id="for-animal-names-roaming" style="margin-top: 1em;">
              <span class="def-us">{{ translation[wl[cursor]]['es'] }}</span>
              <span class="def-us">{{ translation[wl[cursor]]['zh'] }}</span>
              <span class="def-us">{{ translation[wl[cursor]]['fr'] }}</span>
              <span class="def-us">{{ translation[wl[cursor]]['ja'] }}</span>
              <span class="def-us">{{ translation[wl[cursor]]['de'] }}</span>
              <div v-for="(group, k) in word_stem[wl[cursor]]" :key="k" class="def-us">
                <p v-if="k>0">
                  {{ (group).match(/^[aeiou]\w+/) ? 'an':'a'}}
                  <span
                    style="color:#9c27b0;font-weight:900;"
                  >{{ group }}</span>
                  of {{ word_stem[wl[cursor]][0] }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import PI from "../assets/pi-digit.json";
import WL from "../assets/word_list_lemma.json";
import STEM from "../assets/word_stems_zh.json";
import TRAN from "../assets/word_list_tran.json";

export default {
  name: "Roamer",
  props: {
    msg: String
  },
  data() {
    return {
      pi: PI,
      wl: WL,
      word_stem: STEM,
      stems: Object.keys(STEM),
      translation: TRAN,
      c_offset: 0,
      WL_size: 41295,
      cursor: 0,
      speakMsg: new SpeechSynthesisUtterance(),
      autoScroll: null,
      sayingPi: false,
      search: "",


      // Speech voices
      en_male: [],
      en_female: [],
      zh_female: []
    };
  },
  computed: {
    word_list: function() {
      const start =
        this.cursor > this.c_offset ? parseInt(this.cursor) - this.c_offset : 0;
      return this.wl.slice(start, parseInt(this.cursor) + 1);
    },
    iframe_src: function() {
      let word = this.word_list[this.c_offset];

      word = word.word ? word.word : word;
      // if (this.cursor <= 7) return "";
      // word = this.first_morph(word);
      // word = this.word_stem[w.stem][0];

      return "https://pixabay.com/en/photos/" + word;
      return "https://www.stockvault.net/free-photos/" + word;
      return "https://www.pexels.com/search/" + word;
    }
  },
  mounted() {
    this.speakMsg = new SpeechSynthesisUtterance();
    this.speakMsg.voice = speechSynthesis.getVoices()[32];

    window.addEventListener("keypress", e => {
      switch (e.keyCode) {
        case 44:
          if (this.cursor > 0) {
            this.cursor--;
            // this.speakStemWords(this.cursor);
          }
          break;
        case 46:
          if (this.cursor < this.WL_size) {
            this.cursor++;
            // this.speakStemWords(this.cursor);
          }
          break;
        case 39:
          this.en_male = [
            // speechSynthesis.getVoices()[7], // Daniel
            // speechSynthesis.getVoices()[32], // Samantha US
            speechSynthesis.getVoices()[0] // Alex
            // speechSynthesis.getVoices()[50], // UK male
            // speechSynthesis.getVoices()[17], // Karen AU
            // speechSynthesis.getVoices()[48], // US female
          ];
          this.en_female = [
            // speechSynthesis.getVoices()[10], // Fiona UK
            // speechSynthesis.getVoices()[28], // Moria IE
            // speechSynthesis.getVoices()[36], // Tessa ZA
            // speechSynthesis.getVoices()[39], // Veena IN
            // speechSynthesis.getVoices()[40], // Victoria US
            speechSynthesis.getVoices()[17], // Karen AU
            speechSynthesis.getVoices()[32], // Samantha US
            speechSynthesis.getVoices()[48], // US female
            speechSynthesis.getVoices()[49] // UK female
          ];
          this.fr_female = [
            speechSynthesis.getVoices()[3], // Amelie ca-FR
            speechSynthesis.getVoices()[53] // google FR
          ];
          this.zh_female = [
            speechSynthesis.getVoices()[25], // Meijia TW
            // speechSynthesis.getVoices()[35], // Sinji HK
            // speechSynthesis.getVoices()[38], // Tingting CN
            speechSynthesis.getVoices()[63], // CN
            // speechSynthesis.getVoices()[64], // HK
            speechSynthesis.getVoices()[65] // TW
          ];
          // this.speakWord(this.cursor);
          break;
        case 32:
          this.speakMsg.voice = speechSynthesis.getVoices()[32];
          this.toggleAutoScroll();
          break;
        default:
          speechSynthesis.cancel();
          break;
      }
    });
  },
  methods: {
    toggleAutoScroll() {
      if (this.autoScroll) {
        clearTimeout(this.autoScroll);
        this.autoScroll = null;
      } else {
        this.loop();
      }
    },

    loop() {
      const word = this.wl[++this.cursor];

      let timeout = this.word_stem[w.stem].reduce((acc, mor) => {
        return acc + Object.keys(mor)[0].length * 50 + 450;
      }, 4700 + word.length * 50);

      // this.speakWord(this.cursor);
      this.speakStemWords(this.cursor);

      this.autoScroll = setTimeout(this.loop, timeout);
    },

    speakWord(index) {
      // Delay showing word list to wait iframe refresh
      // document.getElementById("word-list").classList.add("hide");

      const word = WL[index];

      // Delay speech to wait iframe refresh
      setTimeout(() => {
        // document.getElementById("word-list").classList.remove("hide");
        // this.speakMsg.voice = this.en_male[
        //   Math.floor(Math.random() * this.en_male.length)
        // ];
        this.speakMsg.text = word;
        speechSynthesis.speak(this.speakMsg);
        // setTimeout(() => {
        //   if (this.translation[word]) {
        //     this.speakMsg.voice = this.fr_female[
        //       Math.floor(Math.random() * this.fr_female.length)
        //     ];
        //     this.speakMsg.text = this.translation[word]["fr"] || word;
        //     speechSynthesis.speak(this.speakMsg);
        //   }
        //   setTimeout(() => {
        //     if (this.translation[word]["zh"]) {
        //       this.speakMsg.voice = this.zh_female[
        //         Math.floor(Math.random() * this.zh_female.length)
        //       ];
        //       this.speakMsg.text = this.translation[word]["zh"];
        //       speechSynthesis.speak(this.speakMsg);
        //     }
        //     setTimeout(() => {
        //       if (this.translation[word] && this.translation[word]["us"]) {
        //         this.speakMsg.voice = this.en_female[
        //           Math.floor(Math.random() * this.en_female.length)
        //         ];
        //         this.speakMsg.text = this.translation[word]["us"];
        //         speechSynthesis.speak(this.speakMsg);
        //       }
        //     }, 2000); // us
        //   }, 1500); // zh
        // }, 700); // fr
      }, 0); // word
    },

    speakStemWords(index, stop) {
      if (stop) {
        this.sayingPi = false;
        speechSynthesis.cancel();
        return;
      }
      this.sayingPi = true;
      this.cursor = index;

      const stem = this.wl[index].stem;
      // Delay showing word list to wait iframe refresh
      document.getElementById("word-list-0").classList.add("hide");

      setTimeout(() => {
        document.getElementById("word-list-0").classList.remove("hide");
        this.speakMsg.voice = speechSynthesis.getVoices()[8];
        const word = this.wl[index].word;
        this.speakMsg.text = word
        speechSynthesis.speak(this.speakMsg);
        this.speakMsg.onend = () => {
          this.speakMsg.voice = speechSynthesis.getVoices()[40];
          if (this.word_stem[stem]) {
            this.speakMsg.text = (!!this.translation[word] && !!this.translation[word]['us']) ? this.translation[word]['us'] : '';
            this.speakMsg.text += this.word_stem[stem].reduce((acc, mor) => {
              return acc + Object.keys(mor)[0] + ", ,";
            }, ", ");
          }
          speechSynthesis.speak(this.speakMsg);

          this.speakMsg.onend = () => {
            this.speakStemWords(Math.floor(Math.random()*this.WL_size+7), !this.sayingPi);
          };
        };
      }, 500);
    },

    speakPi(index, stop) {
      if (stop) {
        this.sayingPi = false;
        speechSynthesis.cancel();
        return;
      }

      this.sayingPi = true;
      this.cursor = index;

      this.speakMsg.text = this.word_dict[index];
      this.speakMsg.voice = speechSynthesis.getVoices()[index > 6 ? 40 : 8];
      speechSynthesis.speak(this.speakMsg);
      this.speakMsg.onend = () => {
        setTimeout(() => {
          this.speakPi(+index + 1, !this.sayingPi);
        }, 200);
      };
    },

    speakAnimal(index, stop) {
      if (stop) {
        this.sayingPi = false;
        speechSynthesis.cancel();
        return;
      }
      this.sayingPi = true;
      this.cursor = index;
      // Delay showing word list to wait iframe refresh
      document.getElementById("word-list-0").classList.add("hide");

      setTimeout(() => {
        document.getElementById("word-list-0").classList.remove("hide");

        const groups = this.word_dict[this.wl[index]].slice(1);
        const animals = this.word_dict[this.wl[index]][0];
        this.speakMsg.voice = speechSynthesis.getVoices()[14];
        this.speakMsg.text = groups
          .map(g => `${g.match(/^[aeiou]\w+/) ? "an" : "a"} ${g} of ${animals}`)
          .join(", ");
        speechSynthesis.speak(this.speakMsg);
        this.speakMsg.onend = () => {
          setTimeout(() => {
            this.speakAnimal(+index + 1, !this.sayingPi);
          }, 1000);
        };
      }, 2000);
    },

    searchWord() {
      const findIdx = WL.findIndex(w => w === this.search);
      this.cursor = findIdx >= 0 ? findIdx : this.cursor;
    },

    first_morph: function(stem) {
      return Object.keys(WL[stem][0])[0];
    },

    max_morph: function(morphs) {
      const len = morphs.length;
      if (len < 10) {
        return len;
      } else if (len < 20) {
        return Math.ceil(len / 2);
      } else {
        return Math.ceil(len / 3);
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
  margin-top: 10px;
}
li {
  display: inline-block;
  margin: 10px auto;
  font-size: 150%;
  font-size: 120%;
  border-color: #009688;
  /* max-width: 60%; */
  background: #fafafadd;
  border-radius: 0.2em;
  box-shadow: 0px 0px 40px 20px #fafafadd;
}
table {
  table-layout: fixed;
  /* width: 60%; */
  margin: 10px auto;
  padding-bottom: 50px;
}
td {
  min-width: 7em;
  /* max-width: 12em; */
  max-width: 300px;
  height: 1.2em;
  /* width: 50%; */
  overflow: hidden;
  padding-bottom: 500px;
  line-height: 4em;
}
a {
  color: #2c3e5088;
  text-decoration: none;
}
.current-cursor {
  color: #009688;
  color: #EF9A9A;
  font-size: 400%;
  font-weight: 700;
  font-family: "avenir next";
  padding: 0.2em 1em;
  z-index: 1;
}
.cursor {
  color: #67c79c44;
  font-size: 50%;
  font-family: "menlo";
  position: absolute;
  left: 15%;
  top: 10%;
}
.def-lang {
  display: inline-block;
  font-size: 160%;
  font-weight: 500;
  font-family: "roboto";
  color: #42b983;
  margin: 10px auto;
  padding: 0.1em 0.5em;
  max-width: 1000px;
  /* background: #fefdfdef; */
  /* border-radius: 0.2em; */
  /* box-shadow: 0px 0px 40px 20px #fefdfdef; */
  z-index: 1;
}
.def-us {
  font-size: 200%;
  font-family: 'DFKai-SB', 'KaiTi';
  font-weight: 600;
  font-size: 130%;
  color: #2c3e5066;
}
.def-zh {
  font-size: 180%;
  font-weight: 700;
  font-family: "Hannotate SC";
  color: #607D8B;
}
.stem-lang {
  font-size: 160%;
  font-weight: 500;
  text-align: right;
  color: #42b983;
  margin: 10px auto;
  padding: 0.1em 0.5em;
}
.stem-zh {
  font-size: 120%;
  font-weight: 700;
  font-family: "Hannotate SC";
  text-align: left;
}
.def-gre {
  font-size: 130%;
  color: #67c79b;
}
span.pi-block {
  display: inline-grid;
  padding: 0px;
  margin: 0px;
  width: 60px;
  max-height: 40px;
}
span.pi-digits {
  position: relative;
  top: 45px;
  font-size: 28%;
  font-family: 'consolas', Courier, monospace;
}
span.def-label {
  color: #67c79c77;
}
#word-list-0.hide {
  opacity: 0;
  transition: opacity 0s;
}
#word-list-0 {
  opacity: 1;
  transition: opacity 0.1s ease-out;
}
iframe.word-image {
  position: relative;
  top: -140px;
  left: -50%;
  /* margin: 0 auto; */
  z-index: -1;
  width: 85%;
  height: 100%;
  background: #f6f2f2 !important;
  opacity: 0.18;
}
div.footer {
  display: none;
}

/* animation show reading progress */
#speech-tracker {
  position: absolute;
  left: 85%;
  background-color: slategrey;
  width: 40px;
  height: 10px;
  display: block;
  top: -150px;
}
.move-shape {
  position: relative;
  animation: ani 299s 1 linear;
}

@keyframes ani {
  0% {
    top: 0px;
  }

  100% {
    top: -10000px;
  }
}

#pi-talk-img{
  position: relative;
  top: -50px;
  left: 0px;
  float: right;
}
</style>
