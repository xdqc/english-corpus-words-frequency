const spk = new SpeechSynthesisUtterance();
const stopCode = 40935;
let prevText = '';
let stopSpk = false;
const CJK = [];

const speak_code = (currentCode, dontClick) => {
  if (!dontClick) {
    window.document.querySelectorAll('\[data-code="' + currentCode + '"\]')[0].click();
  }

  let wait = setTimeout(() => {
    const desc = document.getElementsByClassName('desc')[0].innerText;
    document.getElementsByClassName('desc')[0].style.display = 'None';
    console.log(desc);
    if (desc === 'loading ...') {
      clearTimeout(wait);
      speak_code(currentCode, true);
    } else {
      setTimeout(() => {
        const currText = document.getElementsByClassName('desc-en')[0].innerText
          .replace(/\([^\)]+\)/, '')
          .replace(/rad\. no\. \d+/, '')
          .replace(/GB radical \d+/, '')
          .replace(/KangXi radical number \d+/, '')
          .replace(/KangXi radical \d+/, '')
          .replace(/radical number \d+/, '')
          .replace(/rad\. no\. \d+/, '')
          .replace(/U\+\d+/, '')
          .replace(/kwukyel/, '')
          .split(' ');
        // document.getElementsByClassName('desc-en')[0].innerHTML = currText.slice(1, -1).join(' ');
        // document.getElementsByClassName('char')[0].style.width = '400px';
        // document.getElementsByClassName('vchar')[0].style['font-size'] = '108px';
        // document.getElementsByClassName('vchar')[0].style['font-family'] = '"DFKai-SB", "KaiTi"';
        // document.getElementsByClassName('desc-en')[0].style['color'] = 'hsl(' + Math.round(Math.random() * 360) + ', 50%, 50%)';
        // document.getElementsByClassName('desc-en')[0].style['font-size'] = '3em';
        // document.getElementsByClassName('desc-en')[0].style['line-height'] = '1.2em';
        // document.getElementsByClassName('desc-en')[0].style['margin-top'] = '-1em';
        if (document.getElementsByClassName('desc-en')[0].style.display !== 'none') {
          const toTop = document.getElementsByClassName('desc-en')[0].getBoundingClientRect().top + window.pageYOffset - 350;
          window.scrollTo({ top: toTop, behavior: 'smooth' });
          // let idx = 0;
          // while (idx < currText.length && currText[idx]!=='' && prevText[idx]===currText[idx]) {
          //     idx++;
          // };

          // spk.text = document.getElementsByClassName('vchar')[0].innerText;
          // spk.voice = speechSynthesis.getVoices()[20];
          // speechSynthesis.speak(spk);
          // spk.onend = () => {
            // spk.text = currText.slice(1, -1).join(' ');
            // spk.voice = speechSynthesis.getVoices()[0];
            // speechSynthesis.speak(spk);
            // spk.onend = () => {
            //   prevText = currText;
            //   if (!stopSpk && currentCode < stopCode) { speak_code(currentCode + 1); }
            // }
          // }
          CJK.push({
            code: document.getElementsByClassName('code')[0].innerText.replace('U+', ''),
            char: document.getElementsByClassName('vchar')[0].innerText,
            tran: currText.slice(1, -1).join(' '),
          });
        } 
        // else {
          prevText = currText;
          if (!stopSpk && currentCode < stopCode) { speak_code(currentCode + 1); }
        // }
      }, 20);
    }
  }, 20);
}
