<template>
  <div class="hello">
    <!-- <h3>{{msg}}</h3> -->
    <p>
      Press
      <code>J</code> and
      <code>K</code> to go up and down; Press
      <code>SPACE</code> to toggle auto scroll.
    </p>
    <input type="number" v-model="cursor" :max="WL_size" min="-1" step="10">
    <button @click="toggleAutoScroll()">{{ autoScroll ? 'Stop' : 'Start' }}</button>
    <input type="text" v-model="search" placeholder="search" @change="searchWord()">
    <ul>
      <li v-for="(word,i) in word_list" :key="i">
        <a :href="'https://www.google.com/search?tbm=isch&tbs=itp:clipart&q='+word" target="_blank">
          <span :class="{ 'current-cursor': (cursor<c_offset ? cursor==i : i==c_offset)}">{{ word }}</span>
        </a>
        <div
          v-if="translation[word] && (cursor<c_offset ? cursor==i : i==c_offset)"
          class="translation"
        >
          <p class="def-us">{{ translation[word]['us'] || ' ' }}</p>
          <p class="def-zh">{{ translation[word]['zh'] || ' ' }}</p>
          <!-- <table>
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
          </table> -->
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import WL from "../assets/word_list.json";
import TRAN from "../assets/word_list_tran.json";

export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  data() {
    return {
      translation: TRAN,
      c_offset: 3,
      WL_size: 61420,
      cursor: 100,
      speakMsg: new SpeechSynthesisUtterance(),
      autoScroll: null,
      search: ""
    };
  },
  computed: {
    word_list: function() {
      const start =
        this.cursor > this.c_offset ? parseInt(this.cursor) - this.c_offset : 0;
      return WL.slice(start, parseInt(this.cursor) + 1);
    }
  },
  mounted() {
    window.addEventListener("keypress", e => {
      switch (e.keyCode) {
        case 44:
          if (this.cursor > 0) {
            this.cursor--;
            this.speakWord(this.cursor);
          }
          break;
        case 46:
          if (this.cursor < this.WL_size) {
            this.cursor++;
            this.speakWord(this.cursor);
          }
          break;
        case 39:
          this.speakWord(this.cursor);
          break;
        case 32:
          // this.speakMsg.voice = speechSynthesis.getVoices()[32];
          this.toggleAutoScroll();
          break;
        default:
          speechSynthesis.cancel();
          break;
      }
    });
  },
  methods: {
    speakWord(index) {
      const word = WL[index]
      this.speakMsg.text = word;
      this.speakMsg.voice = speechSynthesis.getVoices()[0];
      speechSynthesis.speak(this.speakMsg);

      setTimeout(()=> {
        if (this.translation[word] && this.translation[word]['us']){
          this.speakMsg.voice = speechSynthesis.getVoices()[32];
          this.speakMsg.text = this.translation[word]['us'];
          speechSynthesis.speak(this.speakMsg);
        }
      }, 200);


      setTimeout(()=> {
        if (this.translation[word] && this.translation[word]['zh']){
          this.speakMsg.voice = speechSynthesis.getVoices()[25];
          this.speakMsg.text = this.translation[word]['zh'];
          console.log(this.speakMsg.text);
          speechSynthesis.speak(this.speakMsg);
        }
      }, 1500);

    },

    toggleAutoScroll() {
      if (this.autoScroll) {
        clearTimeout(this.autoScroll);
        this.autoScroll = null;
      } else {
        this.loop();
      }
    },

    loop() {
      const word = WL[++this.cursor];
      let timeout = 0;
      if (this.translation[word]){
        const sentance = word + '... ' + this.translation[word]['us'] + this.translation[word]['zh'];
        timeout = 3000 + (sentance.length - 1) * 50 + this.translation[word]['zh'].length*100;
      } else {
        timeout = 1000 + (word.length - 1) * 50 ;
      }
      this.speakWord(this.cursor);
      this.autoScroll = setTimeout(this.loop, timeout);
    },

    searchWord() {
      const findIdx = WL.findIndex(w => w === this.search);
      this.cursor = findIdx >= 0 ? findIdx : this.cursor;
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
}
li {
  /* display: inline-block; */
  margin: 10px 10px;
  font-size: 150%;
}
table {
  width: 60%;
  margin: 30px auto;
  padding-bottom: 50px;
}
td {
  min-width: 8em;
  max-width: 8em;
  height: 2.2em;
}
a {
  color: #2c3e5096;
  text-decoration: none;
}
.current-cursor {
  color: #009688;
  /* color: #42b983; */
  /* color:#f7786b; */
  font-size: 400%;
  font-weight: 700;
}
.translation {
  font-size: 150%;
  font-weight: 500;
  color: #42b983;
}
.def-us {
  font-size: 100%;
  width: 60%;
  margin: 40px auto;
}
.def-zh {
  font-size: 120%;
  width: 60%;
  margin: 20px auto;
}
</style>
