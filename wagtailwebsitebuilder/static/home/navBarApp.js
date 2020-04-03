let navBarApp = new Vue({
  name: 'NavBarApp',
  el: '#navBar',
  data: () => {
    return {
      burgerIsActive: false,
    }
  },
  methods: {
    toggleBurger: function () {
      this.burgerIsActive = !this.burgerIsActive;
    }
  }
});