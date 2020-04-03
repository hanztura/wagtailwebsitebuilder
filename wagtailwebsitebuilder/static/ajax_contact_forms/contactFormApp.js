let contactForm = new Vue({
  name: 'ContactFormApp',
  el: '#contactForm',
  components: {
    'vue-recaptcha': VueRecaptcha,
  },
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
    }
  },
  computed: {
    showRecaptchaHelp: function () {
      return this.recaptcha ? false : true;
    }
  },
  methods: {
    closeModal: function () {
      this.showThankYouModal = false;
      console.log('close modal')
    },
    getCSRF: () => {
      let csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
      return csrf;
    },

    onVerify: function (response) {
      this.recaptcha = response;
      this.recaptchaRequired = false;
    },

    onExpired: function () {
      console.log('recaptcha expired');
      this.resetRecaptcha();
    },

    resetRecaptcha: function () {
      this.$refs.recaptcha.reset();
      this.recaptchaRequired = false;
    },

    sendContactForm: function(e) {
      this.$refs.recaptcha.execute();

      if (this.recaptcha) {
        // disable sending
        this.enableSending = false;

        let url = e.target.action;
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
            _this.showThankYouModal = true;
          })
        .catch((error) => {
            console.log(error);
          })
        .finally((e) => {
          _this.enableSending = true;
        })
      } else {
        // recaptcha is needed
        this.recaptchaRequired = true;
      }
    }
  }
});
