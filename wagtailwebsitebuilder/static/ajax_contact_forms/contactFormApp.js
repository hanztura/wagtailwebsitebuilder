let contactForm = new Vue({
  name: 'ContactFormApp',
  el: '#contactForm',
  delimiters: ['[[', ']]'],
  data: () => {
    return {
      name: '',
      emailAddress: '',
      message: '',
      enableSending: true,
      recaptchaSiteKey: '6Ld5NuYUAAAAAEb02q1JOUauw5wA8faVagG0KN_G',
      recaptcha: '',
      recaptchaRequired: false,
      showThankYouModal: false,
      randomWords: [
        'offense',
        'choice',
        'voyage',
        'radiation',
        'to',
        'dynamic',
        'creation',
        'courtship',
        'sense',
        'cooperation',
        'serve',
        'lodge',
        'disappear',
        'slippery',
        'pray',
        'absolute',
        'sun',
        'rise',
        'flexible',
        'means',
        'coup',
        'taste',
        'pawn',
        'Bible',
        'nuclear',
        'discover',
        'fit',
        'irony',
        'shaft',
        'driver',
        'broccoli',
        'interrupt',
        'part',
        'contact',
        'path',
        'executive',
        'banner',
        'reality',
        'sentiment',
        'redundancy',
        'imposter',
        'descent',
        'damn',
        'frozen',
        'throne',
        'psychology',
        'reference',
        'incongruous',
        'will',
        'tolerate',
      ],
      randomWord: '',
      customCaptcha: '',
    }
  },
  computed: {
    showRecaptchaHelp: function () {
      return this.randomWord == this.customCaptcha && this.customCaptcha != '' ? false : true;
    }
  },
  methods: {
    setRandomWord: function () {
      this.randomWord = this.randomWords[Math.floor(Math.random() * this.randomWords.length)];
    },
    closeModal: function () {
      this.showThankYouModal = false;
      console.log('close modal')
    },
    getCSRF: () => {
      let csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
      return csrf;
    },

    sendContactForm: function(e) {

      if (!this.showRecaptchaHelp) {
        // disable sending
        this.enableSending = false;
        let form = e.target;
        let url = form.action;
        let data = {
          sender_message: this.message,
          sender_email: this.emailAddress,
          sender_name: this.name
        };
        let _this = this;
        axios.post(
          url,
          data,
          {
            headers: {
              "X-CSRFToken": this.getCSRF(),
            }
          })
        .then((response) => {
          form.reset();
          _this.showThankYouModal = true;
          setTimeout(() => { _this.enableSending = true; }, 30000);
        })
        .catch((error) => {
            console.log(error);
            _this.enableSending = true
          })
      } else {
        // recaptcha is needed
        this.recaptchaRequired = true;
      }
    }
  },
  mounted() {
    this.setRandomWord();
  }
});
